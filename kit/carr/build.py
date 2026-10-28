import os
SK = open('av_skeptic.svg').read(); WK = open('av_wink.svg').read()
N = 9
CSS = """
@font-face{font-family:P;font-weight:500;src:url(fonts/poppins-latin-500-normal.woff2)}
@font-face{font-family:P;font-weight:600;src:url(fonts/poppins-latin-600-normal.woff2)}
@font-face{font-family:P;font-weight:700;src:url(fonts/poppins-latin-700-normal.woff2)}
@font-face{font-family:P;font-weight:800;src:url(fonts/poppins-latin-800-normal.woff2)}
@font-face{font-family:M;font-weight:400;src:url(fonts/space-mono-latin-400-normal.woff2)}
@font-face{font-family:M;font-weight:700;src:url(fonts/space-mono-latin-700-normal.woff2)}
@font-face{font-family:S;src:url(fonts/instrument-serif-latin-400-italic.woff2),url(fonts/instrument-serif-latin-ext-400-italic.woff2)}
*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1350px;overflow:hidden;font-family:P}
.s{position:relative;width:1080px;height:1350px;overflow:hidden;padding:110px 110px 0}
.light{background:#F4EDE6;color:#141414;background-image:linear-gradient(rgba(0,0,0,.035) 2px,transparent 2px),linear-gradient(90deg,rgba(0,0,0,.035) 2px,transparent 2px);background-size:90px 90px}
.dark{background:#111;color:#F4EDE6}
.orange{background:#E2723D;color:#141414}
.top{position:absolute;left:110px;right:110px;top:56px;display:flex;justify-content:space-between;font:700 26px M;letter-spacing:1px}
.foot{position:absolute;left:110px;right:110px;bottom:52px;display:flex;justify-content:space-between;font:400 22px M;opacity:.75}
.kick{font:700 28px M;letter-spacing:3px;color:#E2723D;text-transform:uppercase;margin-bottom:26px}
.strip{display:inline-block;font:800 92px/1.02 P;text-transform:uppercase;letter-spacing:-2px;padding:6px 18px 2px;margin:0 0 10px -18px}
.w{background:#F4EDE6;color:#141414}.b{background:#141414;color:#F4EDE6}.o{background:#E2723D;color:#141414}
.h{font:800 74px/1.05 P;letter-spacing:-2px;text-transform:uppercase}
.h em{font:400 84px S;text-transform:none;letter-spacing:-1px;color:#E2723D}
.p{font:500 38px/1.35 P;margin-top:34px}
.stat{display:flex;align-items:baseline;gap:34px;border-top:4px solid #E2723D;padding:28px 0 26px}
.stat .v{font:700 84px M;color:#E2723D;letter-spacing:-3px;min-width:330px}
.stat .t{font:600 34px/1.25 P}.stat .src{display:block;font:400 22px M;opacity:.6;margin-top:6px}
.card{background:#fff;border:5px solid #141414;box-shadow:16px 16px 0 #141414;padding:14px}
.card img{display:block;width:100%}
.flag{position:absolute;left:0;right:0;top:0;height:420px;opacity:.16;background:repeating-linear-gradient(180deg,#E2723D 0 32px,transparent 32px 64px)}
"""
def page(cls, i, body, extra=''):
    return f"""<section class="s {cls}">{extra}<div class="top"><span>@mostrader_</span><span>{i}/{N}</span></div>{body}
<div class="foot"><span>Fuente: The Economist</span><span>@mostrader_</span></div></section>"""
def stats(rows):
    return ''.join(f'<div class="stat"><div class="v">{v}</div><div class="t">{t}<span class="src">{s}</span></div></div>' for v,t,s in rows)
S = []
S.append(page('dark', 1, f"""
<div style="position:relative;z-index:2;margin-top:70px">
<div class="kick">Economía · Estados Unidos</div>
<span class="strip w">¿Quién gana</span><br><span class="strip w">con la</span><br><span class="strip o">Trumponomics?</span>
<div class="p" style="max-width:560px;color:#F4EDE6">Lo que dicen los datos, por nivel de ingreso.</div></div>
<div style="position:absolute;right:-40px;bottom:120px;width:560px;height:560px">{SK}</div>
<div style="position:absolute;left:110px;bottom:150px;font:700 30px M;color:#E2723D">DESLIZA →</div>""", '<div class="flag"></div>'))
S.append(page('light', 2, """
<div style="margin-top:120px"><div class="kick">El contexto</div>
<div style="font:700 260px/1 M;color:#E2723D;letter-spacing:-12px">~3%</div>
<div style="font:600 36px M;margin:10px 0 50px">crecimiento previsto · 3er trimestre</div>
<div class="h">La economía crece. <em>Pero no para todos igual.</em></div>
<div class="p">La Casa Blanca dice que sus políticas suben los salarios. The Economist sumó lo que gana y pierde cada hogar.</div></div>"""))
S.append(page('dark', 3, """
<div style="margin-top:90px"><div class="kick">Lo que encarece la vida</div>
<div class="h" style="margin-bottom:46px">Aranceles <em>y petróleo.</em></div>""" + stats([
 ('+2%', 'Precios de bienes por los aranceles', 'Fed de Nueva York'),
 ('$1.100', 'Costo de los aranceles por hogar este año', 'Yale Budget Lab'),
 ('+$1.000', 'Gasto extra por hogar por la guerra en Irán', 'estimación a fin de año')]) + '</div>'))
S.append(page('light', 4, """
<div style="margin-top:90px"><div class="kick">Lo que ayuda… y lo que quita</div>
<div class="h" style="margin-bottom:46px">La reforma <em>fiscal.</em></div>""" + stats([
 ('+$340', 'Más en devoluciones de impuestos, en promedio', 'One Big Beautiful Bill'),
 ('$1.000', 'Para invertir por recién nacido: las “cuentas Trump”', ''),
 ('-5M', 'Personas que perdieron los cupones de alimentos', 'hasta ahora')]) + '</div>'))
S.append(page('light', 5, """
<div style="margin-top:40px"><div class="kick">El balance por ingreso</div>
<div class="h" style="font-size:66px">Ganan <em>los de arriba.</em></div>
<div style="display:flex;gap:40px;margin-top:40px;align-items:flex-start">
<div class="card" style="width:500px"><img src="chart1.png"></div>
<div style="flex:1;font:600 32px/1.3 P">
<div style="border-top:4px solid #E2723D;padding:18px 0"><b style="font:700 56px M;color:#E2723D">-3%</b><br>10% más pobre</div>
<div style="border-top:4px solid #E2723D;padding:18px 0"><b style="font:700 56px M;color:#E2723D">-$400</b><br>clase media</div>
<div style="border-top:4px solid #E2723D;padding:18px 0"><b style="font:700 56px M;color:#E2723D">+3%</b><br>10% más rico</div></div></div>
<div style="font:400 22px M;opacity:.6;margin-top:22px">Gráfico: The Economist · cambio estimado del ingreso 2026</div></div>"""))
S.append(page('dark', 6, """
<div style="margin-top:40px"><div class="kick">La bolsa, para pocos</div>
<div class="h" style="font-size:66px">+$17 billones… <em>¿para quién?</em></div>
<div style="display:flex;gap:40px;margin-top:40px;align-items:flex-start">
<div class="card" style="width:500px;box-shadow:16px 16px 0 #E2723D"><img src="chart2.png"></div>
<div style="flex:1;font:600 32px/1.3 P">
<div style="border-top:4px solid #E2723D;padding:18px 0"><b style="font:700 56px M;color:#E2723D">~90%</b><br>se lo llevó el 10% más rico</div>
<div style="border-top:4px solid #E2723D;padding:18px 0"><b style="font:700 56px M;color:#E2723D">0,6%</b><br>para la mitad más pobre</div></div></div>
<div style="font:400 22px M;opacity:.6;margin-top:22px">Gráfico: The Economist · datos de la Reserva Federal</div></div>"""))
S.append(page('light', 7, """
<div style="margin-top:90px"><div class="kick">Empleo y vivienda</div>
<div class="h" style="margin-bottom:46px">El bolsillo <em>no siente el boom.</em></div>""" + stats([
 ('&gt;7%', 'Tasas hipotecarias', ''),
 ('-0,7%', 'Salario real frente a hace un año', ''),
 ('-20.000', 'Empleos en fábricas desde enero de 2025', '')]) + '</div>'))
S.append(page('dark', 8, """
<div style="margin-top:80px"><div class="kick">Resumen · qué mirar en el mercado</div>
<span class="strip o">Lo que importa</span>
<div style="margin-top:40px;font:600 36px/1.35 P">
<div style="border-top:3px solid #333;padding:22px 0">📈 El rally depende de la <b style="color:#E2723D">IA</b> y de los que más tienen.</div>
<div style="border-top:3px solid #333;padding:22px 0">🛒 Si el consumo de la mitad de abajo se frena, lo sienten las <b style="color:#E2723D">acciones de consumo</b>.</div>
<div style="border-top:3px solid #333;padding:22px 0">⛽ Petróleo e hipotecas altas pesan en el bolsillo.</div>
<div style="border-top:3px solid #333;padding:22px 0">🗳️ <b style="color:#E2723D">3 de noviembre:</b> elecciones de medio mandato.</div></div></div>"""))
S.append(page('orange', 9, f"""
<div style="margin-top:110px;position:relative;z-index:2"><span class="strip b">Guarda</span><br><span class="strip b">este post</span>
<div class="p" style="max-width:560px;font-weight:600">Comenta <b style="background:#141414;color:#F4EDE6;padding:0 10px">MIDTERMS</b> y te mando cómo se movió el mercado después de las últimas elecciones.</div></div>
<div style="position:absolute;right:30px;bottom:120px;width:500px;height:500px;border-radius:50%;background:#141414;padding:14px">{WK}</div>"""))
os.makedirs('out', exist_ok=True)
for i, s in enumerate(S, 1):
    open(f'out/s{i}.html', 'w').write(f'<!DOCTYPE html><html><head><meta charset="utf-8"><base href="file://{os.getcwd()}/"><style>{CSS}</style></head><body>{s}</body></html>')
print(len(S))
