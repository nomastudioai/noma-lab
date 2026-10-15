# Lab

Cada carpeta es un test de un lanzamiento de ComfyUI o de Claude, con este formato:

```
lab/AAAA-MM-DD_nombre-del-test/
  README.md        qué probamos, cómo, qué salió y qué haríamos distinto
  workflow.json    el workflow de ComfyUI, listo para arrastrar
  prompts/         los prompts exactos, uno por archivo
  resultados/      renders y comparaciones livianas (los pesados van linkeados)
```

El `README.md` de cada test arranca con este encabezado, que es lo que arma la tabla
del README principal:

```
---
title: Vidu Q4 y Fish Audio Drama 3, una escena de serie vertical
date: 2026-10-15
tools: ComfyUI, Vidu Q4 Preview, Fish Audio Drama 3
---
```

Las fotos de referencia de personas reales no se publican nunca. Los workflows que
usan una cara traen el nodo de carga vacío para que pongas la tuya.

Si vas a correr estos workflows en Comfy Cloud, entrá por
[nuestro link de afiliado](https://www.comfy.org/?via=nomastudioai).
