import json,hashlib
from pathlib import Path
OUT=Path(__file__).resolve().parents[1]
plan=json.loads((OUT/'storyboard.json').read_text())
for shot in plan['shots']:
 image=OUT/shot['image']
 if not image.is_file(): continue
 manifest=OUT/shot['reference_manifest']; target=image.with_suffix('.source.json')
 if target.exists(): continue
 record={'source':'OpenAI image_gen','generated_image':'original full-scene illustration; resized only by renderer','image_path':shot['image'],'sha256':hashlib.sha256(image.read_bytes()).hexdigest(),'prompt_file':shot['prompt_file'],'prompt':shot['prompt'],'reference_manifest':shot['reference_manifest'],'reference_inputs':shot.get('reference_inputs',[]),'characters':shot['characters'],'outfits':shot['outfits'],'user_visual_acceptance':'not_recorded'}
 target.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print('source records written for new illustrations')
