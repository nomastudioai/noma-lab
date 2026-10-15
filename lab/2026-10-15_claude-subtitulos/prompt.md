# Prompt: subtitulador de inglés a español con Claude

Copialo entero, completá el bloque DATOS y mandalo en claude.ai junto con el video. Más detalles en el [README](README.md).

```text
Actúa como subtitulador profesional de inglés a español para televisión y redes. Necesito los subtítulos en español de un video en inglés, en un archivo .srt.

DATOS (completa antes de enviar)
- Video: [pega aquí la ruta del archivo]
- Nombres y términos que aparecen en el video (opcional): [personas, marcas, lugares, separados por coma]
- Variante de español: neutro latinoamericano [cambiar a "chileno coloquial" si corresponde]
- Quemar los subtítulos en el video: no [cambiar a "sí" si necesitas el video con los subtítulos incrustados]

REGLAS DE TRABAJO
- No puedes escuchar audio directamente: transcribe con tu entorno de ejecución de código, como se indica abajo.
- Si falla una instalación o hay un choque de versiones de librerías, corrígelo tú y sigue. Si Hugging Face responde con límite de descargas (error 429), espera un minuto y reintenta.
- Detente solo si no encuentras el video o si la red bloquea un dominio. En ese caso dime exactamente qué pasó (incluido el dominio bloqueado) para reenviárselo al administrador.
- Nunca inventes ni reconstruyas la transcripción a partir del nombre del archivo o del contexto.

PASO 1 · Preparar el entorno
1. Instala con pip las versiones probadas: faster-whisper==1.2.1 av==18.1.0 ctranslate2==4.8.3
2. Define la variable de entorno HF_HUB_DISABLE_XET=1 y carga WhisperModel("small.en", device="cpu", compute_type="int8").
3. Trae el video de la ruta indicada a tu entorno (pide acceso a la carpeta si hace falta).

PASO 2 · Transcribir el inglés
- Transcribe el video completo con language="en", vad_filter=True y word_timestamps=True. Si te di nombres y términos, pásalos en el parámetro hotwords.
- Si el entorno corta procesos largos, transcribe por tramos y une los resultados corrigiendo los tiempos.
- Elimina frases que Whisper suele inventar en silencios o música (por ejemplo "Thank you for watching").
- Corrige solo errores de reconocimiento evidentes por el contexto. Nombres propios y palabras dudosas no los cambies: anótalos para el reporte.

PASO 3 · Subtítulos en inglés
Con los tiempos por palabra, arma los subtítulos: cada uno entre 1 y 7 segundos en pantalla, cortados en fin de frase o en pausas naturales. Guárdalo con el nombre del video terminado en _EN.srt.

PASO 4 · Traducción y adaptación
- Traduce tú mismo. No uses librerías ni servicios de traducción automática.
- Si el video es largo, trabaja por bloques y al final verifica que no falte ningún subtítulo.
- Conserva la numeración y los tiempos del .srt en inglés. Si un subtítulo queda demasiado largo, puedes dividirlo o fusionarlo dentro de su tramo de tiempo original, sin solapamientos.
- Máximo 2 líneas por subtítulo y 42 caracteres por línea. Apunta a no más de 17 caracteres por segundo. Sintetiza sin perder sentido: subtitular no es traducir literal.
- Corta las líneas en puntos naturales (no separes artículo y sustantivo, ni verbo y pronombre).
- Puntuación española completa (¿? ¡!). Si hablan dos personas en un mismo subtítulo, cada línea empieza con guion "-".
- Mantén el registro del original (formal, coloquial, groserías) sin censurar ni suavizar.
- No traduzcas nombres propios, marcas ni nombres de programas. Títulos de obras: usa el título oficial en español solo si estás seguro; si no, deja el original.
- No conviertas unidades ni monedas. No agregues nada que no esté en el original. Lo que no se entienda va como [inaudible].

PASO 5 · Control de calidad
Valida el archivo en español con un script: formato SRT correcto, sin solapamientos, ninguna línea de más de 42 caracteres, ningún subtítulo de más de 2 líneas. Lista los que superen 17 caracteres por segundo, corrige lo que se pueda y vuelve a validar.

PASO 6 · Quemar los subtítulos (solo si en DATOS dice "sí")
1. Instala con pip imageio-ffmpeg==0.6.0 y usa su ffmpeg (imageio_ffmpeg.get_ffmpeg_exe()), que trae libass.
2. Copia el _ES.srt a un nombre simple sin espacios (subs.srt). Crea una carpeta fonts con DejaVuSans-Bold.ttf, que viene dentro de matplotlib en mpl-data/fonts/ttf (si no está matplotlib, instálalo con pip).
3. Lee el ancho (W) y el alto (H) del video y calcula: FontSize = el menor entre 16 y 12 × W / H. Outline = FontSize / 10. MarginV = 55 si el video es vertical (así el texto queda sobre los botones de las apps) y 14 en cualquier otro caso.
4. Ejecuta ffmpeg con estos ajustes:
-vf "subtitles=subs.srt:fontsdir=fonts:force_style='FontName=DejaVu Sans,FontSize=[FontSize],PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,BorderStyle=1,Outline=[Outline],Shadow=0,MarginV=[MarginV]'" -c:v libx264 -preset veryfast -crf 20 -pix_fmt yuv420p -c:a copy -movflags +faststart
Si la copia del audio falla, usa -c:a aac -b:a 192k.
5. Extrae un fotograma donde haya subtítulo y muéstramelo para revisar.

ENTREGA
1. Los archivos para descargar: el del video terminado en _ES.srt (UTF-8), el _EN.srt de referencia y, si quemaste subtítulos, el video terminado en _ES_subtitulado.mp4. Si el video es demasiado pesado para descargarlo desde el chat, guárdalo en la carpeta del video original.
2. Un reporte breve: duración del video, cantidad de subtítulos, nombres y términos dudosos para que los revise una persona, subtítulos que sigan por encima de 17 caracteres por segundo y cuánto tardó cada paso.
```
