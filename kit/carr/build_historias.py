import os
A={e:open(f'av_{e}.svg').read() for e in ['surprised','serious','wink','skeptic']}
CSS="""@font-face{font-family:P;font-weight:600;src:url(fonts/poppins-latin-600-normal.woff2)}
@font-face{font-family:P;font-weight:800;src:url(fonts/poppins-latin-800-normal.woff2)}
@font-face{font-family:P;font-weight:500;src:url(fonts/poppins-latin-500-normal.woff2)}
@font-face{font-family:M;font-weight:700;src:url(fonts/space-mono-latin-700-normal.woff2)}
@font-face{font-family:M;font-weight:400;src:url(fonts/space-mono-latin-400-normal.woff2)}
@font-face{font-family:S;src:url(fonts/instrument-serif-latin-400-italic.woff2)}
*{margin:0;padding:0;box-sizing:border-box}body{width:1080px;height:1920px;overflow:hidden;font-family:P}
.s{position:relative;width:1080px;height:1920px;padding:300px 90px 0;background:#F4EDE6;color:#141414;background-image:linear-gradient(rgba(0,0,0,.035) 2px,transparent 2px),linear-gradient(90deg,rgba(0,0,0,.035) 2px,transparent 2px);background-size:90px 90px}
.dark{background:#111;color:#F4EDE6;background-image:none}.org{background:#E2723D;background-image:none}
.tag{font:700 30px M;letter-spacing:3px;color:#E2723D;margin-bottom:28px}.org .tag{color:#141414}
.h{font:800 104px/1.02 P;letter-spacing:-3px}.h em{font:400 120px S;color:#E2723D;letter-spacing:-1px}
.p{font:500 44px/1.35 P;margin-top:36px}
.av{position:absolute;width:560px;height:560px;border-radius:50%}
.bar{display:flex;align-items:center;gap:24px;margin:22px 0}.bar .n{font:700 40px M;width:250px}.bar .b{height:70px;border:4px solid #141414}.bar .v{font:700 52px M;color:#E2723D}
.row{border-top:5px solid #E2723D;padding:30px 0}.row b{font:700 84px M;color:#E2723D;letter-spacing:-3px;display:block}.row span{font:600 40px/1.3 P}
.poll{position:absolute;left:140px;right:140px;top:1150px;height:300px;border:5px dashed #141414;border-radius:30px;display:flex;align-items:center;justify-content:center;font:700 34px M;opacity:.55;text-align:center}
.foot{position:absolute;left:90px;bottom:330px;font:700 30px M;opacity:.7}"""
F=[]
F.append(f"""<div class="s"><div class="tag">MARTES 27 OCT · CIERRE</div><div class="h">El Nasdaq subió <em>1,18%</em> hoy.</div><div class="p">Pero hay un detalle que no me gusta.</div>
<div class="av" style="left:260px;top:900px">{A['surprised']}</div></div>""")
F.append("""<div class="s dark" style="padding-top:260px"><div class="tag">EL DETALLE · MRKT + THE ECONOMIST</div><div class="h" style="font-size:80px">Subió la tecnología. <em>El resto, casi nada.</em></div>
<div style="margin-top:40px">
<div class="bar"><div class="n">Nasdaq</div><div class="b" style="width:520px;background:#E2723D"></div><div class="v">+1,18%</div></div>
<div class="bar"><div class="n">S&amp;P 500</div><div class="b" style="width:265px;background:#F4EDE6"></div><div class="v">+0,60%</div></div>
<div class="bar"><div class="n">Dow</div><div class="b" style="width:14px;background:#888"></div><div class="v">+0,03%</div></div></div>
<div style="margin-top:30px;background:#fff;border:5px solid #E2723D;padding:10px"><img src="econ_ai.png" style="display:block;width:100%"></div>
<div style="font:600 36px/1.3 P;margin-top:26px">The Economist: el cómputo para IA es <b style="color:#E2723D">"el nuevo petróleo"</b>.</div>
<div style="font:400 22px M;opacity:.6;margin-top:10px">Ilustración: The Economist</div></div>""")
F.append("""<div class="s"><div class="tag">MAÑANA · MIÉRCOLES 28</div><div class="h">Habla <em>la Fed.</em></div><div style="margin-top:60px">
<div class="row"><b>2:00 pm</b><span>Decisión de tasas</span></div>
<div class="row"><b>4,99%</b><span>Bono a 10 años, pegado al 5%</span></div>
<div class="row"><b>91,7</b><span>Confianza del consumidor. Esperaban 81</span></div></div></div>""")
F.append(f"""<div class="s org"><div class="tag">TU TURNO · NIVELES MRKT</div><div class="h" style="font-size:96px">El NQ está en 29.811. ¿A dónde va después de la Fed?</div>
<div style="font:600 40px/1.35 P;margin-top:40px">MRKT: sesgo alcista, con riesgo de reversión.<br>Objetivo 30.300 · soporte 29.300</div><div style="position:absolute;left:90px;right:90px;top:1180px;background:#141414;color:#F4EDE6;padding:44px 50px;border-radius:24px;font:700 54px/1.25 P">▲ 30.300 &nbsp;o&nbsp; ▼ 29.300<div style="font:500 36px P;margin-top:14px;color:#E2723D">Respóndeme esta historia con tu número.</div></div></div>""")
F.append(f"""<div class="s dark"><div class="tag">MAÑANA 6:00 PM</div><div class="h">Te cuento qué pasó <em>y qué hago yo.</em></div><div class="p">Activa las notificaciones para no perderte el reel.</div>
<div class="av" style="left:260px;top:900px;background:#E2723D">{A['wink']}</div></div>""")
os.makedirs('out',exist_ok=True)
for i,f in enumerate(F,1): open(f'out/h{i}.html','w').write(f'<!DOCTYPE html><html><head><meta charset="utf-8"><base href="file://{os.getcwd()}/"><style>{CSS}</style></head><body>{f}</body></html>')
