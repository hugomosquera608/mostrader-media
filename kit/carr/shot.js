const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350}});
for(let i=1;i<=9;i++){await p.goto('file://'+process.cwd()+`/out/s${i}.html`);await p.evaluate(()=>document.fonts.ready);await p.screenshot({path:`out/mostrader_trumponomics_${String(i).padStart(2,'0')}.png`});}await b.close()})()
