"""Corre las pruebas de pruebas.json en OmniHuman 2.0 o 1.5 (BytePlus Vision AI) y baja cada video.

Uso:
    pip install --upgrade byteplus-sdk
    set BYTEPLUS_AK=...   (o export en Linux/macOS)
    set BYTEPLUS_SK=...
    python correr_omnihuman.py [--v15] [T1 T2 ...]

Las claves se leen de las variables de entorno y nunca se imprimen. Cada prueba necesita una
imagen_url y un audio_url públicos de descarga directa. La cuenta corre una tarea a la vez (error
50430 si mandás otra), así que el script las manda en fila. El link del video vence en una hora:
se baja apenas termina. Todo queda en outputs/<modelo>_log.jsonl.
"""
import json
import os
import subprocess
import sys
import time
import urllib.request

from byteplus_sdk.visual.VisualService import VisualService

AQUI = os.path.dirname(os.path.abspath(__file__))
V15 = "--v15" in sys.argv
if V15:
    sys.argv.remove("--v15")
# 1.5 usa CVSubmitTask/CVGetResult, una sola image_url y output_resolution; 2.0 usa el par Sync2Async.
REQ_KEY = "realman_avatar_picture_omni15_cv" if V15 else "realman_avatar_picture_omni20_cv"
PREFIJO = "OH15" if V15 else "OH2"
SALIDA = os.path.join(AQUI, "outputs")
os.makedirs(SALIDA, exist_ok=True)
LOG = os.path.join(SALIDA, f"{PREFIJO}_log.jsonl")


def log(evento):
    evento["t"] = time.strftime("%Y-%m-%dT%H:%M:%S")
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(json.dumps(evento, ensure_ascii=False) + "\n")
    print(json.dumps(evento, ensure_ascii=False)[:300], flush=True)


def buscar_video(obj):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if "video_url" in k and isinstance(v, str) and v.startswith("http"):
                return v
            r = buscar_video(v)
            if r:
                return r
    elif isinstance(obj, list):
        for v in obj:
            r = buscar_video(v)
            if r:
                return r
    elif isinstance(obj, str) and obj.startswith("{"):
        try:
            return buscar_video(json.loads(obj))
        except ValueError:
            return None
    return None


def bajar(url, destino):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=300) as r, open(destino, "wb") as f:
        f.write(r.read())


def specs(ruta):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration:stream=width,height,r_frame_rate",
                          "-of", "json", ruta], capture_output=True, text=True).stdout
    return json.loads(out) if out else None


def main():
    pruebas = json.load(open(os.path.join(AQUI, "pruebas.json"), encoding="utf-8"))["pruebas"]
    if len(sys.argv) > 1:
        pruebas = [p for p in pruebas if p["id"] in sys.argv[1:]]
    svc = VisualService()
    svc.set_ak(os.environ["BYTEPLUS_AK"])
    svc.set_sk(os.environ["BYTEPLUS_SK"])

    pendientes, activas = list(pruebas), {}
    while pendientes or activas:
        while pendientes:
            p = pendientes[0]
            if V15:
                body = {"req_key": REQ_KEY, "image_url": p["imagen_url"], "audio_url": p["audio_url"],
                        "prompt": p["prompt"], "output_resolution": 720}
            else:
                body = {"req_key": REQ_KEY, "image_urls": [p["imagen_url"]], "audio_url": p["audio_url"],
                        "prompt": p["prompt"], "enable_watermark": False}
            try:
                resp = svc.cv_submit_task(body) if V15 else svc.cv_sync2async_submit_task(body)
            except Exception as e:  # noqa: BLE001
                if "50429" in str(e) or "50430" in str(e):
                    break
                log({"id": p["id"], "evento": "error_envio", "detalle": str(e)[:500]})
                pendientes.pop(0)
                continue
            if resp.get("code") in (50429, 50430):
                break
            if resp.get("code") != 10000:
                log({"id": p["id"], "evento": "rechazo_envio", "resp": resp})
                pendientes.pop(0)
                continue
            activas[p["id"]] = {"p": p, "task_id": resp["data"]["task_id"], "t0": time.time()}
            log({"id": p["id"], "evento": "enviada", "task_id": resp["data"]["task_id"]})
            pendientes.pop(0)

        time.sleep(15)
        for pid in list(activas):
            a = activas[pid]
            consulta = {"req_key": REQ_KEY, "task_id": a["task_id"]}
            try:
                resp = svc.cv_get_result(consulta) if V15 else svc.cv_sync2async_get_result(consulta)
            except Exception as e:  # noqa: BLE001
                log({"id": pid, "evento": "error_consulta", "detalle": str(e)[:300]})
                continue
            data = resp.get("data") or {}
            if data.get("status") == "done":
                url = buscar_video(data)
                if url:
                    destino = os.path.join(SALIDA, f"{PREFIJO}_{pid}_{a['p']['nombre']}.mp4")
                    bajar(url, destino)
                    log({"id": pid, "evento": "bajada", "seg_generacion": round(time.time() - a["t0"]),
                         "specs": specs(destino)})
                else:
                    log({"id": pid, "evento": "done_sin_video"})
                del activas[pid]
            elif data.get("status") in ("not_found", "expired") or resp.get("code") not in (10000, None):
                log({"id": pid, "evento": "fallo", "resp": resp})
                del activas[pid]


if __name__ == "__main__":
    main()
