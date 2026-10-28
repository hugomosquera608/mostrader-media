"""Add a mouth-opening envelope (0..1 per frame) from the voice track to a spec. Usage: envelope.py spec.json track.wav"""
import sys,json,subprocess,numpy as np
spec=json.load(open(sys.argv[1]));fps=spec.get('fps',30)
raw=subprocess.check_output(['ffmpeg','-v','error','-i',sys.argv[2],'-ac','1','-ar','16000','-f','s16le','-'])
a=np.frombuffer(raw,np.int16).astype(float)/32768;hop=16000//fps
n=int(spec['duration']*fps)+1;env=[]
for i in range(n):
  seg=a[i*hop:(i+1)*hop];env.append(float(np.sqrt((seg**2).mean())) if len(seg) else 0.0)
env=np.array(env);ref=np.percentile(env[env>0.005],90) if (env>0.005).any() else 1
env=np.clip(env/ref,0,1)
sm=np.copy(env)
for i in range(1,len(sm)): sm[i]=max(env[i],sm[i-1]*0.55)  # fast attack, quick release
spec['env']=[round(x,3) for x in sm];json.dump(spec,open(sys.argv[1],'w'),ensure_ascii=False)
print('frames',len(sm),'mean',round(float(sm.mean()),3))
