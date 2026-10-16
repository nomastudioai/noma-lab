---
title: Stress test de OmniHuman 2.0 (y comparación con la 1.5)
date: 2026-10-16
tools: OmniHuman 2.0 y 1.5 (BytePlus Vision AI, API), Suno v6, ElevenLabs, ffmpeg
---

# Stress test de OmniHuman 2.0

OmniHuman es el modelo de avatares de BytePlus: le das una imagen y un audio, y te devuelve un
video donde ese personaje dice o canta ese audio. El prompt es opcional y dirige la actuación y
la cámara. A diferencia de los modelos de video que generan su propia voz, usa el audio tal cual.

Lo probamos el 16/10/2026 por API, con seis pruebas sobre material propio, y corrimos las cinco
primeras también en OmniHuman 1.5 para comparar.

## Las pruebas

| Prueba | Qué mide | Audio | Resultado en 2.0 |
|---|---|---|---|
| T1 dos personas | Dos caras en cuadro y un diálogo de dos voces | 8,9 s | Cada línea sale de la boca correcta |
| T2 primer plano | Sincronía de cerca, un gesto y un acercamiento pedidos en el prompt | 4,9 s | Hace el gesto y el acercamiento |
| T3 personaje tejido | Un muñeco al crochet sin boca, cantando sobre la mezcla con música | 15,0 s | Le arma una boca de títere tejida que sigue el canto |
| T4 anime | Animación 2D con un prop cerca de la boca y dos líneas | 11,2 s | Respeta el trazo y el prop |
| T5 toma larga | 34 s con voz clonada y tres tramos de actuación | 33,6 s | La identidad no se mueve; los tramos no siguen los tiempos pedidos |
| T6 trap | Un avatar ilustrado cantando un trap hecho en Suno | 42,1 s | 43 s cantando sin perder la cara |

Los prompts completos y lo que mide cada prueba están en [pruebas.json](pruebas.json). La letra y el
estilo de la canción de Suno están en [cancion/](cancion/). Las imágenes de entrada no se
publican.

## 2.0 contra 1.5

La 2.0 ganó en cuatro de cinco pruebas. La 1.5 le hizo decir al personaje equivocado una línea del
diálogo (su documentación aclara que un solo audio no maneja un diálogo entre dos personajes),
dibujó dentro del cuadro a un personaje que el prompt ubicaba fuera de cámara, y en la toma larga
la cara se alejó de la original. En el personaje tejido, la 1.5 fue más fiel al diseño (abrió la
puntada en vez de inventar una boca), pero el canto casi no se lee.

## Lo que medimos de la API

- Salida a 720p, 24 fps en la 2.0 y 25 fps en la 1.5.
- El primer cuadro es la imagen de entrada, idéntica: se puede empalmar con el plano original.
- La cuenta corre una tarea a la vez (error 50430 si mandás otra).
- Precio de consola al 16/10/2026: 0,07 USD por segundo la 2.0 y 0,12 USD la 1.5.

## Cómo se usa el script

1. `pip install --upgrade byteplus-sdk` y tener `ffprobe` en el PATH.
2. Habilitá OmniHuman en la consola de Vision AI de BytePlus y creá un par de claves.
3. Cargá las claves en las variables de entorno `BYTEPLUS_AK` y `BYTEPLUS_SK`.
4. En `pruebas.json`, completá `imagen_url` y `audio_url` de cada prueba con links públicos de
   descarga directa.
5. `python correr_omnihuman.py` corre todo en 2.0; `python correr_omnihuman.py --v15 T1 T2` corre
   las pruebas que elijas en 1.5.

Escrito para los prompts: con 2.0, una o dos indicaciones claras de gesto o cámara funcionan; una
coreografía por tramos no. Si el prompt manda la mirada a un costado, la cara queda de perfil y la
sincronía se deja de leer. Con 1.5, no nombres en el prompt a nadie que no tenga que aparecer: lo
dibuja.
