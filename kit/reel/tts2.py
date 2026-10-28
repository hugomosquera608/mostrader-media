import sys, os, asyncio, certifi
certifi.where = lambda: os.path.expanduser('~/.ccr/ca-bundle.crt')
import edge_tts
voice,text,out,rate,pitch=sys.argv[1:6]
asyncio.run(edge_tts.Communicate(text, voice, rate=rate, pitch=pitch).save(out))
