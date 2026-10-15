# NoMa Lab

El laboratorio abierto de [NoMa Studio AI](https://nomastudio.ai). Cada vez que
ComfyUI o Claude lanzan algo, lo probamos con material de nuestras producciones y
publicamos acá el workflow, los prompts y lo que salió, bien o mal.

Además está la base de prompts de IA generativa que usamos de verdad en producción,
con el modelo exacto con el que funcionaron. No son prompts de ejemplo ni generados
para el repo: si un prompt está acá es porque dio un resultado que usamos.

**2 tests**, **96 prompts** y **3 workflows de ComfyUI**.

> Somos afiliados de ComfyUI y de Claude. Si vas a probar Comfy Cloud para correr
> estos workflows, entrá por [nuestro link](https://www.comfy.org/?via=nomastudioai): nos ayuda a seguir
> publicando tests.

## Lab

| Fecha | Test | Herramientas |
|---|---|---|
| 2026-10-15 | [Vidu Q4 Preview y Fish Audio Drama 3, una escena de serie con dos personajes que hablan](lab/2026-10-15_vidu-q4_fish-drama3/README.md) | ComfyUI (Comfy Cloud), Vidu Q4 Preview, Fish Audio Drama 3, Fish Audio Instant Voice Clone, Seedance 2.0 mini |
| 2026-10-15 | [Nodos VFX de NVIDIA RTX contra Topaz, upscaling de anime 480p a 1080p](lab/2026-10-15_nvidia-rtx-vfx/README.md) | ComfyUI (Comfy Cloud), RTX Video Super Resolution, RTX Video Frame Generation, Topaz Proteus |

## Prompts

> **Esto se mantiene y se agranda todo el tiempo.** Sumamos un test por cada
> lanzamiento que vale la pena y prompts a medida que producimos. Si te sirve,
> ponele una estrella y te enterás de lo que agregamos.

### Cómo usarlo

Cada prompt es un `.md` con el texto en un bloque de código, listo para copiar, y
un encabezado con el modelo y los parámetros que importan (relación de aspecto,
duración, resolución). Los workflows son `.json` que se arrastran a ComfyUI.

Un detalle que ahorra frustración: **los prompts que empiezan con `the man from
reference image 1` o similar necesitan tus propias imágenes de referencia**. El
texto solo no alcanza, describe qué hacer con una referencia que tenés que poner vos.

### Modelos

| Modelo | Prompts |
|---|---|
| Nano Banana Pro | 29 |
| Seedream 5.0 Pro | 14 |
| GPT Image 2 | 13 |
| Seedream 4.5 | 7 |
| Kling Omni Pro (imagen a video) | 6 |
| ElevenLabs SFX v2 | 5 |
| ElevenLabs Sound Generation | 4 |
| Seedance 2.0 mini | 4 |
| ElevenLabs Multilingual v2 | 3 |
| Seedance 2.0 | 3 |
| Gemini 3 Pro Image | 3 |
| Seedream (BytePlus) | 2 |
| Kling Avatar | 2 |
| Kling Omni Pro (primer y ultimo frame) | 1 |
| Stable Audio 2.5 | 1 |
| Sonilo (texto a musica) | 1 |
| Seedance | 1 |

### Video (17)

- [30 second realistic comedy: profile picture comes alive, celebrates 10k followers, clones multiply and squish against ca](prompts/video/30-second-realistic-comedy-profile-picture-comes-alive-celebrates-10k.md) · `Kling Omni Pro (primer y ultimo frame)`
- [epic anime cavalry charging in a blizzard, cinematic](prompts/video/epic-anime-cavalry-charging-in-a-blizzard-cinematic.md) · `Seedance 2.0 mini`
- [Epic historical seinen anime film: Argentine cavalry crossing the snowy Andes toward a glowing stadium.](prompts/video/epic-historical-seinen-anime-film-argentine-cavalry-crossing-the-snowy-2.md) · `Kling Omni Pro (imagen a video)`
- [Epic historical seinen anime film: Argentine cavalry crossing the snowy Andes.](prompts/video/epic-historical-seinen-anime-film-argentine-cavalry-crossing-the-snowy.md) · `Kling Omni Pro (imagen a video)`
- [Epic historical seinen anime film: Argentine cavalry revealing a glowing stadium from a snowy summit.](prompts/video/epic-historical-seinen-anime-film-argentine-cavalry-revealing-a-glowin.md) · `Kling Omni Pro (imagen a video)`
- [FPV drone one-take flight through Buenos Aires at night (Obelisco, Caminito, Puerto Madero)](prompts/video/fpv-drone-one-take-flight-through-buenos-aires-at-night-obelisco-camin.md) · `Seedance 2.0`
- [Painterly seinen anime style like Attack on Titan, cinematic, epic, film grain.](prompts/video/painterly-seinen-anime-style-like-attack-on-titan-cinematic-epic-film.md) · `Seedance 2.0 mini`
- [Painterly seinen anime style, snowy mountain scenes with the general from the reference image.](prompts/video/painterly-seinen-anime-style-snowy-mountain-scenes-with-the-general-fr.md) · `Kling Omni Pro (imagen a video)`
- [script_test](prompts/video/script-test.md) · `Seedance`
- [Seedance reference-to-video multishot](workflows/NN-E01-Seedance-R2V-multishot.json) · `Seedance 2.0`
- [The five soldiers from the reference images stand in a line on a snowy mountain ridge at dawn, snow falling, camera slow](prompts/video/the-five-soldiers-from-the-reference-images-stand-in-a-line-on-a-snowy.md) · `Kling Omni Pro (imagen a video)`
- [The general from the reference image, keeping his exact face and uniform, rides a black horse through falling snow towar](prompts/video/the-general-from-the-reference-image-keeping-his-exact-face-and-unifor.md) · `Kling Omni Pro (imagen a video)`
- [the man from reference image 1 rides a black horse through snow, anime style](prompts/video/the-man-from-reference-image-1-rides-a-black-horse-through-snow-anime.md) · `Seedance 2.0 mini`
- [the man from reference image 1 rides a black horse...](prompts/video/the-man-from-reference-image-1-rides-a-black-horse.md) · `Seedance 2.0 mini`
- [The man speaks directly into the camera lens, making eye contact with the viewer, calm confident delivery, subtle natura](prompts/video/the-man-speaks-directly-into-the-camera-lens-making-eye-contact-with-t.md) · `Kling Avatar`
- [The man speaks to camera with calm confidence, subtle natural head movement, static shot.](prompts/video/the-man-speaks-to-camera-with-calm-confidence-subtle-natural-head-move.md) · `Kling Avatar`
- [Yuko hoverboard chase through 2077 Buenos Aires night market, Seedance 2.0 txt2video 15s 9:16 720p with sound](prompts/video/yuko-hoverboard-chase-through-2077-buenos-aires-night-market-seedance.md) · `Seedance 2.0`

### Imagen (68)

- [2D cel anime keyframe, Cyberpunk: Edgerunners / Studio Trigger style, bold linework, saturated neon palette.](prompts/image/2d-cel-anime-keyframe-cyberpunk-edgerunners-studio-trigger-style-bold.md) · `GPT Image 2`
- [arquero granadero sin logo](prompts/image/arquero-granadero-sin-logo.md) · `Nano Banana Pro`
- [Casa Rosada anime energia](prompts/image/casa-rosada-anime-energia.md) · `Nano Banana Pro`
- [Character reference sheet of the man in the reference photo as a modern Argentine national football player.](prompts/image/character-reference-sheet-of-the-man-in-the-reference-photo-as-a-moder.md) · `Nano Banana Pro`
- [Character reference sheet of the man in the reference photo as a modern Argentine national football player.](prompts/image/character-reference-sheet-of-the-man-in-the-reference-photo-as-a-moder-2.md) · `Nano Banana Pro`
- [Character reference sheet of the man in the reference photo as a modern Argentine national football player.](prompts/image/character-reference-sheet-of-the-man-in-the-reference-photo-as-a-moder-3.md) · `Nano Banana Pro`
- [Character reference sheet of the man in the reference photo as a modern Argentine national football player.](prompts/image/character-reference-sheet-of-the-man-in-the-reference-photo-as-a-moder-4.md) · `Nano Banana Pro`
- [Character reference sheet of the man in the reference photo as a modern Argentine national football player.](prompts/image/character-reference-sheet-of-the-man-in-the-reference-photo-as-a-moder-5.md) · `Nano Banana Pro`
- [Character reference sheet of the man in the reference photo as a modern Argentine national football player.](prompts/image/character-reference-sheet-of-the-man-in-the-reference-photo-as-a-moder-6.md) · `Nano Banana Pro`
- [Character reference sheet of the man in the reference photo as a modern Spain national football player, a goalkeeper wea](prompts/image/character-reference-sheet-of-the-man-in-the-reference-photo-as-a-moder-7.md) · `Nano Banana Pro`
- [Character reference sheet of the young man from the FIRST reference photo.](prompts/image/character-reference-sheet-of-the-young-man-from-the-first-reference-ph.md) · `Seedream 4.5`
- [Character reference sheet of the young man from the FIRST reference photo.](prompts/image/character-reference-sheet-of-the-young-man-from-the-first-reference-ph-2.md) · `Seedream 4.5`
- [Character reference sheet of the young man from the FIRST reference photo.](prompts/image/character-reference-sheet-of-the-young-man-from-the-first-reference-ph-3.md) · `Seedream 5.0 Pro`
- [Character reference sheet of the young man from the FIRST reference photo.](prompts/image/character-reference-sheet-of-the-young-man-from-the-first-reference-ph-4.md) · `Seedream (BytePlus)`
- [Character reference sheet of the young man shown in the FIRST reference photo.](prompts/image/character-reference-sheet-of-the-young-man-shown-in-the-first-referenc.md) · `Nano Banana Pro`
- [Character reference sheet of the young man shown in the FIRST reference photo.](prompts/image/character-reference-sheet-of-the-young-man-shown-in-the-first-referenc-2.md) · `Seedream 4.5`
- [Debut silhouette trophy cathedral GOAT graffiti darker v02](prompts/image/debut-silhouette-trophy-cathedral-goat-graffiti-darker-v02.md) · `GPT Image 2`
- [Debut silhouette with trophy cathedral behind for hold-to-reveal](prompts/image/debut-silhouette-with-trophy-cathedral-behind-for-hold-to-reveal.md) · `GPT Image 2`
- [defensor granadero sin logo](prompts/image/defensor-granadero-sin-logo.md) · `Nano Banana Pro`
- [Edit image 1 with one single change: reshape the running character's coral starburst head so it matches the Claude logo](prompts/image/edit-image-1-with-one-single-change-reshape-the-running-characters-cor.md) · `Nano Banana Pro`
- [Edit this character reference sheet.](prompts/image/edit-this-character-reference-sheet.md) · `Seedream 4.5`
- [Edit this character reference sheet.](prompts/image/edit-this-character-reference-sheet-2.md) · `Seedream 4.5`
- [Edit this character reference sheet.](prompts/image/edit-this-character-reference-sheet-3.md) · `Seedream 4.5`
- [Edit this square meme.](prompts/image/edit-this-square-meme.md) · `GPT Image 2`
- [frame cero con GPT Image 2](workflows/NN-E01-FrameCero-gptimage2.json) · `GPT Image 2`
- [Full-body character reference sheet, single subject, on a plain light-grey studio background.](prompts/image/full-body-character-reference-sheet-single-subject-on-a-plain-light-gr.md) · `Seedream (BytePlus)`
- [Gavi kit rojo retry](prompts/image/gavi-kit-rojo-retry.md) · `Nano Banana Pro`
- [Generate 5 separate character reference sheets, one per character, all sharing the exact same art style: dark realistic](prompts/image/generate-5-separate-character-reference-sheets-one-per-character-all-s.md) · `Seedream 4.5`
- [granadero extra ref uniforme azul](prompts/image/granadero-extra-ref-uniforme-azul.md) · `Nano Banana Pro`
- [Humorous editorial cartoon meme, square 1:1 format.](prompts/image/humorous-editorial-cartoon-meme-square-11-format.md) · `Nano Banana Pro`
- [Image 1 is the canonical character sheet: her exact suit design, body surface, hair, mask and proportions.](prompts/image/image-1-is-the-canonical-character-sheet-her-exact-suit-design-body-su.md) · `GPT Image 2`
- [jugador granadero sin logo](prompts/image/jugador-granadero-sin-logo.md) · `Nano Banana Pro`
- [jugador granadero sin logo](prompts/image/jugador-granadero-sin-logo-2.md) · `Nano Banana Pro`
- [Keep the exact same 3D stylized character, the same face, hair and beard, and the same black t-shirt with the identical](prompts/image/keep-the-exact-same-3d-stylized-character-the-same-face-hair-and-beard.md) · `Gemini 3 Pro Image`
- [Keep the exact same 3D stylized character, the same face, hair and beard, and the same black t-shirt with the identical](prompts/image/keep-the-exact-same-3d-stylized-character-the-same-face-hair-and-beard-2.md) · `Gemini 3 Pro Image`
- [Keep the exact same 3D stylized character, the same face, hair and beard, and the same black t-shirt with the identical](prompts/image/keep-the-exact-same-3d-stylized-character-the-same-face-hair-and-beard-3.md) · `Gemini 3 Pro Image`
- [Licha granadero sin logo](prompts/image/licha-granadero-sin-logo.md) · `Nano Banana Pro`
- [Meme Fable escapando Alcatraz v2 - texto FABLE 5 IS FREE, logo Claude real](prompts/image/meme-fable-escapando-alcatraz-v2---texto-fable-5-is-free-logo-claude-r.md) · `Nano Banana Pro`
- [Meme Fable escapando de Alcatraz perseguido por ICE, logo de Claude](prompts/image/meme-fable-escapando-de-alcatraz-perseguido-por-ice-logo-de-claude.md) · `Nano Banana Pro`
- [Monumento Bandera Rosario anime energia](prompts/image/monumento-bandera-rosario-anime-energia.md) · `Nano Banana Pro`
- [Obelisco anime energia](prompts/image/obelisco-anime-energia.md) · `Nano Banana Pro`
- [Paredes granadero sin logo](prompts/image/paredes-granadero-sin-logo.md) · `Nano Banana Pro`
- [Perito Moreno anime energia](prompts/image/perito-moreno-anime-energia.md) · `Nano Banana Pro`
- [Redraw the exact man shown in reference image 1 (face close-up) and reference image 2 (full body) as an anime character,](prompts/image/redraw-the-exact-man-shown-in-reference-image-1-face-close-up-and-refe.md) · `Seedream 5.0 Pro`
- [San Martin (diez) granadero sin logo](prompts/image/san-martin-diez-granadero-sin-logo.md) · `Nano Banana Pro`
- [Silent Death frontal close deep V plating hand on shoulder](prompts/image/silent-death-frontal-close-deep-v-plating-hand-on-shoulder.md) · `GPT Image 2`
- [Silent Death frontal close shot hand on shoulder eyes dominant](prompts/image/silent-death-frontal-close-shot-hand-on-shoulder-eyes-dominant.md) · `GPT Image 2`
- [Silent Death low-key sensual portrait for X hold-to-reveal trend](prompts/image/silent-death-low-key-sensual-portrait-for-x-hold-to-reveal-trend.md) · `GPT Image 2`
- [Silent Death v04 edit multiref canonico tight close](prompts/image/silent-death-v04-edit-multiref-canonico-tight-close.md) · `GPT Image 2`
- [Silent Death v04 tight close canonical porcelain suit blazing teeth](prompts/image/silent-death-v04-tight-close-canonical-porcelain-suit-blazing-teeth.md) · `GPT Image 2`
- [Silent Death waist-up medium shot white hair high detail](prompts/image/silent-death-waist-up-medium-shot-white-hair-high-detail.md) · `GPT Image 2`
- [Tagliafico granadero sin logo](prompts/image/tagliafico-granadero-sin-logo.md) · `Nano Banana Pro`
- [Turn the man from reference image 1 into an anime character.](prompts/image/turn-the-man-from-reference-image-1-into-an-anime-character.md) · `Seedream 5.0 Pro`
- [Turn the man from reference image 1 into an anime character.](prompts/image/turn-the-man-from-reference-image-1-into-an-anime-character-2.md) · `Seedream 5.0 Pro`
- [Turn the man from reference image 1 into an anime character.](prompts/image/turn-the-man-from-reference-image-1-into-an-anime-character-3.md) · `Seedream 5.0 Pro`
- [Turn the man from reference image 1 into an anime character.](prompts/image/turn-the-man-from-reference-image-1-into-an-anime-character-4.md) · `Seedream 5.0 Pro`
- [Turn the man from reference image 1 into an anime character.](prompts/image/turn-the-man-from-reference-image-1-into-an-anime-character-5.md) · `Seedream 5.0 Pro`
- [Turn the man from reference image 1 into an anime character.](prompts/image/turn-the-man-from-reference-image-1-into-an-anime-character-6.md) · `Seedream 5.0 Pro`
- [Turn the man from reference image 1 into an anime character.](prompts/image/turn-the-man-from-reference-image-1-into-an-anime-character-7.md) · `Seedream 5.0 Pro`
- [Turn the man from reference image 1 into an anime character.](prompts/image/turn-the-man-from-reference-image-1-into-an-anime-character-8.md) · `Seedream 5.0 Pro`
- [Turn the man from reference image 1 into an anime character.](prompts/image/turn-the-man-from-reference-image-1-into-an-anime-character-9.md) · `Seedream 5.0 Pro`
- [Turn the man from reference image 1 into an anime character.](prompts/image/turn-the-man-from-reference-image-1-into-an-anime-character-10.md) · `Seedream 5.0 Pro`
- [Turn the man from reference image 1 into an anime character.](prompts/image/turn-the-man-from-reference-image-1-into-an-anime-character-11.md) · `Seedream 5.0 Pro`
- [Turn the young man from reference image 1 into an anime character.](prompts/image/turn-the-young-man-from-reference-image-1-into-an-anime-character.md) · `Seedream 5.0 Pro`
- [Turn this real photo into a painterly realistic anime scene, Attack on Titan / Demon Slayer style, bold lineart, cel sha](prompts/image/turn-this-real-photo-into-a-painterly-realistic-anime-scene-attack-on.md) · `Nano Banana Pro`
- [Unai Simon sheet](prompts/image/unai-simon-sheet.md) · `Nano Banana Pro`
- [Using image 1 as the base composition and image 2 as the exact logo shape reference, redraw this editorial cartoon meme](prompts/image/using-image-1-as-the-base-composition-and-image-2-as-the-exact-logo-sh.md) · `Nano Banana Pro`
- [You are given two images batched together.](prompts/image/you-are-given-two-images-batched-together.md) · `GPT Image 2`

### Audio y voz (14)

- [Argentinos...](prompts/audio/argentinos.md) · `ElevenLabs Multilingual v2`
- [Argentinos...](prompts/audio/argentinos-2.md) · `ElevenLabs Multilingual v2`
- [Cinematic black hole: short reverse suction riser into a massive deep sub-bass boom with cosmic gravitational rumble](prompts/audio/cinematic-black-hole-short-reverse-suction-riser-into-a-massive-deep-s.md) · `ElevenLabs SFX v2`
- [Dark ethereal cinematic ambient underscore, cosmic mystery emerging from the void, slowly evolving deep synth drone pads](prompts/audio/dark-ethereal-cinematic-ambient-underscore-cosmic-mystery-emerging-fro.md) · `Stable Audio 2.5`
- [Dark smoke burst: airy billowing gust of smoke, soft wispy swirling whoosh](prompts/audio/dark-smoke-burst-airy-billowing-gust-of-smoke-soft-wispy-swirling-whoo.md) · `ElevenLabs SFX v2`
- [deep rising energy charge, humming power building up to a peak, sci-fi, cinematic](prompts/audio/deep-rising-energy-charge-humming-power-building-up-to-a-peak-sci-fi-c.md) · `ElevenLabs Sound Generation`
- [Epic cinematic orchestral battle music, trailer style.](prompts/audio/epic-cinematic-orchestral-battle-music-trailer-style.md) · `Sonilo (texto a musica)`
- [huge football stadium crowd roar and euphoric cheer, goal celebration](prompts/audio/huge-football-stadium-crowd-roar-and-euphoric-cheer-goal-celebration.md) · `ElevenLabs Sound Generation`
- [huge passionate Argentine football stadium crowd, bombo drum, singing and chanting rhythmically, roaring](prompts/audio/huge-passionate-argentine-football-stadium-crowd-bombo-drum-singing-an.md) · `ElevenLabs Sound Generation`
- [Liquid water morph: sudden watery splash whoosh with bubbling flowing water surge](prompts/audio/liquid-water-morph-sudden-watery-splash-whoosh-with-bubbling-flowing-w.md) · `ElevenLabs SFX v2`
- [locucion con ElevenLabs y clonado de voz](workflows/voz_elevenlabs_tts.json) · `ElevenLabs Multilingual v2`
- [Magical instant freeze: fast crystalline ice crackling and glassy frost spreading, shimmering cold tail](prompts/audio/magical-instant-freeze-fast-crystalline-ice-crackling-and-glassy-frost.md) · `ElevenLabs SFX v2`
- [massive energy explosion impact boom with shockwave](prompts/audio/massive-energy-explosion-impact-boom-with-shockwave.md) · `ElevenLabs Sound Generation`
- [Sudden fire ignition burst: a deep fwoom of flames igniting instantly, with a short crackling embers tail](prompts/audio/sudden-fire-ignition-burst-a-deep-fwoom-of-flames-igniting-instantly-w.md) · `ElevenLabs SFX v2`

### Workflows de ComfyUI (3)

- [locucion con ElevenLabs y clonado de voz](workflows/voz_elevenlabs_tts.json) · `ElevenLabs Multilingual v2`
- [frame cero con GPT Image 2](workflows/NN-E01-FrameCero-gptimage2.json) · `GPT Image 2`
- [Seedance reference-to-video multishot](workflows/NN-E01-Seedance-R2V-multishot.json) · `Seedance 2.0`

## Licencia

[CC BY 4.0](LICENSE). Usalos, modificalos y vendé lo que hagas con ellos. Lo único
que pedimos es atribución a NoMa Studio AI.

---

Hecho por [NoMa Studio AI](https://nomastudio.ai) · [@nomastudioai](https://instagram.com/nomastudioai) · [@nomaaistudio en X](https://x.com/nomaaistudio) · [@nicolasmariar](https://instagram.com/nicolasmariar)