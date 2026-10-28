import os,re
src=open('../carr/build.py').read(); CSS=re.search(r'CSS = """(.*?)"""',src,re.S).group(1)
CSS+=""".bar{display:flex;align-items:center;gap:24px;margin:26px 0}.bar .n{font:700 38px M;width:240px}.bar .bb{height:72px;border:4px solid #141414}.bar .v{font:700 50px M;color:#E2723D}
.big{font:700 150px/1 M;color:#E2723D;letter-spacing:-8px;white-space:nowrap}
li{margin:0 0 26px 0}"""
N=8
WK=open('av_wink.svg').read(); SE=open('av_serious.svg').read()
def page(cls,i,body,extra='',src='Fuente: The Economist'):
    return f'<section class="s {cls}">{extra}<div class="top"><span>@mostrader_</span><span>{i}/{N}</span></div>{body}<div class="foot"><span>{src}</span><span>@mostrader_</span></div></section>'
S=[]
S.append(page('dark',1,f"""<div style="margin-top:40px"><div class="kick">IA · Mercados</div>
<span class="strip w">El nuevo</span><br><span class="strip o">petróleo</span><br><span class="strip w">son los chips</span>
<div class="p" style="color:#F4EDE6;max-width:620px">Por qué el Nasdaq subió solo hoy.</div></div>
<div class="card" style="position:absolute;left:110px;bottom:120px;width:560px;box-shadow:16px 16px 0 #E2723D;padding:8px"><img src="econ_ai.png"></div>
<div style="position:absolute;right:60px;bottom:110px;width:330px;height:330px;border-radius:50%;background:#E2723D">{WK}</div>""",src='Ilustración: The Economist'))
S.append(page('light',2,"""<div style="margin-top:80px"><div class="kick">Hoy, 27 de octubre</div>
<div class="h">Subió la tecnología. <em>El resto, casi nada.</em></div><div style="margin-top:50px">
<div class="bar"><div class="n">Nasdaq</div><div class="bb" style="width:470px;background:#E2723D"></div><div class="v">+1,18%</div></div>
<div class="bar"><div class="n">S&amp;P 500</div><div class="bb" style="width:240px;background:#141414"></div><div class="v">+0,60%</div></div>
<div class="bar"><div class="n">Dow</div><div class="bb" style="width:12px;background:#999"></div><div class="v">+0,03%</div></div></div>
<div class="p">Lo empujó la demanda de IA, según el resumen de MRKT.</div></div>""",src='Fuente: MRKT'))
S.append(page('dark',3,"""<div style="margin-top:90px"><div class="kick">La demanda</div>
<div class="big">$360.000M</div><div style="font:600 36px M;margin:20px 0 60px">invertidos en cómputo de IA el año pasado</div>
<div class="h">Un 50% más <em>que en cobre.</em></div></div>""",src='Fuente: BCG vía The Economist'))
S.append(page('light',4,"""<div style="margin-top:90px"><div class="kick">El tamaño en 2030</div>
<div class="big">$2,3 bill.</div><div style="font:600 36px M;margin:20px 0 60px">de dólares en operaciones de cómputo, según BCG</div>
<div class="h">Lo mismo que hoy mueve <em>el comercio de crudo.</em></div></div>""",src='Fuente: BCG vía The Economist'))
S.append(page('dark',5,"""<div style="margin-top:90px"><div class="kick">El problema</div>
<div class="h" style="margin-bottom:40px">Un mercado gigante <em>y todavía informal.</em></div>""" + ''.join(f'<div class="stat"><div class="v" style="min-width:120px">{v}</div><div class="t">{t}</div></div>' for v,t in [('01','Se negocia con intermediarios, a veces por WhatsApp o Telegram.'),('02','Casi todo va en contratos de varios años.'),('03','Los bonos de CoreWeave muestran cuánto riesgo ve el mercado.')]) + '</div>'))
S.append(page('light',6,"""<div style="margin-top:90px"><div class="kick">Lo que viene</div>
<div class="h" style="margin-bottom:40px">Futuros <em>de cómputo.</em></div>""" + ''.join(f'<div class="stat"><div class="v" style="min-width:250px;font-size:46px;white-space:nowrap">{v}</div><div class="t">{t}</div></div>' for v,t in [('CME · ICE','Quieren lanzar futuros de cómputo. Esperan la aprobación del regulador.'),('OTC','Ya hay swaps a medida que fijan el precio por servidor y hora.'),('Bermuda','Una bolsa ya ofrece futuros ligados a chips en EE. UU.')]) + '</div>'))
S.append(page('dark',7,"""<div style="margin-top:80px"><div class="kick">Resumen para traders</div><span class="strip o">Lo que importa</span>
<ol style="margin:50px 0 0 46px;font:600 38px/1.35 P"><li>La demanda de IA está moviendo el <b style="color:#E2723D">NQ</b>.</li><li>La subida está concentrada en chips: más frágil.</li><li>El cómputo se negocia como una materia prima nueva.</li><li>Si salen los futuros, será otro mercado para operar.</li></ol></div>""",src='Fuente: The Economist · MRKT'))
S.append(page('orange',8,f"""<div style="margin-top:110px;position:relative;z-index:2"><span class="strip b">Guarda</span><br><span class="strip b">este post</span>
<div class="p" style="max-width:600px;font-weight:600">Mañana a las 6:00 pm te cuento qué hizo la Fed y cómo se movió el Nasdaq.</div></div>
<div style="position:absolute;right:30px;bottom:120px;width:480px;height:480px;border-radius:50%;background:#141414;padding:14px">{WK}</div>""",src='@mostrader_'))
os.makedirs('out',exist_ok=True)
for i,s in enumerate(S,1): open(f'out/s{i}.html','w').write(f'<!DOCTYPE html><html><head><meta charset="utf-8"><base href="file://{os.getcwd()}/"><style>{CSS}</style></head><body>{s}</body></html>')
