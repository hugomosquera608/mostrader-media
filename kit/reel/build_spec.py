"""Build a timed spec from a script. Usage: python3 build_spec.py script.json spec.json [durations.json]
durations.json (optional): list of seconds per line, from the real voiceover."""
import json, sys
src = json.load(open(sys.argv[1]))
durs = json.load(open(sys.argv[3])) if len(sys.argv) > 3 else None
WPS = src.get('wps', 2.75); GAP = 0.18; WIPE = 0.7
t = 0.6; lines = []; scenes = []; wipes = []; k = 0
for si, sc in enumerate(src['scenes']):
    if si > 0:
        wipes.append(t + WIPE / 2); t += WIPE
    start = t
    for ln in sc['lines']:
        d = durs[k] if durs else max(1.1, len(ln['text'].split()) / WPS)
        lines.append({'start': round(t, 3), 'end': round(t + d, 3), 'text': ln['text'], 'hl': ln.get('hl', [])})
        if 'block_at' in ln:  # mark when a block should appear (relative)
            pass
        t += d + GAP; k += 1
    end = t + 0.3
    s = {k2: v for k2, v in sc.items() if k2 != 'lines'}
    s['start'] = round(start - (WIPE / 2 if si > 0 else 0.6), 3); s['end'] = round(end + (WIPE / 2), 3)
    scenes.append(s); t = end
for i in range(len(scenes) - 1):
    scenes[i]['end'] = scenes[i + 1]['start']
dur = round(t + 0.8, 2); scenes[-1]['end'] = dur
json.dump({'date': src['date'], 'duration': dur, 'fps': 30, 'scenes': scenes, 'lines': lines, 'wipes': wipes},
          open(sys.argv[2], 'w'), ensure_ascii=False, indent=1)
print('duration', dur, 'lines', len(lines))
