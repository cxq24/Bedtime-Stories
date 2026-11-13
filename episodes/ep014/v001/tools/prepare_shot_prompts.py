#!/usr/bin/env python3
import hashlib, json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]
OUT=ROOT/'episodes/ep014/v001'
sys.path.insert(0,str(ROOT/'local'))
from character_references import resolve
plan=json.loads((OUT/'storyboard.json').read_text())
cont=json.loads((OUT/'continuity.json').read_text())
assets=cont['assets']
for shot in plan['shots']:
    cid=shot['characters']
    outfit=shot['outfits']
    char=resolve(cid,outfit)
    paths=list(char['referenced_image_paths'])
    labels=[]
    for c in char['characters']:
        labels.append(f"Input {paths.index(c['identity_paths'][0])+1} is the strict identity reference for {c['name']} ({c['id']}): {c['identity_anchors']}")
        if c['outfit']:
            for f in c['outfit'].get('files',[]):
                fp=str((ROOT/f['path']).resolve())
                labels.append(f"Input {paths.index(fp)+1} is clothing-only for {c['name']}: {c['outfit']['description']}")
    scene=shot['setting']
    extra=[]
    if scene=='field': extra.append(OUT/'assets/field_anchor.png')
    elif scene=='porch': extra.append(ROOT/'episodes/ep011/v002/assets/porch_anchor.png')
    elif scene in ('bedroom_window','opening_preview'):
        extra.append(OUT/'assets/bedroom_anchor.png' if shot['id']!=3 else OUT/'assets/field_anchor.png')
    sid=shot['id']
    if sid==12: extra.append(OUT/'assets/drawing_frame_landscape_anchor.png')
    elif sid in (13,14,15,16): extra.append(OUT/'assets/drawing_leaf_landscape_anchor.png')
    elif 17<=sid<=31: extra.append(OUT/'assets/drawing_moon_landscape_anchor.png')
    elif 32<=sid<=35: extra.append(OUT/'assets/drawing_final_landscape_anchor.png')
    if 36<=sid<=40: extra.append(OUT/'assets/folder_anchor.png')
    for p in extra:
        p=p.resolve(); v=str(p)
        if v not in paths: paths.append(v)
    if len(paths)>5: raise SystemExit(f"shot {sid}: {len(paths)} refs > image tool limit")
    for i,p in enumerate(paths,1):
        labels.append(f"Input {i}: {p}; use only its labelled purpose (identity/clothes/environment/object); do not copy poses or extra items from it.")
    wardrobes=[]
    if shot['outfits'].get('pipi')=='day_v001': wardrobes.append('Pipi wears the daytime cream shirt, dusty blue short overalls, and blue shoes. Omit the yellow school backpack in this story; it is not mentioned or carried in these scenes. No cap.')
    if shot['outfits'].get('pipi')=='sleep_v001': wardrobes.append('Pipi wears only the navy star-patterned sleep cap and simple oatmeal sleepwear, with cream bedding. No backpack, no yellow blanket, no carrot plush toy; those belong to a different story.')
    if 'diandian' in cid: wardrobes.append('Diandian is a very small mole, about 0.65 Pipi height, grey-brown round body, tiny eyes, pale pink nose, short rounded paws, beige bib. Slightly squint only when focusing; no glasses.')
    if 'goat_teacher' in cid: wardrobes.append('The goat teacher is an adult, clearly taller than the children, cream-and-pale-gray wool, short curved horns, side-drooping ears, small beard, sage cardigan, oatmeal shirt, brown trousers.')
    object_text=''
    if sid<=3: object_text='This is a separate opening vignette. Do not advance the real drawing state; show a blank board or a simple indistinct preview only.'
    elif 7<=sid<=11: object_text='Show one completely blank warm-white portrait sheet on the single board. No brown lines, green leaf, moon, curtain or other marks have been drawn yet.'
    elif sid==12: object_text='On the single portrait paper draw exactly two straight brown vertical frame lines only. No leaf, moon or curtain yet.'
    elif sid==13: object_text='Copy the frame from its reference and add exactly one green leaf at the upper right; still no moon or curtain.'
    elif 14<=sid<=15: object_text='Preserve exactly two brown vertical frame lines and one green leaf; no moon or curtain yet.'
    elif sid==16: object_text='Preserve the frame and leaf; show only the first tiny pale-yellow crayon start of a moon, not a completed circle.'
    elif 17<=sid<=30: object_text='Show exactly the same one solid, fully crayon-colored pale-yellow lopsided moon from the canonical drawing reference, fatter on its left side and thinner on its right, leaning toward the same single green leaf. It is filled across its interior, not an outline or ring. Keep the two brown vertical lines unchanged. No curtain yet.'
    elif sid==31: object_text='Preserve the same two brown lines, one green leaf and one solid pale-yellow lopsided moon from the reference. Add exactly one narrow pale-blue hanging curtain on the left side of the drawing; keep the marks fixed and most of the paper blank.'
    elif 32<=sid<=35: object_text='Copy the finished canonical drawing exactly: same two brown lines, one green leaf, one solid pale-yellow lopsided moon, one narrow pale-blue hanging curtain on the left, and a large blank white area. Do not alter, duplicate or reposition any mark.'
    elif 36<=sid<=38: object_text='The finished drawing is placed carefully inside the one slim closed grey-blue folder; the drawing itself is no longer separately visible. The board stays on the desk.'
    elif 39<=sid<=40: object_text='Diandian carries the same single closed grey-blue folder from the previous shots; keep it in his paws and do not leave another folder in the house.'
    elif sid>=41: object_text='No drawing, drawing board, crayons, eraser or folder in the bedroom. Diandian has left with the folder. The real four-pane window and leafy curtain remain on the wall.'
    else: object_text='Keep the single sheet and its current state unchanged; no added or removed marks.'
    prompt=(
      'Use case: one original full-bleed vertical 9:16 watercolor children’s story illustration for a locked narration shot. '
      'Use each attached image strictly for its labelled reference role. Preserve named character identity and fixed object designs; do not make a collage or copy a reference sheet.\n'
      +' '.join(labels)+'\n'
      +f"Scene location: {scene}. Keep its fixed layout from the environment anchor.\n"
      +f"Visible cast: {', '.join(cid)}; draw each listed character once and no unlisted animals.\n"
      +' '.join(wardrobes)+'\n'
      +f"Single visual moment and acting: {shot['action']}\n"
      +f"Before: {shot['state_before']} After: {shot['state_after']}\n"
      +object_text+'\n'
      +'For all bedroom shots keep one centered four-pane wooden window, the same pale-green leafy curtain hanging only on the right, one low light-wood desk directly beneath it, and one bed against the left wall. These never shift or multiply. On day scenes, soft natural afternoon light; toward farewell, dusk; bedtime is muted blue night outside with a warm bedside glow. The house is the same warm honey-brown wooden cottage.\n'
      +'Style: gentle hand-painted watercolor on fine warm paper, rounded soft shapes, muted natural color, quiet bedtime picture-book mood. Character expression and eye direction must match the present narration moment, never a fixed neutral or sleepy expression unless the narration says so.\n'
      +'Keep faces and key props in the upper 68% (above the bottom subtitle area); one clear coherent camera composition, no split panels, no text, no letters, no logos, no watermark, no extra windows, no duplicate moons, no extra artwork or unlisted props.'
    )
    payload={'id':sid,'title':shot['title'],'destination':shot['image'],'prompt':prompt,'reference_inputs':paths,'characters':cid,'outfits':outfit,'source_ranges':shot['source_ranges'],'timing':{'start_s':shot['actual_start_s'],'end_s':shot['actual_end_s']}}
    (OUT/'prompts'/f'shot_{sid:02d}.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
    (OUT/shot['reference_manifest']).write_text(json.dumps({**char,'referenced_image_paths':paths,'reference_roles':labels,'continuity_asset_ids':shot['continuity_refs']},ensure_ascii=False,indent=2)+'\n')
    shot['environment_reference']=next((str(p.relative_to(OUT)) for p in extra if p.is_relative_to(OUT)),None)
    shot['reference_inputs_verified']={**char,'referenced_image_paths':paths,'reference_roles':labels}
    (OUT/'prompts'/f'shot_{sid:02d}.txt').write_text(prompt+'\n')
(OUT/'storyboard.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n')
print('PREPARED',len(plan['shots']),'shot prompts; max refs',max(len(json.loads((OUT/f'references/shot_{s["id"]:02d}.json').read_text())['referenced_image_paths']) for s in plan['shots']))
