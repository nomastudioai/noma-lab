---
title: Krea 3 vs FLUX 3 Image vs FLUX 3 Klein, edición con referencias y texto
date: 2026-10-16
tools: ComfyUI (Comfy Cloud), Krea 3 (Partner Node), FLUX 3 Image (Partner Node), FLUX 3 Image Klein (pesos abiertos)
---

# Krea 3 vs FLUX 3: edición con varias referencias

El 15/10/2026 llegaron a ComfyUI dos modelos de imagen que prometen lo mismo: editar con
varias referencias sin romper el resto de la escena. **Krea 3** entró como Partner Node y
**FLUX 3 Image Klein**, de Black Forest Labs, entró nativo con pesos abiertos. Los pusimos
a competir entre ellos y contra **FLUX 3 Image**, la versión de API de BFL.

Usamos material propio de NoMa Studio AI: una locación y un vestuario de Mala Praxis (serie
vertical) y una maqueta de Los Amigurumis. Mismo prompt, en inglés, para los tres modelos.

## Qué probamos

1. **Tres referencias a la vez.** Una cara (imagen 1), un vestuario (imagen 2) y una
   locación (imagen 3): "la persona de la imagen 1, con la ropa de la imagen 2, en la
   oficina de la imagen 3".
2. **Cambio de materiales.** En la maqueta del cuarto de Kiti, cambiar solo dos textiles
   (la alfombra y la manta) sin tocar el resto.
3. **Texto con tilde.** Agregar una placa de bronce que diga "DIRECCIÓN" en la puerta de
   la oficina.

## Qué salió

| | Krea 3 | FLUX 3 Image (API) | FLUX 3 Klein (abierto) |
|---|---|---|---|
| Caso 1: cara | Muy parecida a la referencia | La que más se aleja | Muy parecida a la referencia |
| Caso 1: locación | La reencuadra más cerca, se reconoce | Idéntica, casi píxel a píxel | La reinterpreta (cambia el encuadre y el escritorio) |
| Caso 2: materiales | Cambia los dos textiles y respeta todo lo demás | Cambia los dos textiles y respeta todo lo demás | Cambia los textiles, pero pierde el almohadón y mueve un poco el encuadre |
| Caso 3: "DIRECCIÓN" | Bien escrito, con tilde | Bien escrito, con tilde, la placa mejor integrada | Sin tilde ("DIRECCION") y letras algo deformadas |
| Salida | 2736 x 1536 | 2704 x 1520 | 1360 x 768 (lo que pedimos) |

- **Krea 3** fue el más parejo: buena cara, buena edición puntual y texto correcto.
- **FLUX 3 Image (API)** es el que mejor conserva la escena original, pero en el caso de
  la cara quedó atrás.
- **FLUX 3 Klein** sorprende para ser abierto y de 5,6B parámetros: la cara salió muy bien.
  Pierde en texto y en conservar el encuadre exacto.
- Estimador de Comfy Cloud: unos 15 créditos por imagen con Krea 3 a 2K y 14 con FLUX 3
  Image a 2K. Klein no usa créditos de API, solo tiempo de GPU.

Es una sola corrida por caso, con seed fija. Con otras imágenes, otros prompts o más
intentos el resultado puede cambiar.

## Un detalle para armar el workflow de Krea 3 a mano

Las imágenes de Krea 3 van en las entradas `model.images.image_1`, `model.images.image_2`,
etc. Con `model.images.item_1` el nodo falla en Comfy Cloud.

## Archivos

- `workflow_krea3_multiref.json`: caso 1 con Krea 3.
- `workflow_flux3-api_multiref.json`: caso 1 con FLUX 3 Image (API).
- `workflow_flux3-klein_multiref.json`: caso 1 con FLUX 3 Klein (distilled, 16 pasos).
  Para los casos 2 y 3 dejá una sola imagen conectada.
- `prompts.md`: los tres prompts completos.
- `resultados/`: comparativas de los casos 2 y 3.

Los workflows están en formato API de ComfyUI y traen los nodos de carga vacíos: poné tus
propias imágenes. No publicamos fotos de personas reales, por eso el caso 1 no tiene
imagen en esta carpeta.

---

Hecho por [NoMa Studio AI](https://nomastudio.ai). Somos afiliados de ComfyUI: si lo
vas a probar en la nube, entrá por [nuestro link](https://www.comfy.org/?via=nomastudioai).
