#!/usr/bin/env python3
"""Import generated image paths and retain prompt/reference provenance."""
import argparse,base64,json,shutil
from pathlib import Path
from PIL import Image
OUT=Path(__file__).resolve().parents[1]
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--manifest-b64',required=True);ap.add_argument('--overwrite',action='store_true');args=ap.parse_args()
 data=json.loads(base64.b64decode(args.manifest_b64).decode());board=json.loads((OUT/'storyboard.json').read_text());entries=json.loads((OUT/'prompts/shot_prompts.json').read_text());by={x['shot_id']:x for x in entries}
 for item in data:
  sid=item['shot_id'];target=OUT/'images'/f'shot_{sid:02}.png';source=Path(item['source'])
  if not source.is_file(): raise FileNotFoundError(source)
  if target.exists() and not args.overwrite: raise FileExistsError(target)
  shutil.copy2(source,target)
  with Image.open(target) as im: size=list(im.size);im.verify()
  (OUT/'images'/f'shot_{sid:02}.source.json').write_text(json.dumps({'image_tool':'built_in image_gen','shot_id':sid,'image':f'images/shot_{sid:02}.png','prompt':item['prompt'],'references_loaded':item['references'],'output_source':str(source),'size_px':size,'review_status':'generated_pending_contact_sheet_and_continuity_review'},ensure_ascii=False,indent=2)+'\n')
  shot=next(s for s in board['shots'] if s['id']==sid);shot['image_status']='generated';shot['image_source']=f'images/shot_{sid:02}.source.json'
  by[sid].update(prompt=item['prompt'],references_loaded=item['references'],output_source=str(source))
 (OUT/'prompts/shot_prompts.json').write_text(json.dumps(sorted(by.values(),key=lambda x:x['shot_id']),ensure_ascii=False,indent=2)+'\n')
 (OUT/'storyboard.json').write_text(json.dumps(board,ensure_ascii=False,indent=2)+'\n');print('IMPORTED',','.join(str(x['shot_id']) for x in data))
if __name__=='__main__':main()
