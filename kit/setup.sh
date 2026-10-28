#!/bin/bash
# Prepara el kit Mostrader en una sesión nueva. Uso: bash setup.sh (dentro de la carpeta del kit)
set -e; cd "$(dirname "$0")"
pip install --break-system-packages -q edge-tts numpy certifi
for d in reel carr; do (cd $d && npm init -y >/dev/null && npm i -s @fontsource/poppins @fontsource/space-mono @fontsource/instrument-serif >/dev/null); mkdir -p $d/fonts
  for f in poppins/files/poppins-latin-{500,600,700,800}-normal space-mono/files/space-mono-latin{,-ext}-{400,700}-normal instrument-serif/files/instrument-serif-latin{,-ext}-400-italic; do cp $d/node_modules/@fontsource/$f.woff2 $d/fonts/; done; done
(cd carr && for e in skeptic wink smile surprised serious; do node avatar.js $e av_$e.svg; done)
chmod +x reel/make_reel.sh; echo "Kit listo"
