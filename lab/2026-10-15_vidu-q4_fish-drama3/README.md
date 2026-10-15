---
title: Vidu Q4 Preview y Fish Audio Drama 3, una escena de serie con dos personajes que hablan
date: 2026-10-15
tools: ComfyUI (Comfy Cloud), Vidu Q4 Preview, Fish Audio Drama 3, Fish Audio Instant Voice Clone, Seedance 2.0 mini
---

# Vidu Q4 Preview y Fish Audio Drama 3

En una semana llegaron dos Partner Nodes a ComfyUI que nos interesaban para nuestras series
verticales: **Vidu Q4 Preview** (07/10/2026), un modelo de video que promete mejor
actuación y voces consistentes, y **Fish Audio Drama 3** (13/10/2026), que genera una
escena de varias voces de una sola pasada.

Los probamos con una escena corta de Mala Praxis, una serie vertical de NoMa Studio AI:
el director del hospital le pregunta a su secretaria por su diploma.

## Qué probamos

1. **Voces con Fish Audio.** Dos muestras de cada actor (de 10 a 30 s) en el nodo
   Instant Voice Clone, y la escena completa en Drama 3 con `@Voice1` y `@Voice2`, dirigida
   con indicaciones entre corchetes (`[long pause]`, `[soft tone]`).
2. **La escena con Vidu Q4 Preview** (Reference to Video): las hojas de personaje y la
   locación como imágenes de referencia, y una muestra de voz de cada actor (de 3 a 12 s)
   como referencia de timbre. El diálogo va escrito en el prompt.
3. **La misma escena con Seedance 2.0 mini**, con el audio de Fish Audio como referencia
   para la boca: primero con el audio generado activado y después apagado, con la pista de
   Fish Audio puesta encima.

## Qué salió

- **Vidu Q4** armó la oficina como la describimos (incluido el clavo vacío en la pared),
  hizo el gesto de la mano en el pelo y el corte a la secretaria, y dijo bien cada palabra
  en rioplatense. El estimador de Comfy marca 94,9 créditos por una toma de 10 s a 540p.
- **Fish Audio Drama 3** clonó las dos voces y generó la escena con la pausa que le
  pedimos. La segunda toma (seed 7) respetó mejor la pausa larga.
- **Seedance 2.0 mini con audio generado** vuelve a decir el diálogo con su propia voz y
  deformó palabras. Con el audio generado apagado y la pista de Fish Audio encima, el
  camino funciona.
- **Veredicto para nuestro pipeline:** para escenas cortas con diálogo, Vidu Q4 nos
  sorprendió. Seedance sigue siendo el modelo que más usamos en producción.

Es una prueba sobre una sola escena. Con otros personajes, idiomas o duraciones el
resultado puede cambiar.

## Archivos

- `workflow_fish-audio-drama3.json`: clonado de dos voces y escena de diálogo.
- `workflow_vidu-q4.json`: escena de dos personajes con referencias de imagen y de voz.
- `prompt_vidu-q4.md`: el prompt completo de la escena.

Los workflows están en formato API de ComfyUI y traen los nodos de carga vacíos: poné tus
propias hojas de personaje, tu locación y tus muestras de voz. No publicamos fotos ni
voces de personas reales.

---

Hecho por [NoMa Studio AI](https://nomastudio.ai). Somos afiliados de ComfyUI: si lo
vas a probar en la nube, entrá por [nuestro link](https://www.comfy.org/?via=nomastudioai).
