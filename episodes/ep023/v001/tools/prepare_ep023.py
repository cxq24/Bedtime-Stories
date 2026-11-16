import json,re
from pathlib import Path
OUT=Path(__file__).resolve().parents[1]
voice=json.loads((OUT/'voice-timeline.json').read_text()); units=json.loads((OUT/'narration-units.json').read_text()); snap=json.loads((OUT/'script.snapshot.json').read_text())
source_by={u['id']:u for u in units}; audio_by={u['id']:u for u in voice['units']}
# Greedy, paragraph-preserving, semantically natural shot groups near 8-9 sec.
groups=[]; group=[]; dur=0; target=8.6; max_s=10.8
for u in voice['units']:
    if group and (u['paragraph_id']!=group[-1]['paragraph_id'] or dur+u['end_s']-u['start_s']>max_s):
        groups.append(group);group=[];dur=0
    group.append(u);dur+=u['end_s']-u['start_s']+source_by[u['id']]['pause_after_s']
    if dur>=target:
        groups.append(group);group=[];dur=0
if group:groups.append(group)
# Build exact source ranges at full unit boundaries.
assets={
 'postcard':{'asset_id':'asset_postcard_01','appearance':'一张小尺寸手绘明信片，奶油白纸边，正面是简单彩色花朵与星点图案，不含可读文字。','reference_image':'images/shot_04.png','initial_state':'皮皮在学堂画好后寄出，邮筒收件。'},
 'postbox':{'asset_id':'asset_postbox_01','appearance':'森林邮局旁固定的圆顶绿色木质邮筒，正面有小投信口与深绿色底座。','reference_image':'images/shot_04.png','initial_state':'邮筒位于森林学堂外的邮局旁。'},
 'cloud':{'asset_id':'asset_cloud_01','appearance':'一朵低饱和浅白、松软不规则轮廓的云，夜间边缘有淡银色月光，无脸无手、不实际携带信件。','reference_image':'images/shot_14.png','initial_state':'夜间由窗外缓缓飘过，后来移出窗框。'},
 'moon':{'asset_id':'asset_moon_01','appearance':'小而清楚的暖白弯月，固定在夜空背景，形状保持一致。','reference_image':'images/shot_14.png','initial_state':'夜晚窗外，先被云遮挡后显露。'},
 'window':{'asset_id':'asset_window_01','appearance':'卧室北墙木窗，分格木窗框、窗台，窗外可见树梢与夜空。','reference_image':'images/shot_08.png','initial_state':'始终在床边同一位置。'},
 'curtain':{'asset_id':'asset_curtain_01','appearance':'浅绿叶片花纹的软布窗帘，两侧系束；后段只留一个小三角缝。','reference_image':'images/shot_08.png','initial_state':'开始较开敞，皮皮休息前留出一个小三角视线缝。'},
 'bed':{'asset_id':'asset_bed_01','appearance':'同一张浅木床，木床头、柔软蓝灰与暖黄色拼色寝具，靠近窗台。','reference_image':'images/shot_08.png','initial_state':'皮皮由床边坐下后逐渐躺回。'},
 'pillow':{'asset_id':'asset_pillow_01','appearance':'床头同一只浅米色柔软枕头，绣一片小叶纹，无形变。','reference_image':'images/shot_08.png','initial_state':'先空置，之后接住皮皮的头部。'},
 'carrot_plush':{'asset_id':'asset_carrot_01','appearance':'一只橙色胡萝卜形绒布玩偶，绿色短叶冠、圆润缝线，尺寸约皮皮前臂长。','reference_image':'images/shot_20.png','initial_state':'床边待抱，后由皮皮抱到身侧并盖暖黄毯。'},
 'blanket':{'asset_id':'asset_blanket_01','appearance':'一条暖黄色柔软小毛毯，细小织纹，床上使用；先覆盖胡萝卜玩偶，再盖至皮皮肩膀。','reference_image':'images/shot_21.png','initial_state':'床边折叠，随后覆盖玩偶与皮皮肩部。'} }
def visual(text,pid,idx):
    t=text
    if pid=='p000': return ('开场：' + ('夜色窗前的皮皮抬头看着月亮与慢云，眼神好奇、耳朵轻轻抬起' if idx%2==0 else '窗外浅云缓缓经过弯月，皮皮在窗边期待明信片远行')+'；9:16水彩，留出底部字幕区。')
    if any(k in t for k in ['学堂','写自己的名字']): return '白天森林学堂，皮皮坐在小木桌前练习写名字，专注又带一点初学的开心，桌面纸张不出现可辨文字。'
    if any(k in t for k in ['明信片','画了一张']): return '森林学堂木桌旁，皮皮用蜡笔画花朵与星点装饰明信片，神情认真满足，卡片上无可读字。'
    if any(k in t for k in ['邮筒','寄给','投进']): return '森林邮局旁的固定绿色邮筒，皮皮将同一张花朵明信片投入小投信口，动作清楚、神情珍惜。'
    if any(k in t for k in ['喜鹊','邮差叔叔','两座大山','远方山谷']): return '白天森林邮局，戴蓝帽的喜鹊邮差温和地向皮皮解释寄信路程，皮皮抬头认真倾听；保持两者距离自然。'
    if any(k in t for k in ['坐在床边','睡觉的时间','窗外的夜空']): return '同一间木质卧室，皮皮穿深蓝星星睡帽坐在床沿仰望固定木窗，惦记远方的外婆，神情牵挂但平和。'
    if any(k in t for k in ['白云','月亮','夜空']): return '从同一卧室木窗向外看，浅白软云缓慢经过弯月，树梢与屋顶在下方；不画云的脸或邮件。'
    if any(k in t for k in ['慢邮差','银色月光边','挨家挨户']): return '夜空远景，淡银月光勾出白云边缘，云缓缓越过树叶与小木屋屋顶，安静送出夜色的想象，不出现实体信件。'
    if any(k in t for k in ['盯','小眼睛','发酸','撑着床沿']): return '皮皮仍坐在床边望向窗外，眼睛略显疲倦、前爪撑在床沿，耳朵稍垂；表现长时间等待，不画痛苦。'
    if any(k in t for k in ['哈欠','喜鹊邮差叔叔说','一直盯着']): return '卧室床边，皮皮打一个小哈欠，目光从窗外转回枕头，脸上出现理解与放松，不画文字气泡。'
    if any(k in t for k in ['靠回','枕头','三角缝隙']): return '皮皮靠回同一张木床的米色枕头，轻轻把叶子花窗帘留成小三角缝，身体姿势渐渐放松。'
    if any(k in t for k in ['胡萝卜玩偶','暖黄色的毛毯','肩膀']): return '床边近景，皮皮把同一只橙色胡萝卜玩偶放在身旁并为它拉好暖黄小毯，再把毯子盖到自己肩部，动作连续。'
    if any(k in t for k in ['闭着眼睛','睁开一条眼缝','挪开了']): return '皮皮在枕头上闭眼歇息后微微睁开一条眼缝，望向同一扇木窗；云已悄悄移出窗框，神情轻轻惊喜。'
    if any(k in t for k in ['月光','木地板','回信']): return '窗外云已离开，皎洁月光越过窗框落在床边木地板上，像一片安静银色光毯；保持床窗布局不变。'
    if any(k in t for k in ['从容的速度','慢慢往前走']): return '月光铺在卧室地板，窗外云继续向前飘远，树叶与屋顶安静留在夜色里，画面平静从容。'
    if any(k in t for k in ['闭上了眼睛','云朵一样','甜甜的梦乡','晚安']): return '皮皮终于完全闭上眼睛，头被同一只米色枕头稳稳托住，胡萝卜玩偶与暖黄毛毯保持在身旁，安然入梦。'
    return '同一段情节的静态水彩关键画面，皮皮保持稳定身份外形，按旁白动作自然表演，视线落在当前提及的对象；不添加文字、道具或情节。'
shots=[]
for n,g in enumerate(groups,1):
    text=''.join(x['text'] for x in g); pid=g[0]['paragraph_id']; refs=[]
    for key,terms in {'postcard':['明信片','寄出','信件'],'postbox':['邮筒'],'cloud':['云'],'moon':['月亮','月光','月色'],'window':['窗','窗外'],'curtain':['窗帘','缝隙'],'bed':['床','床边'],'pillow':['枕头'],'carrot_plush':['胡萝卜玩偶','玩偶'],'blanket':['毛毯','毯子']}.items():
       if any(t in text for t in terms):refs.append(assets[key]['asset_id'])
    start=g[0]['start_s'];end=g[-1]['end_s']
    ranges=[]
    for x in g:
      original=source_by[x['id']]['text']
      ranges.append({'unit_id':x['id'],'start_char':0,'end_char':len(original)})
    shots.append({'id':n,'title':f'镜头{n:02d}','source_ranges':ranges,'text':text,'place':('森林学堂/森林邮局/山谷想象' if pid=='p001' else '皮皮卧室与窗外夜空'),'reality_layer':('现实' if pid!='p000' else '片头引入'),'characters':['pipi'] if pid!='p001' or not any(k in text for k in ['喜鹊','邮差叔叔']) else ['pipi','magpie_postman'],'visual_description':visual(text,pid,n),'continuity_refs':refs,'state_before':'承接前镜已说明的地点和物件状态；人物动作按本镜原文顺序开始。','state_after':'完成本镜旁白所述动作；无文本依据的道具/角色状态不变化。','transition_from':shots[-1]['id'] if shots else None,'motion':'fixed','image':f'images/shot_{n:02d}.png','prompt_file':f'illustration-prompts/shot_{n:02d}.txt','reference_manifest':f'references/shot_{n:02d}.json','scene':'classroom_post_office' if pid=='p001' else 'bedroom_night','start_s_estimate':start,'end_s_estimate':end})
plan={'episode':snap['id'],'version':'v001','script_version':'v5','cover_title':'云朵邮差','actual_audio_measured':False,'max_visible_duration_s':15,'total_duration_s':voice['duration_s'],'shots':shots,'shot_count':len(shots),'timing_basis':'actual voice duration; lock after storyboard ranges'}
(OUT/'storyboard.draft.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n')
# Continuity ledger with visual state narrative for repeated props.
continuity={'episode':'ep023','version':'v001','preflight_status':'passed_text_preflight','assets':assets,'shot_states':[{'shot_id':s['id'],'place':s['place'],'characters_present':s['characters'],'assets':s['continuity_refs'],'state_before':s['state_before'],'state_after':s['state_after'],'transition_from':s['transition_from']} for s in shots],'text_preflight':'按镜号顺序检查了寄信、夜间等待、云移出窗框、月光照到地板、皮皮入睡的动作因果；室内卧室布局保持固定。图像接触表待完成。'}
(OUT/'continuity.json').write_text(json.dumps(continuity,ensure_ascii=False,indent=2)+'\n')
print('draft shots',len(shots),'duration',voice['duration_s'],'min/max chars',min(len(x['text']) for x in shots),max(len(x['text']) for x in shots))
