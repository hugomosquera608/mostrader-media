// Exporta el avatar con una expresión a SVG para los carruseles. Uso: node avatar.js skeptic av_skeptic.svg
const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
(async()=>{const [e,out]=process.argv.slice(2);const b=await chromium.launch();const p=await b.newPage();
await p.goto('file://'+path.resolve(__dirname,'../reel/template.html'));
fs.writeFileSync(out,await p.evaluate(x=>avatarSVG(x,0,0),e));await b.close()})();
