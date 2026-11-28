#!/usr/bin/env python3
"""Prepare ep046's storyboard draft and continuity states from the adopted v5 narration."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]; OUT=ROOT/'episodes/ep046/v001'
# first/last narration unit and shot title, location, time, visual action, cast, assets, state transition
G=[
('p000_u01','p000_u03','片头：雪中的绒毯','独立开场意象','昨日下午的冬日','宽阔门廊长椅上放着一条米白绒毯，远处零星雪花飘过；画面安静提出分享后如何都温暖的问题。不出现角色或文字。',[],['LOC_OPENING_01','PROP_BENCH_01','PROP_FLANNEL_BLANKET_01'],'独立p000开场图，不承接剧情人物状态。','建立米白绒毯与冬日分享主题。'),
('p000_u04','p000_u05','片头：两份温暖','独立开场细节','冬日傍晚','从长椅近处看米白绒毯柔软地分成两半，两个并排的位置都被照顾到，背景只有轻雪和暖色门廊光；没有角色、无字。',[],['LOC_OPENING_01','PROP_BENCH_01','PROP_FLANNEL_BLANKET_01'],'独立p000开场的第二张画，不复制封面或剧情图。','把分享的核心问题落到绒毯与两个座位。'),
('p001_u01','p001_u03','绒绒来做客','皮皮家门廊','昨日下午·零星小雪','皮皮家的木屋门廊外飘着细雪，皮皮微笑迎接第一次来做客的小熊绒绒；两位朋友相互看着对方，绒绒憨厚而友好，皮皮自然开心。',['pipi','rongrong'],['LOC_PORCH_01','CHAR_PIPI_01','CHAR_RONGRONG_01','PROP_BENCH_01'],'开场意象切入真实剧情；下午细雪，绒绒抵达皮皮家。','两位朋友在门廊相聚，尚未拿出绒毯。'),
('p001_u04','p001_u05','拿出米白绒毯','门廊门口','昨日下午·零星小雪','皮皮从敞开的木门里抱出一条厚实干净的米白法兰绒毯，神情期待地看向门廊长椅；绒绒在旁等待。',['pipi','rongrong'],['LOC_PORCH_01','CHAR_PIPI_01','CHAR_RONGRONG_01','PROP_FLANNEL_BLANKET_01'],'承接两位朋友到达门廊，桌椅与木屋位置稳定。','同一条米白绒毯由皮皮从屋内拿到门廊。'),
('p001_u06','p001_u07','并排看雪听故事','门廊长椅','昨日下午·零星小雪','皮皮和绒绒并排坐在同一条宽木长椅上，米白绒毯平平盖在两人膝腿上，各自盖到一半；两人舒适地望着飘雪，皮皮讲故事，绒绒专注微笑。',['pipi','rongrong'],['LOC_PORCH_01','CHAR_PIPI_01','CHAR_RONGRONG_01','PROP_BENCH_01','PROP_FLANNEL_BLANKET_01'],'皮皮把毯子铺在固定的长椅上，两人共享一条毯子。','形成肩并肩看雪、各盖一半的温暖记忆。'),
('p002_u01','p002_u02','雪越下越大','门廊长椅','昨晚·大雪','傍晚转夜，雪比下午更密，皮皮担忧地望向准备回家的绒绒；他略皱眉，身体向朋友倾过去，绒绒在长椅边。',['pipi','rongrong'],['LOC_PORCH_01','CHAR_PIPI_01','CHAR_RONGRONG_01','PROP_FLANNEL_BLANKET_01'],'时间由下午进入夜晚；原先的薄雪变成大雪。','皮皮注意到绒绒要冒雪回家，开始担心他着凉。'),
('p002_u03','p002_u04','把毯子借给绒绒','门廊出口','昨晚·大雪','皮皮把同一条米白绒毯轻轻披到绒绒肩上挡风雪，眼神关切；绒绒感激地看向皮皮，厚实的绒毯包住肩背但仍露出绿色背心。',['pipi','rongrong'],['LOC_PORCH_01','CHAR_PIPI_01','CHAR_RONGRONG_01','PROP_FLANNEL_BLANKET_01'],'毯子从共同覆盖的长椅移到绒绒身上，外观相同。','绒绒带着借来的绒毯迎雪回家，皮皮留在门口。'),
('p002_u05','p002_u07','晴天里再次来访','皮皮家门前','今天傍晚·雪后放晴','天色放晴，雪地柔亮，绒绒准时来到皮皮家门前；他双手托着一条米白绒毯，皮皮看见好友后露出高兴而轻松的表情。',['pipi','rongrong'],['LOC_PORCH_01','CHAR_PIPI_01','CHAR_RONGRONG_01','PROP_FLANNEL_BLANKET_01'],'新的一天傍晚；绒绒已归还同一条干净的绒毯。','两位朋友重逢，毯子归还状态是已洗净烘干。'),
('p002_u08','p002_u10','叠得方正的绒毯','门廊近景','今天傍晚·雪后放晴','绒绒双手稳稳捧着洗净烘干的米白绒毯，四角叠得方方正正；画面清楚呈现柔软织物与规整折线，皮皮在背景中欣喜注视。',['pipi','rongrong'],['LOC_PORCH_01','CHAR_PIPI_01','CHAR_RONGRONG_01','PROP_FLANNEL_BLANKET_01'],'归还时毯子干净、蓬松前为整齐折叠状态。','呈现熊妈妈帮忙清洗烘干后整齐归还。'),
('p002_u11','p002_u13','冬青叶小礼物','绒毯顶部特写','今天傍晚·雪后放晴','同一条整齐叠放的米白绒毯最上方放着一片干净、鲜亮的绿色冬青叶；绒绒的小熊爪托着毯子，叶片清楚可辨，无额外装饰。',['rongrong'],['LOC_PORCH_01','CHAR_RONGRONG_01','PROP_FLANNEL_BLANKET_01','PROP_HOLLY_LEAF_01'],'绒毯仍在绒绒手中，冬青叶首次出现，作为感谢小礼物。','冬青叶随绒毯一起交到皮皮手中。'),
('p003_u01','p003_u02','收下绒毯与冬青叶','门廊小桌边','今天傍晚·暖光','皮皮开心地接过叠好的米白绒毯，另一只手小心取下绿色冬青叶，准备放进门廊小桌上的浅色小碟子；绒绒在旁温和微笑。',['pipi','rongrong'],['LOC_PORCH_01','CHAR_PIPI_01','CHAR_RONGRONG_01','PROP_FLANNEL_BLANKET_01','PROP_HOLLY_LEAF_01','PROP_DISH_01'],'手持物从绒绒转交给皮皮；冬青叶由毯面取下。','皮皮将冬青叶放进碟子，绒毯仍折叠在手边。'),
('p003_u03','p003_u04','展开轻轻抖开','门廊长椅','今天傍晚·暖光','皮皮双手把同一条折叠的米白绒毯展开，在长椅上轻轻抖开；动作轻柔，毯面展开而没有飞起，绒绒在旁看着。',['pipi','rongrong'],['LOC_PORCH_01','CHAR_PIPI_01','CHAR_RONGRONG_01','PROP_BENCH_01','PROP_FLANNEL_BLANKET_01'],'冬青叶留在门廊小碟子里；毯子从折叠变为展开。','绒毯在长椅上铺开，恢复蓬松状态。'),
('p003_u05','p003_u07','阳光烘出的柔软','绒毯纹理近景','今天傍晚·暖光','米白绒毯在阳光与烘干后显得松软蓬松，柔细绒面带有轻柔的金色暖光；背景虚化为同一门廊木板，无人物或字。',[],['LOC_PORCH_01','PROP_FLANNEL_BLANKET_01'],'保持绒毯已洗净晒干的同一物件，只表现质感变化。','毯子蓬松柔软，散发皂角清香的感受。'),
('p004_u01','p004_u03','绒绒摸摸毯角','门廊长椅','今天傍晚·暖光','绒绒伸出厚厚的大爪子摸米白绒毯的一角，憨厚地笑起来；皮皮站在另一侧，目光温暖地看着他。',['pipi','rongrong'],['LOC_PORCH_01','CHAR_PIPI_01','CHAR_RONGRONG_01','PROP_FLANNEL_BLANKET_01'],'毯子仍松软摊在长椅上，绒绒开始回应触感。','绒绒开心而安心，开始称赞绒毯。'),
('p004_u04','p004_u07','和昨天一样暖和','长椅旁近景','今天傍晚·暖光','绒绒仍轻摸同一条米白绒毯，面带憨厚笑意，向皮皮表达它暖和柔软、像昨天并排看雪时一样舒服；皮皮安静听着，眼神柔和。',['pipi','rongrong'],['LOC_PORCH_01','CHAR_PIPI_01','CHAR_RONGRONG_01','PROP_FLANNEL_BLANKET_01'],'延续绒绒触摸绒毯，人物位置不变。','两位朋友共同认可这条毯子带来的温暖。'),
('p004_u08','p004_u10','把绒毯收进藤篮','卧室床尾','今天傍晚·室内暖光','皮皮将同一条米白绒毯重新叠整齐，轻轻放进卧室床尾的藤编篮子；绒绒站在一旁，跟进卧室。篮内没有其他毯子。',['pipi','rongrong'],['LOC_PIPI_BEDROOM_01','CHAR_PIPI_01','CHAR_RONGRONG_01','PROP_FLANNEL_BLANKET_01','PROP_WICKER_BASKET_01'],'场景由门廊转入卧室；毯子从展开变为平整折叠并入藤篮。','绒毯固定存放于床尾藤篮，冬青叶仍留在门廊碟子。'),
('p004_u11','p004_u13','下回一起看雪','卧室床尾','今天傍晚·室内暖光','皮皮手指身旁床尾的藤编篮子，笑着邀请绒绒下次再下雪时一起拿毯子看雪；绒绒露出温暖感激的笑容，篮里的折叠米白绒毯可见。',['pipi','rongrong'],['LOC_PIPI_BEDROOM_01','CHAR_PIPI_01','CHAR_RONGRONG_01','PROP_WICKER_BASKET_01','PROP_FLANNEL_BLANKET_01'],'承接绒毯收进同一个藤编篮子的状态。','绒绒知道下次仍可以一起分享；毯子安全留在藤篮。'),
('p005_u01','p005_u02','送别后的安静','门廊与木屋门口','今天傍晚·雪后','皮皮站在门廊木门边目送绒绒走远后轻轻合上门；雪已停，小木屋安静下来，皮皮神情平静满足。',['pipi'],['LOC_PORCH_01','CHAR_PIPI_01'],'绒绒离开皮皮家，皮皮留在自家门口。','门廊不再有绒绒，皮皮准备回卧室。'),
('p005_u03','p005_u04','绒绒回家盖棉被','绒绒的熊屋卧室','今天夜晚·暖光','绒绒回到自己的熊屋，安稳坐在床上拉起厚实深棕色大熊棉被；他的卧室是温暖木质空间，与皮皮家明显不同，绒绒面容放松。',['rongrong'],['LOC_RONGRONG_HOME_01','CHAR_RONGRONG_01','PROP_BEAR_QUILT_01'],'切换到绒绒自己的家；绒绒使用自己的棉被，不带走借来的绒毯。','绒绒在自己家中有厚实棉被，已经暖和安顿。'),
('p005_u05','p005_u05','回到自己的床边','皮皮卧室','今天夜晚·暖光','皮皮回到自己的床边，神情放松，视线落向熟悉的床铺与床尾收好的藤篮。',['pipi'],['LOC_PIPI_BEDROOM_01','CHAR_PIPI_01','PROP_WICKER_BASKET_01','PROP_FLANNEL_BLANKET_01'],'绒绒已离开，皮皮回到自家卧室。','皮皮回到自己的床边，绒毯仍收在藤篮内。'),
('p005_u06','p005_u08','各自在家都温暖','皮皮卧室','今天夜晚·暖光','皮皮在安静温暖的卧室里满足地看向自己的床；绒绒已回到自己的家，前镜已交代他有厚实的大熊棉被。',['pipi'],['LOC_PIPI_BEDROOM_01','CHAR_PIPI_01','PROP_WICKER_BASKET_01','PROP_FLANNEL_BLANKET_01','PROP_BED_01'],'承接皮皮回到床边；绒毯仍在藤篮。','两位朋友各在自己的家中安顿好，皮皮准备上床。'),
('p005_u09','p005_u11','萝卜玩偶在怀里','皮皮床上','今天夜晚·暖光','皮皮爬上自己熟悉的低木床，拉好暖黄色毛毯，把橙色胡萝卜玩偶抱近胸口；他神情松弛，长耳自然垂在枕边。',['pipi'],['LOC_PIPI_BEDROOM_01','CHAR_PIPI_01','PROP_BED_01','PROP_YELLOW_BLANKET_01','PROP_CARROT_PLUSH_01'],'皮皮已在卧室床上，使用自己的黄色毯子和胡萝卜玩偶。','皮皮被熟悉的床铺与玩偶温暖包围。'),
('p006_u01','p006_u02','不必重演昨天','皮皮卧室床边','今天夜晚·柔和暖光','皮皮已经躺在床上，视线温和落向床尾藤篮中折叠的米白绒毯，神情释然；没有把它再次拿到门廊，也没有雪景重演。',['pipi'],['LOC_PIPI_BEDROOM_01','CHAR_PIPI_01','PROP_WICKER_BASKET_01','PROP_FLANNEL_BLANKET_01','PROP_BED_01','PROP_YELLOW_BLANKET_01'],'米白绒毯继续收在篮里；皮皮已回到自己的床。','皮皮愿意珍藏昨天经历，而不需要重新安排同一场景。'),
('p006_u03','p006_u03','一段肩并肩的时光','记忆中的门廊','昨日下午·记忆','呈现昨天的同一门廊回忆：皮皮和绒绒在长椅上肩并肩看雪，原来那条米白绒毯仍平铺各盖一半；构图柔和安静，但保留真实水彩场景，不做拼贴或魔法光圈。',['pipi','rongrong'],['LOC_PORCH_01','CHAR_PIPI_01','CHAR_RONGRONG_01','PROP_BENCH_01','PROP_FLANNEL_BLANKET_01'],'这是皮皮心中的昨天回忆，时间明确回到昨日下午；重现此前共享毯子的正确状态。','最温暖的相伴时光留在记忆中，不改变当晚收纳状态。'),
('p006_u04','p006_u05','温暖留在心里','皮皮卧室床上','今天夜晚·柔和暖光','回到当前卧室，皮皮将一只爪轻轻放在胸口，脸上浮现安心的小小微笑；胡萝卜玩偶贴在胸前，暖黄被子盖好，床尾藤篮远处安静可见。',['pipi'],['LOC_PIPI_BEDROOM_01','CHAR_PIPI_01','PROP_BED_01','PROP_CARROT_PLUSH_01','PROP_YELLOW_BLANKET_01','PROP_WICKER_BASKET_01'],'从昨日回忆明确回到当前卧室；所有物件回到当前夜间位置。','皮皮感到那段温暖已经留在心里。'),
('p006_u06','p006_u07','呼吸慢慢均匀','皮皮卧室床上','今天夜晚·柔和暖光','皮皮闭上眼睛，安静地躺在枕边，长耳自然放松；黄毯与胡萝卜玩偶位置稳定，暖灯渐柔，呼吸绵长。',['pipi'],['LOC_PIPI_BEDROOM_01','CHAR_PIPI_01','PROP_BED_01','PROP_YELLOW_BLANKET_01','PROP_CARROT_PLUSH_01'],'皮皮由睁眼的释然转入闭眼休息。','皮皮安稳入睡，室内仍温暖宁静。'),
('p007_u01','p007_u03','朋友分享的快乐','记忆中的门廊','昨日下午·温暖回忆','再次呈现同一段快乐记忆：皮皮和绒绒肩并肩坐在雪后门廊长椅上，米白毯仍各盖一半，神情平静开心；时间是过去的回忆，不与当晚的入睡状态混淆。',['pipi','rongrong'],['LOC_PORCH_01','CHAR_PIPI_01','CHAR_RONGRONG_01','PROP_BENCH_01','PROP_FLANNEL_BLANKET_01'],'片尾寄语提到分享的时光，短暂回望昨天的共享画面。','以安静共享的温暖画面承接对听众的晚安祝愿。'),
('p007_u04','p007_u07','回到自己的暖被窝','皮皮卧室床上','今天夜晚·深蓝夜色','回到皮皮自己的床上，皮皮在暖黄毛毯下安心熟睡，胡萝卜玩偶抱在胸前，床尾藤篮和折叠米白绒毯远处可辨；窗外深蓝安静，最后留白渐暗。',['pipi'],['LOC_PIPI_BEDROOM_01','CHAR_PIPI_01','PROP_BED_01','PROP_YELLOW_BLANKET_01','PROP_CARROT_PLUSH_01','PROP_WICKER_BASKET_01','PROP_FLANNEL_BLANKET_01'],'当前时间回到夜晚；皮皮睡在自己的床和黄毯下，绒毯仍收好。','皮皮进入安睡尾声，最后4秒由渲染渐暗。'),
]
units=json.loads((OUT/'narration-units.json').read_text()); lookup={u['id']:u for u in units}; shots=[]; states=[]
for sid,(first,last,title,location,tod,action,chars,refs,before,after) in enumerate(G):
 ai=next(i for i,u in enumerate(units) if u['id']==first); bi=next(i for i,u in enumerate(units) if u['id']==last); selected=units[ai:bi+1]
 assert selected[0]['id']==first and selected[-1]['id']==last and len({u['paragraph_id'] for u in selected})==1,(sid,first,last)
 ranges=[{'unit_id':u['id'],'start_char':0,'end_char':len(u['text'])} for u in selected]; text=''.join(u['text'] for u in selected); p=selected[0]['paragraph_id']
 wardrobe='sleep_v001' if p in ('p005','p006','p007') and sid>=18 and '回忆' not in location else 'day_v001'
 charrefs={}
 if 'pipi' in chars: charrefs['pipi']=['references/pipi_identity_v001.png','references/pipi_sleep_wardrobe.png' if wardrobe=='sleep_v001' else 'references/pipi_day_wardrobe.png']
 if 'rongrong' in chars: charrefs['rongrong']=['references/rongrong_identity_v001.png']
 wardrobes={x:('sleep_v001' if x=='pipi' and wardrobe=='sleep_v001' else 'day_v001' if x=='pipi' else 'forest_green_v001') for x in chars}
 s={'id':sid,'paragraph_id':p,'source_ranges':ranges,'text':text,'title':title,'location':location,'time_of_day':tod,'layer':'storybook','characters':chars,'character_reference_manifest':'references/episode_cast.json','character_references':charrefs,'wardrobe_ids':wardrobes,'visual_direction':action,'action':action,'continuity_refs':refs,'state_before':before,'state_after':after,'transition_from':None if sid==0 else sid-1,'image_status':'planned','image_path':f'images/shot_{sid:02}.png','image':f'images/shot_{sid:02}.png'}
 shots.append(s); states.append({'shot_id':sid,'location':location,'time_of_day':tod,'characters_present':chars,'character_positions':action,'continuity_refs':refs,'state_before':before,'action':action,'state_after':after,'transition_from':None if sid==0 else sid-1})
assert ''.join(s['text'] for s in shots)==''.join(u['text'] for u in units)
plan={'episode':'ep046','title':'小熊借来的绒毯','cover_title':'皮皮借出绒毯','cover_title_lines':['皮皮借出','绒毯'],'theme':'分享后仍给彼此留足温暖','version':'v001','status':'draft_preflight_pending','shots':shots}
(OUT/'storyboard.draft.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n')
assets={
'CHAR_PIPI_01':{'kind':'character','fixed':'皮皮：暖灰毛、圆脸、粉色小鼻、自然下垂长耳。门廊访友时穿米色上衣、灰蓝短背带裤、蓝鞋；夜间睡衣和深蓝星星睡帽固定。','reference':'references/pipi_identity_v001.png'},
'CHAR_RONGRONG_01':{'kind':'character','fixed':'绒绒：体型宽厚、浅棕毛、奶油色口鼻、圆耳、友善小黑鼻；门廊穿深森林绿背心，柔和憨厚，不凶。','reference':'references/rongrong_identity_v001.png'},
'LOC_OPENING_01':{'kind':'location','fixed':'独立p000开场的雪日木门廊与长椅意象，无角色，不复用剧情图。','reference':'references/porch_scene_ref.png'},
'LOC_PORCH_01':{'kind':'location','fixed':'皮皮家固定木屋门廊；宽木长椅靠门廊栏杆，木门在后侧；昨日下午细雪，昨晚大雪，次日傍晚放晴，主要视角不反转。','reference':'references/porch_scene_ref.png'},
'LOC_PIPI_BEDROOM_01':{'kind':'location','fixed':'皮皮的暖木屋卧室；同一低木床和床尾位置，固定暖灯，床尾藤编篮常驻。','reference':'references/bedroom_scene_ref.png'},
'LOC_RONGRONG_HOME_01':{'kind':'location','fixed':'绒绒自己的暖木熊屋卧室，与皮皮家空间区分；仅用于归家后使用自家棉被的镜头。','reference':'shot_18_initial_scene'},
'PROP_BENCH_01':{'kind':'prop','fixed':'门廊同一宽木长椅；两位朋友并排坐，方向和椅子结构稳定。','reference':'references/porch_scene_ref.png'},
'PROP_FLANNEL_BLANKET_01':{'kind':'prop','fixed':'唯一一条厚实米白法兰绒毯，织绒细密、纯色无图案、矩形；半盖两人、借给绒绒、洗净折方归还、展开蓬松、再折好收进藤篮。','reference':'assets/prop_reference_board.png'},
'PROP_HOLLY_LEAF_01':{'kind':'prop','fixed':'一片干净鲜绿冬青叶，三枚尖裂叶缘和短柄；由绒绒放在折叠毯顶作为礼物，后从毯上取下放进浅色小碟。','reference':'assets/prop_reference_board.png'},
'PROP_DISH_01':{'kind':'prop','fixed':'浅色小陶碟，放置冬青叶；留在皮皮家门廊，不出现在卧室。','reference':'assets/prop_reference_board.png'},
'PROP_WICKER_BASKET_01':{'kind':'prop','fixed':'低矮圆口藤编篮，固定在皮皮卧室床尾；只收纳一条重新折好的米白绒毯。','reference':'assets/prop_reference_board.png'},
'PROP_BED_01':{'kind':'prop','fixed':'皮皮卧室同一低木床，位置固定。','reference':'references/bedroom_scene_ref.png'},
'PROP_YELLOW_BLANKET_01':{'kind':'prop','fixed':'皮皮平时盖的暖黄色床毯，仅用于皮皮卧室睡眠镜头。','reference':'assets/prop_reference_board.png'},
'PROP_CARROT_PLUSH_01':{'kind':'prop','fixed':'橙色柔软胡萝卜形玩偶，绿叶顶，皮皮睡前抱在胸口。','reference':'assets/prop_reference_board.png'},
'PROP_BEAR_QUILT_01':{'kind':'prop','fixed':'绒绒自己家使用的厚实深棕色大熊棉被；不与米白法兰绒毯混淆。','reference':'shot_18_initial_scene'}
}
cont={'episode':'ep046','version':'v001','assets':assets,'shot_states':states,'preflight':{'textual_passes':'passed_two_passes_before_image_generation','causal_review':'passed','prop_state_review':'passed','notes':['p000两张独立片头图，均不复用封面或剧情图。','米白法兰绒毯为唯一持续物件，清楚经历共享、借出、洗净归还、展开、折叠并收入卧室藤篮；没有跳回门廊或替换颜色。','冬青叶只在门廊由绒绒放置、皮皮取下后置于门廊小碟，不错误进入卧室。','绒绒离开后仅在自己家使用大熊棉被；皮皮卧室睡眠使用自己的黄毯和胡萝卜玩偶。','回忆镜明确标注过去的门廊状态，不改变当前夜间收纳状态。','季节时间由昨日下午细雪转昨晚大雪，再到今日傍晚放晴，最后回到夜晚。']}}
(OUT/'continuity.json').write_text(json.dumps(cont,ensure_ascii=False,indent=2)+'\n')
(OUT/'references/episode_cast.json').write_text(json.dumps({'episode':'ep046','characters':{'pipi':{'identity':'references/pipi_identity_v001.png','day_wardrobe':'references/pipi_day_wardrobe.png','sleep_wardrobe':'references/pipi_sleep_wardrobe.png'},'rongrong':{'identity':'references/rongrong_identity_v001.png','day_wardrobe':'official forest-green vest'}},'locations':{'porch':'references/porch_scene_ref.png','pipi_bedroom':'references/bedroom_scene_ref.png'},'identity_acceptance':'registry_approved_for_initial_production_use'},ensure_ascii=False,indent=2)+'\n')
print('DRAFT',len(shots),'shots; hanzi',sum(len(s['text']) for s in shots))
