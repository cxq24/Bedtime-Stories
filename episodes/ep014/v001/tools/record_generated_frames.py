import hashlib,json,sys
from pathlib import Path
from PIL import Image
b=Path(__file__).resolve().parents[1]
for i in map(int,sys.argv[1:]):
 s=next(x for x in json.loads((b/'storyboard.json').read_text())['shots'] if x['id']==i)
 p=b/s['image']; refs=json.loads((b/s['reference_manifest']).read_text())
 prompt=f'prompts/shot_{i:02d}.txt'
 d={'shot_id':i,'source':'OpenAI image_gen','image_path':s['image'],'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'size':list(Image.open(p).size),'prompt':prompt,'reference_inputs':refs['referenced_image_paths'],'continuity_asset_ids':s['continuity_refs'],'image_status':'generated_pending_visual_review'}
 p.with_suffix('.source.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print('recorded',sys.argv[1:])
