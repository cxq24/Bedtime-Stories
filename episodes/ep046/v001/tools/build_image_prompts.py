#!/usr/bin/env python3
"""Build episode-specific image prompts and actual asset-reference lists."""
import json
from pathlib import Path
OUT=Path(__file__).resolve().parents[1]
board=json.loads((OUT/'storyboard.json').read_text())
refs={k:str((OUT/v).resolve()) for k,v in {
'pipi':'references/pipi_identity_v001.png','pipi_day':'references/pipi_day_wardrobe_nobag.png','pipi_sleep':'references/pipi_sleep_wardrobe.png',
'rongrong':'references/rongrong_identity_v001.png','porch':'references/porch_scene_ref.png','bedroom':'references/bedroom_scene_ref.png',
'blanket':'references/prop_blanket_folded.png','holly':'references/prop_holly_leaf.png','dish':'references/prop_dish.png','basket':'references/prop_wicker_basket.png','carrot':'references/prop_carrot_plush.png'}.items()}
base=('Single static vertical 9:16 watercolor storybook illustration, gentle Chinese bedtime picture-book style, hand-painted watercolor washes and soft paper grain, clean readable composition, one coherent scene only. No collage, split screen, panels, words, letters, captions, watermark or border. Keep important faces/objects in upper two thirds and leave lower quarter quiet for subtitles. ')
entries=[]
for s in board['shots']:
 core=[]; props=[]; chars=s['characters']; c=set(s['continuity_refs'])
 if 'pipi' in chars: core += [refs['pipi'],refs['pipi_sleep'] if s['wardrobe_ids']['pipi']=='sleep_v001' else refs['pipi_day']]
 if 'rongrong' in chars: core += [refs['rongrong']]
 if 'LOC_PORCH_01' in c or 'PROP_BENCH_01' in c: core += [refs['porch']]
 if 'LOC_PIPI_BEDROOM_01' in c or 'PROP_BED_01' in c: core += [refs['bedroom']]
 for asset,key in [('PROP_FLANNEL_BLANKET_01','blanket'),('PROP_HOLLY_LEAF_01','holly'),('PROP_DISH_01','dish'),('PROP_WICKER_BASKET_01','basket'),('PROP_CARROT_PLUSH_01','carrot')]:
  if asset in c: props.append(refs[key])
 # Roles and location have priority; use only the most important prop crops within the five-reference tool limit.
 priority={refs['blanket']:0,refs['holly']:1,refs['basket']:2,refs['carrot']:3,refs['dish']:4}
 core=list(dict.fromkeys(core));props=sorted(set(props),key=lambda x:priority[x]);loaded=core+props[:max(0,5-len(core))]
 assert len(loaded)<=5,(s['id'],loaded)
 character=''
 if 'pipi' in chars:
  character+='Pipi must match the official warm-gray rabbit identity, round face, pink nose and naturally drooping ears; choose the precise facial expression, gaze and pose described for this moment. '+('Use the same pale sleepwear and navy star night cap as the sleepwear reference. ' if s['wardrobe_ids']['pipi']=='sleep_v001' else 'Use the same beige shirt, blue-gray short overalls and blue shoes as the daytime wardrobe reference. ')
 if 'rongrong' in chars:
  character+='Rongrong must match the official friendly young brown-bear identity, broad rounded build, cream muzzle, round ears and small dark nose; wear the muted forest-green vest in porch scenes, warm shy expression, never aggressive. '
 restrictions='Only include props explicitly named in this shot description. Do not add a backpack, carrot plush, dish, basket, leaf, extra blanket, toys or food unless the action below explicitly includes that item. Keep the cream flannel blanket plain, solid ivory, and visually identical across its scenes. '
 prompt=base+character+restrictions+s['visual_direction']+' References guide identity, location or only the particular prop whose crop was loaded. Do not copy a reference composition verbatim.'
 entry={'shot_id':s['id'],'title':s['title'],'prompt':prompt,'references_loaded':loaded}
 entries.append(entry);s['image_prompt_manifest']=f"prompts/shot_{s['id']:02}.json"
 (OUT/'prompts'/f"shot_{s['id']:02}.json").write_text(json.dumps(entry,ensure_ascii=False,indent=2)+'\n')
(OUT/'prompts/shot_prompts.json').write_text(json.dumps(entries,ensure_ascii=False,indent=2)+'\n');(OUT/'storyboard.json').write_text(json.dumps(board,ensure_ascii=False,indent=2)+'\n')
print('PROMPTS_READY',len(entries),'shots; refs',min(len(x['references_loaded']) for x in entries),max(len(x['references_loaded']) for x in entries))
