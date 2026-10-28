# Kit Mostrader (@mostrader_)
Motor de reels y carruseles. Ver plan.md para el calendario.
1. `bash setup.sh`
2. REEL: escribir `reel/scripts/FECHA.json` (mismo formato que ejemplo.json: escenas con title, blocks [cards|rows|bars|levels], expr, pose, lines con hl) y `FECHA_tts.txt` (una línea hablada por cada subtítulo, números en palabras). Luego `cd reel && ./make_reel.sh scripts/FECHA.json scripts/FECHA_tts.txt /mnt/user-data/outputs/reel_FECHA.mp4`
   - Expresiones del avatar: neutral, happy, smile, surprised, skeptic, worried, wink, serious, laugh. Movimiento solo respiración.
   - Voz: narrador 4 Andrew (en-US-AndrewMultilingualNeural) +32% +0Hz. Es multilingüe y a veces falla con alguna frase en español: make_reel.sh reintenta 3 veces; si aun así falla, reescribe un poco esa línea (por ejemplo "en cinco" -> "en el cinco").
3. CARRUSEL: copiar carr/build.py como plantilla (estilo noticiero, 1080x1350, avatar av_*.svg, se generan con setup; otras expresiones: node avatar.js EXPR archivo.svg), cambiar el contenido, `python3 build.py && node shot.js` (ajustar nombre/cantidad de slides en shot.js).
   - Gráficos e ilustraciones de The Economist permitidos con crédito "Fuente: The Economist". No usar fotos de personas reales.
Reglas: usar siempre las skills ig-* (ig-reel, ig-carousel, ig-caption, ig-story, ig-human). No cambiar el nombre del perfil.
