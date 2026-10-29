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
F.append(f"""<div class="s"><div class="tag">JUEVES 29 OCT · ANTES DE ABRIR</div><div class="h">Google <em>-10%</em>. Microsoft <em>+4%.</em></div><div class="p">Mismo tema, la IA. Dos reacciones opuestas.</div>
<div class="av" style="left:260px;top:900px">{A['surprised']}</div></div>""")
F.append("""<div class="s dark" style="padding-top:260px"><div class="tag">PREMERCADO</div><div class="h" style="font-size:80px">El mercado <em>premia y castiga.</em></div>
<div style="margin-top:50px">
<div class="bar"><div class="n">Alphabet</div><div class="b" style="width:520px;background:#F4EDE6"></div><div class="v">-10%</div></div>
<div class="bar"><div class="n">Nasdaq fut.</div><div class="b" style="width:52px;background:#888"></div><div class="v">-1%</div></div>
<div class="bar"><div class="n">Microsoft</div><div class="b" style="width:208px;background:#E2723D"></div><div class="v">+4%</div></div></div>
<div style="font:600 40px/1.35 P;margin-top:50px">Google ganó 2,12 por acción y esperaban casi 3. Su flujo de caja libre salió negativo.</div>
<div style="font:400 22px M;opacity:.6;margin-top:20px">Fuente: CNBC, IC Markets, Reuters</div></div>""")
F.append("""<div class="s"><div class="tag">HOY · 8:30 AM</div><div class="h">Salen <em>PIB y PCE.</em></div><div style="margin-top:60px">
<div class="row"><b>3,2%</b><span>PIB del 3T, esperado (anualizado)</span></div>
<div class="row"><b>3,1%</b><span>PCE núcleo de septiembre, esperado (anual)</span></div>
<div class="row"><b>Tarde</b><span>Después del cierre reporta Amazon</span></div></div></div>""")
F.append("""<div class="s dark"><div class="tag">MI LECTURA · SEMÁFORO</div><div class="h" style="font-size:88px">Economía fuerte. <em>Inflación, el problema.</em></div><div style="margin-top:40px">
<div class="row" style="border-color:#4CAF50"><b style="color:#4CAF50">197K</b><span>Solicitudes de desempleo. Bajo 220K = muy sano</span></div>
<div class="row" style="border-color:#E2723D"><b>55,3</b><span>ISM nuevos pedidos. Sobre 50 = expansión</span></div>
<div class="row" style="border-color:#E5484D"><b style="color:#E5484D">3,7%</b><span>Inflación. Sobre 3% y subiendo = presión para el NQ</span></div></div>
<div style="font:400 22px M;opacity:.6;margin-top:30px">Mi análisis del 21 oct. Datos de mis indicadores adelantados.</div></div>""")
F.append("""<div class="s org"><div class="tag">TU TURNO</div><div class="h" style="font-size:96px">NQ: ¿llega al objetivo o pierde el apoyo?</div>
<div style="font:600 40px/1.35 P;margin-top:40px">Mis niveles de ayer: objetivo 30.250 · apoyo 29.600.<br>Los reviso con la apertura.</div><div style="position:absolute;left:90px;right:90px;top:1180px;background:#141414;color:#F4EDE6;padding:44px 50px;border-radius:24px;font:700 54px/1.25 P">▲ 30.250 &nbsp;o&nbsp; ▼ 29.600<div style="font:500 36px P;margin-top:14px;color:#E2723D">Respóndeme esta historia con tu número.</div></div>
<div class="foot" style="bottom:300px">Contenido educativo, no es recomendación financiera.</div></div>""")
os.makedirs('out',exist_ok=True)
for i,f in enumerate(F,1): open(f'out/h{i}.html','w').write(f'<!DOCTYPE html><html><head><meta charset="utf-8"><base href="file://{os.getcwd()}/"><style>{CSS}</style></head><body>{f}</body></html>')
