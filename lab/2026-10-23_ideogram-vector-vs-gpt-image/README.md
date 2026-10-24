---
title: Ideogram Vector contra GPT Image con el mismo prompt (zoom 28x)
date: 2026-10-23
tools: ComfyUI (Comfy Cloud), Ideogram Vector (Partner Node), OpenAI GPT Image (Partner Node, gpt-image-2)
---

# Vector contra píxeles: Ideogram Vector y GPT Image

El 22/10/2026 ComfyUI anunció el primer modelo vectorial de Ideogram. Los nodos `IdeogramVectorGenerateApi` e `IdeogramVectorImageToSVGApi` ya figuraban en Comfy Cloud el 23/10/2026. Lo probamos contra GPT Image con el mismo prompt (`prompts.md`) y un personaje propio de NoMa Studio AI: un capibara amigurumi.

| | Ideogram Vector | GPT Image |
|---|---|---|
| Nodo | `IdeogramVectorGenerateApi`, calidad high, 1:1 | `OpenAIGPTImageNodeV2`, `gpt-image-2`, 2048x2048, calidad high |
| Salida | SVG (67 KB) | PNG 2048x2048 |
| Costo estimado | 60 créditos | ~108 créditos |

Costo total estimado: ~169 créditos (estimación del servidor, no medido en factura).

## Observaciones

- A 28x sobre la nariz, el SVG mantiene bordes nítidos. El PNG se vuelve borroso y con bordes escalonados.
- GPT Image respeta mejor la textura de tejido crochet y el encuadre. El SVG dibuja al capibara más chico dentro del cuadro, con la capucha puesta, gotas de lluvia que el prompt no pedía y puntadas como trazos sueltos.
- Una sola corrida por modelo (seed 1): no es una comparación estadística.

## Cómo reproducirlo

Cargá `workflow_ideogram-vector_vs_gpt-image.json` en Comfy Cloud (formato API). Las imágenes se generan desde texto, sin fotos de referencia.

## Resultados

- `resultados/ideogram_vector_capy.svg`
- `resultados/gptimage_capy_1024.png` (reducido a 1024 px, el original es de 2048 px)
- `resultados/zoom_vector_vs_pixeles.mp4` (video de zoom, 9 s)
- `resultados/reel_vector_vs_pixeles_noma_v2.mp4` (reel con identidad NoMa V2, 15 s)
