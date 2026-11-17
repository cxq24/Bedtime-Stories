import json
from pathlib import Path
OUT=Path(__file__).resolve().parents[1]
old=json.loads((OUT/'storyboard.draft-34.json').read_text())
script=json.loads((OUT/'script.snapshot.json').read_text()); voice=json.loads((OUT/'voice-timeline.json').read_text())
by={s['id']:s for s in old['shots']}
groups=[[i] for i in range(1,12)]+[[12,13],[14,15],[16],[17,18],[19],[20],[21],[22,23],[24,25],[26],[27],[28],[29],[30],[31,32],[33],[34]]
shots=[]
for idx,ids in enumerate(groups,1):
 a=by[ids[0]]; b=by[ids[-1]]; text=''.join(by[i]['text'] for i in ids)
 descriptions=' '.join(by[i]['visual_description'] for i in ids)
 sh={k:v for k,v in a.items() if k not in ['id','title','source_ranges','text','start_s_estimate','end_s_estimate','speech_start_s','speech_end_s','actual_start_s','actual_end_s','visible_start_s','visible_end_s','visible_duration_s','prompt','reference_inputs','reference_roles']}
 sh.update(id=idx,title=f'镜头{idx:02}',text=text,source_ranges=[r for i in ids for r in by[i]['source_ranges']],
           continuity_refs=list(dict.fromkeys(r for i in ids for r in by[i].get('continuity_refs',[]))),
           characters=list(dict.fromkeys(r for i in ids for r in by[i].get('characters',[]))),
           outfits={**by[ids[0]].get('outfits',{}),**by[ids[-1]].get('outfits',{})},
           paragraph_id=a['paragraph_id'], transition_from=idx-1 if idx>1 else None,
           image=f'images/shot_{idx:02}.png',prompt_file=f'illustration-prompts/shot_{idx:02}.txt',reference_manifest=f'references/shot_{idx:02}.json')
 sh['visual_description']=descriptions
 shots.append(sh)
manual={
 12:'皮皮擦干小爪时发现同一只奶油白搪瓷水壶旁最后一缕很淡的白水汽；他停下擦拭，目光轻轻落在壶嘴边。',
 13:'皮皮没有走开，隔着桌面双手托腮安静看着同一缕白汽逐渐飘散；暖灯、搪瓷壶与软木垫固定在同一位置。',
 14:'皮皮隔着桌子双手托腮安静凝望；同一小水壶壶嘴飘出最后一缕白汽，刚离壶时弯成轻巧羽毛叶片的轮廓，轻盈而自然，不是实体物件。',
 15:'最后一缕白汽被暖风拉成长长轻薄的白色围巾形，正在灯光里慢慢变淡；它仍是水汽，没有脸、没有手、不是实体物品。',
 16:'皮皮没有伸爪抓水汽或扇它，而是轻轻把木托盘从桌面中间挪到一边，为水壶和最后一缕白汽留出安静空处。',
 17:'餐桌中央已空出一片安静空间，最后水汽越升越高、越来越淡；皮皮站在桌旁静静看着，水壶与软木垫仍保持原位。',
 19:'水壶逐渐冷却，安安稳稳坐在同一块厚软木垫上，壶嘴没有水汽；皮皮站在桌边看着它。',
 20:'桌上三只洗净的彩色小杯已经放回同一木托盘，皮皮用干布巾仔细擦桌角的浅浅水印，动作轻柔。',
 21:'皮皮轻轻合上餐边柜小木门，刚忙完招待后的他转身朝卧室走去，餐厅的水壶与茶具仍留在桌上。',
 22:'卧室暖灯下，皮皮安静想着水壶旁的小云已经完成今晚的旅行；他自己的招待任务也完成了，神情满足而放松。',
 23:'小主人皮皮在木屋卧室轻松地准备休息，身边是暖黄毛毯、浅米枕头和橙色胡萝卜玩偶，姿势松弛。',
 24:'同一间木屋卧室的床已铺好暖黄色毛毯，浅米色小枕头拍得松软；皮皮站在床边准备安顿下来。',
 25:'皮皮把同一只橙色胡萝卜玩偶放到枕边，然后慢慢躺到同一张浅木床上，夜灯柔和、动作从容。',
 26:'皮皮已躺好休息，端过托盘的小爪自然放在毛毯上，长耳朵舒展在枕边，卧室安静下来。',
 27:'皮皮在暖黄色毛毯下把身体放得软软舒服，枕边的胡萝卜玩偶陪着他；他闭上眼睛准备做轻轻的梦。',
 28:'同一卧室的安静夜晚，皮皮在软枕与暖黄毛毯下睡熟，橙色胡萝卜玩偶在身旁，柔和月蓝从窗外映入。'}
for sh in shots:
 if sh['id'] in manual: sh['visual_description']=manual[sh['id']]
 sh['outfits']={'pipi':'day_v001'} if sh['paragraph_id'] not in ('p006','p007','p008') else {'pipi':'default_v001'}
 if sh['id']==1: sh['characters']=['pipi','rongrong','yaya']
 elif sh['id'] in (3,4,7,8,9):
  if any(k in sh['text'] for k in ['绒绒','芽芽','朋友','大家']): sh['characters']=['pipi','rongrong','yaya']
 else: sh['characters']=['pipi']
 sh['state_before']='沿用前镜固定空间和重复物件外观；本镜仅改变口播所述的角色动作或物件状态。'
 sh['state_after']='按本镜口播更新水汽、茶具和角色位置；重复道具不得移动、替换或复制。'
 sh['transition_from']=sh['id']-1 if sh['id']>1 else None
# Split the final spoken sentence from its 8-second silent tail so no still exceeds the 15-second image hold ceiling.
last=shots.pop()
ranges=last['source_ranges']
assert len(ranges)==2 and ranges[0]['unit_id']=='p008_u04' and ranges[1]['unit_id']=='p008_u05'
units={u['id']:u for u in json.loads((OUT/'narration-units.json').read_text())}
for new_id,r,description in [(28,ranges[0],'皮皮在暖黄色毛毯下把身体放得软软舒服，靠着柔软枕头，神情放松，准备休息。'),(29,ranges[1],'同一卧室的安静夜晚，皮皮闭上眼睛安然入睡，橙色胡萝卜玩偶在身旁，柔和月蓝从窗外映入；留出安静梦境尾声。')]:
    clone=dict(last); clone.update(id=new_id,title=f'镜头{new_id:02}',text=units[r['unit_id']]['text'],source_ranges=[r],visual_description=description,image=f'images/shot_{new_id:02}.png',prompt_file=f'illustration-prompts/shot_{new_id:02}.txt',reference_manifest=f'references/shot_{new_id:02}.json',transition_from=new_id-1)
    shots.append(clone)
plan={'episode':'ep026','version':'v001','script_version':'v5','cover_title':'皮皮看见小云','total_duration_s':voice['duration_s'],'actual_audio_measured':False,'max_visible_duration_s':15,'shots':shots,'shot_count':len(shots),'timing_basis':'actual TTS word boundaries; final image carries silent 8-second ending'}
(OUT/'storyboard.draft.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n')
assets=json.loads((OUT/'continuity.json').read_text())['assets']
continuity={'episode':'ep026','version':'v001','preflight_status':'passed_text_preflight','assets':assets,'shot_states':[{'shot_id':s['id'],'paragraph_id':s['paragraph_id'],'place':s['setting'],'characters_present':s['characters'],'continuity_refs':s['continuity_refs'],'state_before':s['state_before'],'state_after':s['state_after'],'transition_from':s['transition_from']} for s in shots], 'text_preflight':'顺序复核通过：招待朋友→朋友离开后洗杯并观察最后一缕水汽→不触碰水汽、托盘移到一侧→水汽消散与水壶冷却→擦净桌面并关柜门→皮皮回卧室安顿。水壶与软木垫固定不动，托盘只在口播处从桌面中央移开，朋友离家后不再出现；卧室床铺、枕头、胡萝卜玩偶和毛毯沿用相同外观。图像完成后需另做接触表审查。'}
(OUT/'continuity.json').write_text(json.dumps(continuity,ensure_ascii=False,indent=2)+'\n')
# Reassign exact unique illustrations already generated where they match these first scenes.
for new_id,old_id in {**{i:i for i in range(1,13)},13:15,15:18}.items():
 src=OUT/f'images/shot_{old_id:02}.png'; dst=OUT/f'images/shot_{new_id:02}.png'
 if src.is_file() and src.resolve()!=dst.resolve(): dst.write_bytes(src.read_bytes())
print('storyboard groups',len(shots),'reuse',sum((OUT/f'images/shot_{i:02}.png').exists() for i in range(1,len(shots)+1)))
