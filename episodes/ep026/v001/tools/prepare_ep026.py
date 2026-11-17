import json
from pathlib import Path
OUT=Path(__file__).resolve().parents[1]
voice=json.loads((OUT/'voice-timeline.json').read_text()); units=json.loads((OUT/'narration-units.json').read_text()); snap=json.loads((OUT/'script.snapshot.json').read_text())
source={u['id']:u for u in units}; groups=[]; cur=[]; dur=0; target=8.7; max_s=11.2
for u in voice['units']:
    length=u['end_s']-u['start_s']+source[u['id']]['pause_after_s']
    # Do not merge across paragraphs; aim for conversational 8-10 s shots.
    if cur and (u['paragraph_id']!=cur[-1]['paragraph_id'] or dur+length>max_s): groups.append(cur);cur=[];dur=0
    cur.append(u);dur+=length
    if dur>=target: groups.append(cur);cur=[];dur=0
if cur: groups.append(cur)
# Context-aware, continuity-preserving still compositions.
def describe(text,pid,n):
 t=text
 if pid=='p000':
  return '独立开场插画：温馨木屋餐厅夜幕初临，皮皮站在暖灯下，望向桌边袅袅上升的一小团白水汽，眼神带着安静好奇；暗示忙碌之后安顿下来的故事。'
 if pid=='p001':
  return '傍晚的木屋餐厅，皮皮穿灰蓝背带裤和米色上衣，像小主人一样在木桌旁准备托盘和热茶，神情认真又自信；小熊绒绒和小鹿芽芽在桌边一起做松果小人。'
 if pid=='p002':
  if any(k in t for k in ['倒了','杯子','茶','喝茶']): return '同一餐厅、同一张木桌与暖灯。皮皮端着小托盘，为小鹿芽芽倒苹果茶、为小熊绒绒倒蜂蜜水；三只彩色小杯排在一起，松果小人摆满桌面，朋友们愉快交谈。'
  return '同一木屋餐厅桌面近景：搪瓷小水壶稳稳坐在同一块圆形软木隔热垫上，壶身圆润浅奶油色带细蓝边，壶嘴冒出细细白水汽；皮皮与两位朋友在暖灯下做松果小人。'
 if pid=='p003':
  if any(k in t for k in ['收拾','洗干净','擦干手']): return '朋友们已道别离开；餐厅仍是同一暖灯和木桌。皮皮独自把三只喝空的小彩杯逐只洗净，整齐放回小木托盘，神情平静专注。'
  return '餐厅木桌静物与皮皮视角：同一奶油白搪瓷水壶仍坐在软木垫上，壶嘴旁只余最后一缕淡白水汽；空木桌安静下来。'
 if pid=='p004':
  if any(k in t for k in ['羽毛','叶子','弯弯']): return '皮皮隔着桌子双手托腮安静凝望；同一小水壶壶嘴飘出最后一缕白汽，刚离壶时弯成轻巧羽毛叶片的轮廓，轻盈而自然，不是实体物件。'
  return '特写同一缕水汽在木屋餐厅暖黄灯光中被轻风拉成长长的白色小围巾形状，边缘逐渐变淡；下方同一只搪瓷壶与软木垫保持原位，皮皮远处静静观察。'
 if pid=='p005':
  if any(k in t for k in ['融进','凉','安安稳稳','散开']): return '餐厅暖灯下最后一缕水汽轻轻消散，奶油白搪瓷壶已不再冒汽，安稳地坐在同一软木隔热垫上；皮皮把木托盘挪到桌侧，为中央腾出安静空处。'
  return '皮皮用干布巾仔细擦去同一木桌角浅浅的水印，随后轻轻合上餐边柜的小木门，神情满足、动作不急。'
 if pid=='p006':
  return '木屋卧室同一布局：暖黄色毛毯已铺好，浅米色枕头蓬松，皮皮戴深蓝星星睡帽，慢悠悠躺下，将同一只橙色胡萝卜玩偶放在身边；长耳放松，神情舒缓。'
 if pid=='p007':
  return '安静的木屋卧室，皮皮侧躺在柔软枕头上，橙色胡萝卜玩偶在身旁，暖黄毛毯覆盖到肩膀；小爪和长耳都自然放松，屋内只留夜晚的安静。'
 return '皮皮在暖灯柔和的卧室里逐渐放松，安稳准备入睡；温暖细腻水彩，不添加文字或剧本以外物品。'
assets={
 'kettle':{'asset_id':'ep026_enamel_kettle','appearance':'固定圆肚浅奶油白搪瓷小水壶，细蓝色壶口边与壶盖钮，短弯壶嘴朝右，圆弧把手在左；所有镜头同一造型。','first_appearance_shot':1,'state':'坐在圆形编织软木隔热垫上，朋友离开后逐渐冷却。'},
 'trivet':{'asset_id':'ep026_cork_trivet','appearance':'同一圆形厚软木隔热垫，天然浅棕细颗粒边缘，始终位于水壶下方。','first_appearance_shot':1,'state':'全程不移动，承托搪瓷壶。'},
 'tray':{'asset_id':'ep026_wooden_tray','appearance':'长方形浅木托盘，圆角，木纹清楚，无花纹。','first_appearance_shot':1,'state':'皮皮用其端杯；后来从桌面中间挪到一侧。'},
 'cups':{'asset_id':'ep026_three_cups','appearance':'固定三只矮胖陶杯：苹果红、蜂蜜黄、浅天蓝；朋友来时排在桌边，喝完后一只只洗净放回托盘。','first_appearance_shot':1,'state':'盛茶时排列，朋友离开后清洗并收拢。'},
 'pinecone_figures':{'asset_id':'ep026_pinecone_figures','appearance':'同一组手工松果小人，天然棕色松果身体，彩纸小帽，木珠脸，无字。','first_appearance_shot':1,'state':'朋友和皮皮一起完成，摆在餐桌上。'},
 'steam':{'asset_id':'ep026_last_steam','appearance':'壶嘴升起的一缕很淡白色水汽，先卷曲似羽毛叶片，再被轻风拉成长围巾形，逐渐变淡消散；始终是气态，无脸无手无实体。','first_appearance_shot':2,'state':'逐镜减淡直至消散。'},
 'bedroom':{'asset_id':'ep026_bedroom_layout','appearance':'木屋卧室固定同一空间：浅木床靠墙、米色枕头、暖黄色毛毯、床边木地板与一盏柔和暖灯。','first_appearance_shot':None,'state':'后段场景，布局不变。'},
 'carrot':{'asset_id':'ep026_carrot_plush','appearance':'一只橙色胡萝卜形绒布玩偶，绿色短叶冠、圆润缝线，固定尺寸约皮皮前臂长。','first_appearance_shot':None,'state':'放在枕边靠近皮皮。'},
 'blanket':{'asset_id':'ep026_yellow_blanket','appearance':'同一条暖黄色柔软毛毯，细密织纹。','first_appearance_shot':None,'state':'已铺床，随后覆盖皮皮至肩膀。'},
}
shots=[]
for n,g in enumerate(groups,1):
 text=''.join(x['text'] for x in g); pid=g[0]['paragraph_id']; chars=['pipi']
 if pid=='p001' and any(k in text for k in ['绒绒','芽芽','朋友','大家']): chars=['pipi','rongrong','yaya']
 refs=[]
 if pid in ('p001','p002'): refs+=['kettle','trivet','tray','cups','pinecone_figures']
 if pid in ('p003','p004','p005'):
  refs+=['kettle','trivet','steam']
  if any(k in text for k in ['托盘','杯','擦']): refs+=['tray','cups']
 if pid in ('p006','p007','p008'): refs+=['bedroom','carrot','blanket']
 if pid=='p002' and any(k in text for k in ['水汽','壶嘴']): refs+=['steam']
 outfits={'pipi':'day_v001'} if pid in ('p001','p002','p003','p004','p005') else {'pipi':'default_v001'}
 shots.append({'id':n,'title':f'镜头{n:02}','paragraph_id':pid,'text':text,
  'source_ranges':[{'unit_id':x['id'],'start_char':0,'end_char':len(x['text'])} for x in g],
  'characters':chars,'outfits':outfits,'visual_description':describe(text,pid,n),'setting':{'p000':'暖灯木屋餐厅开场','p001':'傍晚木屋餐厅','p002':'同一木屋餐厅与餐桌','p003':'同一餐厅收拾桌面','p004':'同一餐厅观察水汽','p005':'同一餐厅慢慢收尾','p006':'木屋卧室','p007':'同一木屋卧室','p008':'同一木屋卧室'}[pid],
  'continuity_refs':[assets[k]['asset_id'] for k in dict.fromkeys(refs)],'state_before':'沿用前镜已建立的同一餐厅/卧室布局与物件外观；仅发生旁白明确描述的动作。','state_after':'按本镜口播更新物件与角色状态，不增添无依据的移动或变化。','transition_from':n-1 if n>1 else None,'motion':'fixed','image':f'images/shot_{n:02}.png','prompt_file':f'illustration-prompts/shot_{n:02}.txt','reference_manifest':f'references/shot_{n:02}.json'})
# Character role presence correction: absent characters after farewell.
for s in shots:
 if s['paragraph_id']!='p001': s['characters']=['pipi']
 if s['paragraph_id']=='p002' and not any(k in s['text'] for k in ['朋友','大家','绒绒','芽芽']): s['characters']=[]
plan={'episode':snap['id'],'version':'v001','script_version':'v5','cover_title':'小云散开啦','total_duration_s':voice['duration_s'],'actual_audio_measured':False,'max_visible_duration_s':15,'shots':shots,'shot_count':len(shots),'timing_basis':'measured TTS word boundaries'}
(OUT/'storyboard.draft.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n')
continuity={'episode':'ep026','version':'v001','preflight_status':'passed_text_preflight','assets':assets,'shot_states':[{'shot_id':s['id'],'paragraph_id':s['paragraph_id'],'place':s['setting'],'characters_present':s['characters'],'assets':s['continuity_refs'],'state_before':s['state_before'],'state_after':s['state_after'],'transition_from':s['transition_from']} for s in shots], 'text_preflight':'故事顺序复核：傍晚小主人招待两位朋友→朋友离开、逐只洗杯收拾→观察最后一缕水汽形态变化且不触碰→水汽消散并等壶冷却→擦拭桌面、关柜门→回卧室准备休息。水壶与软木垫始终同位；托盘由桌中挪到一侧；朋友离开后不再出镜；卧室阶段沿用同一床、枕头、毛毯及胡萝卜玩偶。图像接触表审查待完成。'}
(OUT/'continuity.json').write_text(json.dumps(continuity,ensure_ascii=False,indent=2)+'\n')
print('shots',len(shots),'audio',voice['duration_s'],'speech hanzi',sum(sum('\u3400'<=c<='\u9fff' for c in u['text']) for u in units))
