from pathlib import Path
import json, hashlib, wave
import numpy as np

root=Path(__file__).resolve().parents[1]
voice_path=root/'audio/voice.wav'
with wave.open(str(voice_path),'rb') as w:
    assert (w.getnchannels(),w.getsampwidth(),w.getframerate())==(1,2,48000)
    voice=np.frombuffer(w.readframes(w.getnframes()),dtype='<i2').astype(np.float32)/32768
sr=48000; n=len(voice); duration=n/sr
t=np.arange(n,dtype=np.float64)/sr
# Gentle original pad: slow warm triads with soft harmonic color, no samples.
chords=[(146.83,174.61,220.00),(130.81,164.81,196.00),(110.00,146.83,174.61),(130.81,164.81,196.00)]
bar=14.0
music=np.zeros(n,dtype=np.float64)
for k,start in enumerate(np.arange(0,duration,bar)):
    end=min(duration,start+bar)
    ix=(t>=start)&(t<end)
    local=t[ix]-start
    f=chords[k%len(chords)]
    env=np.minimum(1,local/2.5)*np.minimum(1,(end-start-local)/2.7)
    for j,hz in enumerate(f):
        phase=2*np.pi*hz*local
        music[ix]+=env*(0.52/(j+1))*np.sin(phase+0.13*j)
    # A quiet upper harmonic breath, smoothly swelled once per chord.
    music[ix]+=env*0.09*np.sin(2*np.pi*f[0]*2.01*local)
# Scale to gentle target RMS before fades.
rms=np.sqrt(np.mean(music**2)); music*=0.0045/max(rms,1e-9)
# Soft forest-night air: shaped noise, no discrete events or water splashes.
rng=np.random.default_rng(28)
noise=rng.standard_normal(n)
# Very low-level broadband room tone, slowly modulated to avoid a static hiss.
amb=noise*(0.78+0.22*np.sin(2*np.pi*0.13*t+0.7))
amb/=max(np.sqrt(np.mean(amb**2)),1e-9); amb*=0.00065
# Standard bed fades: music and ambience in over 2s, out over 5s.
env=np.ones(n,dtype=np.float64)
env[:2*sr]=np.linspace(0,1,2*sr,endpoint=True)
env[-5*sr:]=np.linspace(1,0,5*sr,endpoint=True)
mix=voice.astype(np.float64)+music*env+amb*env
assert np.max(np.abs(mix))<1

def save(path,data):
    pcm=np.clip(np.round(data*32767),-32768,32767).astype('<i2')
    with wave.open(str(path),'wb') as w:
        w.setnchannels(1);w.setsampwidth(2);w.setframerate(sr);w.writeframes(pcm.tobytes())
    return int(np.max(np.abs(pcm.astype(np.int32))))
with wave.open(str(voice_path),'rb') as w:
    voice_pcm=np.frombuffer(w.readframes(w.getnframes()),dtype='<i2').astype(np.int32)
peaks={'voice.wav':int(np.max(np.abs(voice_pcm)))}
peaks['music.wav']=save(root/'music.wav',music*env)
peaks['ambience.wav']=save(root/'ambience.wav',amb*env)
peaks['mix.wav']=save(root/'mix.wav',mix)
report={'source':'original procedural synthesis; no third-party samples','seed':28,'music_rms_before_fade':0.0045,'ambience_rms_before_fade':0.00065,'duration_s':round(duration,2),'sample_rate':sr,'voice_filter_reapplied':False,'voice_sha256':hashlib.sha256(voice_path.read_bytes()).hexdigest(),'peaks_pcm16':peaks,'mix_peak_float':float(np.max(np.abs(mix))),'music_fade_in_s':2,'music_fade_out_s':5,'final_narration_silence_s':round(duration-json.loads((root/'voice-timeline.json').read_text())['units'][-1]['end_s'],2)}
(root/'audio-mix-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
