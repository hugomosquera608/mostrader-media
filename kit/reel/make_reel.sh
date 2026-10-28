#!/bin/bash
# Uso: ./make_reel.sh scripts/FECHA.json scripts/FECHA_tts.txt salida.mp4
# script.json = escenas/subtitulos (con números en dígitos); tts.txt = una línea hablada por subtítulo (números en palabras)
set -e; S=$1; T=$2; OUT=$3; W=$(mktemp -d)
VOICE=${VOICE:-en-US-AndrewMultilingualNeural}; RATE=${RATE:-+32%}; PITCH=${PITCH:-+0Hz}   # voz "narrador 4 Andrew" rápida, aprobada por Hugo
i=0; while IFS= read -r line; do [ -z "$line" ] && continue; i=$((i+1)); n=$(printf %02d $i)
  for k in 1 2 3; do python3 tts2.py $VOICE "$line" $W/$n.mp3 $RATE $PITCH 2>/dev/null && break; sleep 2; done; [ -s $W/$n.mp3 ] || { echo "TTS falló: $line"; exit 1; }; done < "$T"
python3 - "$W" > $W/durs.json <<'PY'
import sys,glob,subprocess,json
fs=sorted(glob.glob(sys.argv[1]+'/[0-9]*.mp3'))
print(json.dumps([round(float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f]))-0.05,3) for f in fs]))
PY
python3 build_spec.py "$S" $W/spec.json $W/durs.json
python3 - "$W" <<'PY'
import sys,json,glob,subprocess
w=sys.argv[1];sp=json.load(open(w+'/spec.json'));fs=sorted(glob.glob(w+'/[0-9]*.mp3'))
inp=[];fl=[]
for k,(f,l) in enumerate(zip(fs,sp['lines'])):
  inp+=['-i',f];ms=int(l['start']*1000);fl.append(f'[{k}:a]adelay={ms}|{ms}[a{k}]')
mix=''.join(f'[a{k}]' for k in range(len(fs)))+f'amix=inputs={len(fs)}:normalize=0,apad=whole_dur={sp["duration"]},acompressor=threshold=-18dB:ratio=3,equalizer=f=3000:t=q:w=1:g=3,loudnorm=I=-14[o]'
subprocess.check_call(['ffmpeg','-y','-v','error',*inp,'-filter_complex',';'.join(fl)+';'+mix,'-map','[o]','-ar','44100',w+'/track.wav'])
PY
python3 envelope.py $W/spec.json $W/track.wav
node render.js $W/spec.json "$OUT" $W/track.wav
echo "OK -> $OUT"
