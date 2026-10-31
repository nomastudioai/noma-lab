---
title: Kling 4.0 y Pika H3 Flex contra Seedance 2.5 y 2.0 mini con un personaje realista
date: 2026-10-31
tools: ComfyUI (Comfy Cloud), Kling 4.0 (Partner Node), Pika H3 Flex (template MiniMax H3 con LoRA), BytePlus ModelArk (Seedance 2.5, Seedance 2.0 mini, Seedream 5.0 pro)
---

# Cuatro modelos de video con el mismo cuadro realista

El 30/10/2026 y el 31/10/2026 ComfyUI anunció Pika H3 Flex y Kling 4.0. Los probamos contra Seedance 2.5 y Seedance 2.0 mini con el mismo cuadro inicial y el mismo prompt (`prompts.md`): Emma, un personaje de NN pasado a realismo con Seedream 5.0 pro, parada en una avenida mojada de Buenos Aires en 2077 y hablando una línea en rioplatense.

| Modelo | Dónde corre | Resolución | Costo |
|---|---|---|---|
| Kling 4.0 (imagen a video) | Comfy Cloud, `api_kling4_i2v` | 720p | 237 créditos (estimado) |
| Pika H3 Flex (referencia a video) | Comfy Cloud, `video_pika_h3_flex_ref2va` | 768x1344 | 0 créditos de API, GPU de Cloud [PENDIENTE: fuente] |
| Seedance 2.5 | ModelArk, referencia de imagen | 480p | ~0,52 USD (tarifa de lista) |
| Seedance 2.0 mini | ModelArk, primer cuadro | 480p | ~0,07 USD (tarifa de lista) |
| Cuadro inicial, Seedream 5.0 pro | ModelArk | 1080x1920 | ~0,045 USD (tarifa de lista) |

Todos con 5 s, 9:16 y audio activado. Los costos son estimaciones, no medidos en factura.

## Observaciones

- Los cuatro mantienen el pelo rojo, la campera, el pantalón cargo y el Obelisco detrás.
- Kling 4.0 y Seedance 2.5 sostienen el rostro y los aros largos dorados del cuadro inicial.
- Pika H3 Flex mantiene la identidad con el maquillaje más marcado.
- Seedance 2.0 mini cambia los aros largos por argollas.
- La voz, el acento y la sincronía labial no se evaluaron por escucha.
- Una sola corrida por modelo: no es una comparación estadística. Seedance 2.5 con `first_frame` devolvió error 400 y se reintentó como `reference_image`.

## Cómo reproducirlo

Los templates `api_kling4_i2v` y `video_pika_h3_flex_ref2va` están en Comfy Cloud. Cargá tu propio cuadro inicial en el nodo de carga de imagen (el cuadro de este test, `resultados/emma_real_frame_v01.png`, es de un personaje ficticio). Para Seedance usá la API de ModelArk con el modelo `dreamina-seedance-2-5-260628` o `dreamina-seedance-2-0-mini-260615`.

## Resultados

- `resultados/emma_comparacion_4modelos.mp4`: los cuatro clips lado a lado, sin audio.
- `resultados/emma_real_frame_v01.png`: el cuadro inicial.
