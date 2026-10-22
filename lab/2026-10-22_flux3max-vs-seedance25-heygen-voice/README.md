---
title: FLUX 3 Max vs Seedance 2.5 (Kiti habla) y HeyGen Voice Turbo vs ElevenLabs
date: 2026-10-22
tools: ComfyUI (Comfy Cloud), FLUX 3 Max (Partner Node), BytePlus ModelArk (Seedance 2.5), HeyGen Voice 1.0 (Partner Node), ElevenLabs
---

# Dos tests del 22/10/2026

El 21/10/2026 ComfyUI sumó **FLUX 3 Max** (video con audio) y **Voice Turbo de HeyGen**. Los probamos con material propio de NoMa Studio AI.

## Test 1: Kiti habla, FLUX 3 Max contra Seedance 2.5

Mismo cuadro inicial (Kiti, de Los Amigurumis), mismo prompt (`prompt_kiti_motion.txt`, en inglés) y una frase en castellano rioplatense con audio nativo.

| | FLUX 3 Max | Seedance 2.5 |
|---|---|---|
| Plataforma | Comfy Cloud, template `api_flux3_max_i2v` | BytePlus ModelArk directo, `first_frame` |
| Resolución | 720p (no ofrece 480p) | 480p |
| Duración | 5 s | 8 s |
| Costo | 64 créditos | ~0,82 USD (0,103 USD/s de lista, no medido en factura) |

Observación por cuadros: los dos mantienen la identidad (boina, bufanda, textura de crochet). FLUX mueve la boca desde el segundo 2; Seedance cierra los ojos varias veces y abre la boca hacia el final. La voz y el acento no se evaluaron por escucha en este README: [PENDIENTE: evaluación de audio].

## Test 2: HeyGen Voice 1.0 Turbo y Standard contra un clon de ElevenLabs

Una muestra de 20 s, generada con un clon de voz de ElevenLabs (no es una grabación real), se clonó con HeyGen Instant Clone. El mismo texto (`guion_voz.txt`) lo dicen HeyGen Turbo, HeyGen Standard y el clon de ElevenLabs. Costo estimado en Comfy Cloud para HeyGen: 0 créditos (el Instant Clone es gratis durante el preview de HeyGen).

El workflow queda en `workflows/heygen_voice_turbo_vs_standard.json` con el nodo de carga de audio vacío: cargá tu propia muestra.

## Resultados

- `videos/reel_kiti_flux3max_vs_seedance25.mp4`
- `videos/reel_voces_heygen_vs_elevenlabs.mp4`
