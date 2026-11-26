#!/usr/bin/env python3
"""Create per-shot image prompts and actual reference manifests from the locked board."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]; OUT=ROOT/'episodes/ep044/v001'
board=json.loads((OUT/'storyboard.json').read_text(encoding='utf-8'))
base='A single static vertical 9:16 watercolor storybook illustration, delicate handmade watercolor and soft paper grain, calm premium Chinese bedtime picture-book style, coherent warm wood interiors and cool winter daylight. Preserve the exact visual action and emotional expression described for this shot. Keep important faces and objects in the upper two-thirds and leave the lower quarter calm and uncluttered for later subtitles. No text, no letters, no captions, no watermark, no panels, no collage, no border. '
entries=[]
for s in board['shots']:
    refs=[]
    if s['characters']:
        refs += ['/workspace/Bedtime-Stories/03_素材与参数/角色参考图库/v4/初始化与转场评估_v001/角色原图/pipi_identity_v001.png']
        wardrobe='pipi_sleep_wardrobe.png' if s['wardrobe_ids'].get('pipi')=='sleep_v001' else 'pipi_day_wardrobe.png'
        refs += [str(OUT/'references'/wardrobe)]
    if s['id']>=2:
        refs += [str(OUT/'references/bedroom_scene_ref.png'),str(OUT/'assets/prop_reference_board.png')]
        if s['id'] in range(3,22): refs += [str(OUT/'images/shot_00.png')]
    elif s['id']==1:
        refs += [str(OUT/'images/shot_00.png')]
    if len(refs)>5: raise ValueError((s['id'],refs))
    expression=''
    if s['characters']:
        expression='Pipi identity must match the official gray rabbit references: warm gray fur, round face, pink nose, naturally drooping long ears. Use the described expression, gaze, and body pose for this exact moment; do not copy the reference sheet sleepy or sad face. '
        if s['wardrobe_ids'].get('pipi')=='sleep_v001': expression+='Keep the same pale sleepwear and navy star sleep cap throughout the post-bath bedtime sequence. '
        else: expression+='Keep the same beige top and blue-gray short overalls; no schoolbag in the room except where the shot explicitly places it by the door or bed. '
    prompt=base+expression+s['visual_direction']+' Maintain object identities and spatial layout from the loaded scene/prop references, but create a fresh composition for this shot; never reproduce a reference image verbatim.'
    entries.append({'shot_id':s['id'],'title':s['title'],'prompt':prompt,'references_loaded':refs})
(OUT/'prompts/shot_prompts.json').write_text(json.dumps(entries,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f'PROMPTS_READY {len(entries)} shots; loaded reference counts {min(map(lambda x:len(x["references_loaded"]),entries))}–{max(map(lambda x:len(x["references_loaded"]),entries))}')
