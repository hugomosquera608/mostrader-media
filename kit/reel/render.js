// node render.js spec.json out.mp4 [audio]
const { chromium } = require('playwright');
const { spawn } = require('child_process');
const fs = require('fs'); const path = require('path');
const [specPath, out, audio] = process.argv.slice(2);
const spec = JSON.parse(fs.readFileSync(specPath, 'utf8'));
const FPS = spec.fps || 30;

// subtitle chunks (2-4 words) from timed lines; speech ranges for the mouth
function chunk(line) {
  const words = line.text.split(/\s+/); const groups = []; let g = [];
  for (const w of words) { g.push(w); if (g.length >= 3 || (/[.,:?!]$/.test(w) && g.length >= 2)) { groups.push(g); g = []; } }
  if (g.length) { if (g.length === 1 && groups.length) groups[groups.length - 1].push(...g); else groups.push(g); }
  const total = groups.reduce((a, x) => a + x.join(' ').length, 0); let t = line.start; const d = line.end - line.start;
  return groups.map(x => { const txt = x.join(' '); const len = d * txt.length / total;
    const s = { start: t, end: t + len, text: txt, hl: (line.hl || []).filter(h => txt.includes(h)) }; t += len; return s; });
}
spec.subs = spec.lines.flatMap(chunk);
spec.speech = spec.lines.map(l => [l.start, l.end - 0.05]);

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
  await page.goto('file://' + path.resolve(__dirname, 'template.html'));
  await page.evaluate(async s => await window.setup(s), spec);
  await page.evaluate(() => document.fonts.ready);
  const args = ['-y', '-f', 'image2pipe', '-framerate', String(FPS), '-i', '-'];
  if (audio) args.push('-i', audio);
  args.push('-c:v', 'libx264', '-preset', 'veryfast', '-crf', '20', '-pix_fmt', 'yuv420p');
  if (audio) args.push('-c:a', 'aac', '-b:a', '192k', '-shortest');
  args.push(out);
  const ff = spawn('ffmpeg', args, { stdio: ['pipe', 'inherit', 'inherit'] });
  const N = Math.ceil(spec.duration * FPS);
  for (let i = 0; i < N; i++) {
    await page.evaluate(t => window.seek(t), i / FPS);
    const buf = await page.screenshot({ type: 'jpeg', quality: 92 });
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
    if (i % 150 === 0) process.stderr.write(`frame ${i}/${N}\n`);
  }
  ff.stdin.end(); await new Promise(r => ff.on('close', r)); await browser.close();
})();
