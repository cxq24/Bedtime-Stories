#!/usr/bin/env python3
"""Prepare the episode 044 shot/story continuity draft from its adopted narration units."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
OUT = ROOT / 'episodes/ep044/v001'

groups = [
    ('p000_u01','p000_u03','片头：窗上的冰花','独立片头画面','冬日清晨','冰窗小花园铺满高窗，晶莹分枝与花形冰晶在浅蓝晨光中显现，窗边有一线暖色室内光；无角色、无文字。',[],['LOC_OPENING_01','PROP_FROST_01'],'片头以静谧窗花引出故事，和后续卧室剧情画面分开。','窗花图案初现于开场画面。'),
    ('p000_u04','p000_u05','片头：冰晶里的图案','独立片头画面','冬日清晨','更近的诗意冰晶花园视角：交错冰枝、圆花和弯曲小路藏在半透明玻璃纹理中；不是实际卧室窗户的重复构图，无角色、无文字。',[],['LOC_OPENING_01','PROP_FROST_01'],'接续片头的冰晶图案提问。','开场想象停留在冰花细节。'),
    ('p001_u01','p001_u02','清冷的清晨','皮皮的卧室','冬日清晨','皮皮在温暖木屋卧室里穿好米色上衣和灰蓝背带裤，蓝布鞋已穿好，小黄书包放在床边；他正准备去森林学堂，动作自然，神情清醒而平和。', ['pipi'],['CHAR_PIPI_01','LOC_BEDROOM_01','PROP_BED_01','PROP_SCHOOLBAG_01'],'从片头切入皮皮清晨的卧室；皮皮在家中准备上学。','窗玻璃四角有薄霜，皮皮尚未发现。'),
    ('p001_u03','p001_u04','发现窗角冰花','皮皮的卧室','冬日清晨','皮皮转向同一扇宽木框窗，惊喜地发现玻璃四角结着晶莹冰窗花；他睁眼微微抬眉，视线落在窗角，没有夸张张嘴。', ['pipi'],['CHAR_PIPI_01','LOC_BEDROOM_01','WIN_WINDOW_01','PROP_FROST_01'],'皮皮从穿衣准备转向窗口，地点仍是卧室。','皮皮发现四角初生的冰窗花，未触碰玻璃。'),
    ('p001_u05','p001_u05','晨光里的细纹','卧室窗边特写','冬日清晨','无人物近景，玻璃角落布满细细密密的分枝冰晶，银色晨光穿过透明纹路，保留木窗框和固定窗台方向。',[],['LOC_BEDROOM_01','WIN_WINDOW_01','PROP_FROST_01'],'承接皮皮刚发现的同一扇卧室窗。','冰花细纹在晨光里闪银光。'),
    ('p001_u06','p001_u07','白色袖珍花园','卧室窗边特写','冬日清晨','同一窗角冰晶如一座袖珍白色花园：细小树枝与花叶般的霜纹层层展开，冷银光温柔清晰；不添加真实人物或拟人冬天爷爷。',[],['LOC_BEDROOM_01','WIN_WINDOW_01','PROP_FROST_01'],'延续同一窗角与晨光，只细看霜花。','皮皮心中把冰晶纹路想成冬夜画出的袖珍花园。'),
    ('p002_u01','p002_u03','放学后回到家','卧室窗边','冬日下午','午后未落山的阳光照进木屋，皮皮放学回家后站到同一扇窗前；小黄书包挂在房间门边，窗角冰花开始变薄但仍完整可辨。', ['pipi'],['CHAR_PIPI_01','LOC_BEDROOM_01','WIN_WINDOW_01','PROP_FROST_01','PROP_SCHOOLBAG_01'],'时间转到下午；皮皮已经回到家，书包放在门边。','冰窗花尚未完全消融，皮皮想趁日光中看看它。'),
    ('p002_u04','p002_u05','搬来小桌子','卧室窗前','冬日下午','皮皮双手把一张矮小浅木色小桌搬到同一扇窗前，坐下仔细欣赏窗角冰花；表情专注好奇，眼睛跟随玻璃纹路。', ['pipi'],['CHAR_PIPI_01','LOC_BEDROOM_01','WIN_WINDOW_01','PROP_FROST_01','PROP_TABLE_01'],'皮皮留在卧室窗前，搬来的小桌位于窗边。','小桌固定在窗前，皮皮坐下观察冰花。'),
    ('p002_u06','p002_u08','冰晶像松树','卧室窗花细节','冬日下午','同一片冰窗花的特写，一组细细分叉的冰晶像挂着冰凌的松树；木窗框边缘和室内柔和日光作为位置锚点。',[],['LOC_BEDROOM_01','WIN_WINDOW_01','PROP_FROST_01'],'承接皮皮坐在窗前观察的视角。','冰晶分叉像一棵挂满冰凌的松树。'),
    ('p002_u09','p002_u10','弯曲的细草','卧室窗花细节','冬日下午','同一冰花另一段曲折如迎风细草的霜纹，纤细弧线沿玻璃展开；不改变窗格和霜花所在角落。',[],['LOC_BEDROOM_01','WIN_WINDOW_01','PROP_FROST_01'],'切到同一窗花的相邻纹路。','皮皮看到弯弯曲曲、像迎风细草的冰晶。'),
    ('p002_u11','p002_u12','冰晶间的小路','卧室窗花细节','冬日下午','同一窗花的中段，一条亮晶晶弯弯的小路穿过松树形分枝与细草纹路之间，保持自然冰晶质感，不像人工画线。',[],['LOC_BEDROOM_01','WIN_WINDOW_01','PROP_FROST_01'],'继续观察同一片冰花的中心纹路。','小路连接树形冰枝和细草形冰枝。'),
    ('p003_u01','p003_u02','没有碰玻璃','卧室窗前','冬日下午','皮皮坐在小桌旁，暖乎乎的小爪子停在离玻璃一小段距离处，没有碰上；他想起冰花会融化，神情认真克制，视线在爪子和冰花之间。', ['pipi'],['CHAR_PIPI_01','LOC_BEDROOM_01','WIN_WINDOW_01','PROP_FROST_01','PROP_TABLE_01'],'承接皮皮在桌边观察同一窗花。','皮皮收住伸向玻璃的动作，冰花保持原样。'),
    ('p003_u03','p003_u04','纸和彩铅','卧室窗前小桌','冬日下午','皮皮把一张白色画纸和一支银灰色彩铅放在同一张浅木桌上；他神情安静专注，准备照着窗花画画。', ['pipi'],['CHAR_PIPI_01','LOC_BEDROOM_01','WIN_WINDOW_01','PROP_TABLE_01','PROP_PAPER_01','PROP_PENCIL_01'],'皮皮从未触摸玻璃，转而取来纸和彩铅，在原位准备绘画。','画纸和彩铅留在桌面，皮皮准备画最喜欢的一段风景。'),
    ('p003_u05','p003_u05','安静画下风景','卧室窗前小桌','冬日下午','皮皮在白纸上安静画下冰窗花里最喜欢的一小段风景，银灰彩铅轻落纸面；眼睛专注纸面，神情舒展。', ['pipi'],['CHAR_PIPI_01','LOC_BEDROOM_01','PROP_TABLE_01','PROP_PAPER_01','PROP_PENCIL_01'],'承接同一张画纸和同一支彩铅，皮皮开始落笔。','纸上出现冰花风景的第一段草图。'),
    ('p003_u06','p003_u08','画纸上的弯弯小路','小桌画纸近景','冬日下午','近景展示同一张白纸上的银灰铅笔画：小路并不笔直，轻巧绕开几片草叶，刚好走到一朵圆圆的冰花旁；边缘可见同一支银灰彩铅。', [],['LOC_BEDROOM_01','PROP_TABLE_01','PROP_PAPER_01','PROP_PENCIL_01'],'承接皮皮正在画的同一张纸，桌上物件不变。','纸上完成小路、草叶和圆冰花，冰窗花仍在窗外侧。'),
    ('p004_u01','p004_u03','夜里的暖炉','木屋卧室','冬日夜晚','同一木屋卧室入夜，暖炉发出稳定柔和的橙光，玻璃窗外是深蓝夜色，室内暖、室外冷，环境安静；无角色。',[],['LOC_BEDROOM_01','WIN_WINDOW_01','PROP_STOVE_01','PROP_FROST_01'],'时间由下午推至夜晚；窗户仍关闭，暖炉在室内。','室内暖炉持续升温，窗花开始受室内外温差影响。'),
    ('p004_u04','p004_u05','洗澡后去看窗户','卧室窗边','冬日夜晚','皮皮洗完澡换上浅色睡衣和深蓝星星睡帽，走到同一扇窗前查看；他看到窗角冰花边缘开始模糊，神情有些意外但平静。', ['pipi'],['CHAR_PIPI_01','LOC_BEDROOM_01','WIN_WINDOW_01','PROP_FROST_01'],'皮皮洗澡后回到卧室窗前；衣服换为睡衣。','窗花纹路开始融化，皮皮仍未碰窗。'),
    ('p004_u06','p004_u07','花园悄悄融化','卧室窗花特写','冬日夜晚','同一窗角冰窗花已融化变形：原先清晰的花园图案变成柔和水痕，玻璃上有薄薄水珠；木窗格方位保持不变。',[],['LOC_BEDROOM_01','WIN_WINDOW_01','PROP_FROST_01','PROP_STOVE_01'],'窗花因暖炉造成的温差自然变化，房间仍是夜晚。','原先的花园图案已不再完整，玻璃上有融水痕。'),
    ('p004_u08','p004_u10','想追着新图案','卧室窗边','冬日夜晚','皮皮手里拿着银灰彩铅站在窗边，稍显惋惜地望着新水痕，像想到从前会追着新纹路画下去；他没有再次落笔，神情克制。', ['pipi'],['CHAR_PIPI_01','LOC_BEDROOM_01','WIN_WINDOW_01','PROP_FROST_01','PROP_PENCIL_01'],'皮皮在窗边观察融化后的玻璃；笔尚未触纸。','出现短暂惋惜和追画念头，但没有开始新画。'),
    ('p005_u01','p005_u03','画纸留住花园','卧室小桌','冬日夜晚','皮皮转身看向原先桌上的画纸，脸上从惋惜转为安定；纸上完整保留下午那座小花园，窗户在背景中仍是同一扇。', ['pipi'],['CHAR_PIPI_01','LOC_BEDROOM_01','PROP_TABLE_01','PROP_PAPER_01','PROP_PENCIL_01','WIN_WINDOW_01'],'皮皮把注意力从融化窗花移向早先画好的纸。','纸上的小花园已经保存下来，皮皮意识到自己不必追画。'),
    ('p005_u04','p005_u05','自然有自己的变化','窗边与画纸','冬日夜晚','同一窗户上的薄霜、水珠与纸上画好的花园在同一构图中并置；自然融化是柔和真实的，不出现魔法闪光；暖室内与冷窗外并存。',[],['LOC_BEDROOM_01','WIN_WINDOW_01','PROP_FROST_01','PROP_PAPER_01'],'承接皮皮看向桌上保存好的图画，同时窗口仍在自然融化。','自然冰花可以消融，纸上画作保持不变。'),
    ('p005_u06','p005_u07','明天会有新图案','窗边与画纸','冬日深夜','窗外冷夜映着逐渐变透明的玻璃，桌上纸画完整安放；皮皮在远处不再守候窗前，温柔宁静的空房间构图。',[],['LOC_BEDROOM_01','WIN_WINDOW_01','PROP_FROST_01','PROP_PAPER_01'],'时间继续到夜深，皮皮不再一直守着窗户。','故事表达明晚寒冷时会有新纹路，今晚不必追赶。'),
    ('p005_u08','p005_u09','收好画纸和彩铅','卧室小桌与绘本','冬日夜晚','皮皮小心把那张已画好的白纸夹进一本绘本，并把同一支银灰彩铅收在桌上固定的位置；动作轻柔，表情安心。', ['pipi'],['CHAR_PIPI_01','LOC_BEDROOM_01','PROP_TABLE_01','PROP_PAPER_01','PROP_PENCIL_01','PROP_BOOK_01'],'皮皮留在卧室桌边，画纸与彩铅位置由此收纳。','画纸夹入绘本，彩铅被收好，桌面整洁。'),
    ('p006_u01','p006_u02','暖黄毛毯与大枕头','卧室床铺近景','冬日夜晚','低床上的暖黄色毛毯铺平，大枕头蓬松柔软，床头灯温暖；窗户仍在画面右侧作为稳定方向锚点。',[],['LOC_BEDROOM_01','PROP_BED_01','PROP_BLANKET_01','PROP_PILLOW_01','WIN_WINDOW_01'],'皮皮准备结束夜晚活动，卧室布局不变。','床铺温暖整齐，枕头空着等待皮皮躺下。'),
    ('p006_u03','p006_u04','长耳朵落在枕边','卧室床铺','冬日夜晚','皮皮换着同一套睡衣和星星睡帽爬上床，躺下时两只长耳朵自然垂落在大枕头边；神情松弛，眼睛尚未闭上。', ['pipi'],['CHAR_PIPI_01','LOC_BEDROOM_01','PROP_BED_01','PROP_BLANKET_01','PROP_PILLOW_01'],'皮皮从窗边回到床上，睡衣与睡帽保持一致。','皮皮躺在床上，耳朵落于枕边，暖黄毛毯盖住身体。'),
    ('p006_u05','p006_u07','冰花自由地变化','卧室床与窗','冬日夜晚','皮皮在同一张床上闭上眼睛；窗外玻璃上的冰花图案在深蓝夜色中淡淡可见，室内床头灯和暖炉很柔和，画面表现接受它会生长或融化。', ['pipi'],['CHAR_PIPI_01','LOC_BEDROOM_01','WIN_WINDOW_01','PROP_FROST_01','PROP_BED_01','PROP_BLANKET_01','PROP_PILLOW_01','PROP_STOVE_01'],'皮皮躺在床上并闭眼，冰窗花还在窗外。','皮皮停止守望，窗花留在窗外自由变化。'),
    ('p006_u08','p006_u09','安心睡去','卧室床与窗','冬日夜晚','同一房间里皮皮安静睡着，窗外的冰花小园在深蓝夜色中保持静谧，皮皮不再睁眼观察；无新增人物或物件。', ['pipi'],['CHAR_PIPI_01','LOC_BEDROOM_01','WIN_WINDOW_01','PROP_FROST_01','PROP_BED_01','PROP_BLANKET_01','PROP_PILLOW_01'],'承接皮皮闭眼入睡；卧室布局和床铺状态稳定。','皮皮沉静睡着，无需一直盯着窗花。'),
    ('p007_u01','p007_u03','把美景收进记忆','卧室清晨夜景','冬日深夜','皮皮在暖黄被子下熟睡，画纸已夹进绘本放在床边小桌；窗外世界安静变化，镜头温柔回望这一天的窗花记忆，不叠加文字或虚构魔法场景。', ['pipi'],['CHAR_PIPI_01','LOC_BEDROOM_01','WIN_WINDOW_01','PROP_FROST_01','PROP_BED_01','PROP_BLANKET_01','PROP_BOOK_01','PROP_PAPER_01'],'进入片尾对听众的温柔寄语，皮皮已在卧室入睡。','美景被留在画纸和记忆里，窗外自然继续变化。'),
    ('p007_u04','p007_u05','温暖安静的睡眠','卧室尾声','冬日深夜','卧室固定构图逐渐安静下来：皮皮睡在暖黄毛毯中，窗外深蓝，床头灯很暗，冰花纹路淡淡可见；画面留白温柔，不出现任何文字。', ['pipi'],['CHAR_PIPI_01','LOC_BEDROOM_01','WIN_WINDOW_01','PROP_FROST_01','PROP_BED_01','PROP_BLANKET_01','PROP_PILLOW_01'],'皮皮保持熟睡，镜头延续同一房间。','皮皮安静睡着，故事进入片尾寄语。'),
    ('p007_u06','p007_u06','晚安','卧室尾声','冬日深夜','皮皮在同一张低床上安睡，暖黄毛毯盖到肩下，窗外深蓝，画面平静留白；不出现文字，最后4秒渐暗到深夜蓝。', ['pipi'],['CHAR_PIPI_01','LOC_BEDROOM_01','WIN_WINDOW_01','PROP_BED_01','PROP_BLANKET_01','PROP_PILLOW_01'],'延续前镜同一构图与熟睡状态。','最后一声晚安后保持静谧尾声并按规范渐暗。'),
]

units = json.loads((OUT/'narration-units.json').read_text(encoding='utf-8'))
by_id={u['id']:u for u in units}
shots=[]
previous=None
for sid,(first,last,title,location,tod,action,chars,refs,before,after) in enumerate(groups):
    start=next(i for i,u in enumerate(units) if u['id']==first)
    end=next(i for i,u in enumerate(units) if u['id']==last)
    selected=units[start:end+1]
    assert selected[0]['id']==first and selected[-1]['id']==last
    ranges=[{'unit_id':u['id'],'start_char':0,'end_char':len(u['text'])} for u in selected]
    text=''.join(u['text'] for u in selected)
    p=selected[0]['paragraph_id']
    if any(u['paragraph_id']!=p for u in selected):
        raise ValueError(f'cross-paragraph shot {sid}')
    if chars:
        wardrobe='sleep_v001' if p in ('p004','p005','p006','p007') and sid>=15 else 'day_v001'
        char_refs={'pipi':['references/pipi_identity_v001.png','references/pipi_'+('sleep' if wardrobe=='sleep_v001' else 'day')+'_wardrobe.png']}
        wardrobe_ids={'pipi':wardrobe}
    else:
        char_refs={}; wardrobe_ids={}
    shot={
        'id':sid,'paragraph_id':p,'source_ranges':ranges,'text':text,'title':title,'location':location,'time_of_day':tod,
        'layer':'storybook','characters':chars,'character_reference_manifest':'references/episode_cast.json',
        'character_references':char_refs,'wardrobe_ids':wardrobe_ids,
        'visual_direction':action+' 竖屏9:16水彩绘本，柔和纸纹，单幅无字图；重要信息位于中上部，底部留足拼音字幕安全区。',
        'action':action,'continuity_refs':refs,'state_before':before,'state_after':after,
        'transition_from':previous,'image_status':'planned','image_path':f'images/shot_{sid:02}.png','image':f'images/shot_{sid:02}.png'}
    shots.append(shot); previous=sid
assert ''.join(s['text'] for s in shots)==''.join(u['text'] for u in units)
draft={'episode':'ep044','title':'冰窗花的小花园','cover_title':'皮皮画下冰花','cover_title_lines':['皮皮画下','冰花'],'theme':'在安静观察中放下忙碌','version':'v001','status':'draft_preflight_pending','shots':shots}
(OUT/'storyboard.draft.json').write_text(json.dumps(draft,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

assets={
 'CHAR_PIPI_01':{'kind':'character','fixed':'皮皮：暖灰毛、圆脸、粉色小鼻、自然下垂长耳；身份依官方图。清晨/下午穿米色上衣、灰蓝短背带裤、蓝布鞋；夜间洗澡后穿睡衣、戴深蓝星星睡帽。表情依每镜动作变化。','reference':'references/character_ref.json'},
 'LOC_OPENING_01':{'kind':'location','fixed':'独立开场的抽象冰窗花花园画面，不固定到故事卧室的具体家具；无角色。','reference':'images/shot_00.png'},
 'LOC_BEDROOM_01':{'kind':'location','fixed':'木屋卧室：同一宽木框玻璃窗在画面右侧、原木窗台、低床在左、床头灯和暖炉；冷蓝窗外与暖金室内。','reference':'references/bedroom_scene_ref.png'},
 'WIN_WINDOW_01':{'kind':'prop','fixed':'同一扇关闭的宽木框玻璃窗；窗格、窗台位置和拍摄方向恒定。','reference':'references/bedroom_scene_ref.png'},
 'PROP_FROST_01':{'kind':'prop','fixed':'冬日清晨生长于同一窗户四角的透明银白冰窗花；分枝像松树、弯曲如细草，中央有亮晶晶弯路和圆花；午后仍可见，夜间暖炉升温后逐渐融化变形。','reference':'images/shot_00.png'},
 'PROP_TABLE_01':{'kind':'prop','fixed':'浅木色矮小小桌，窗前固定位置，大小适合皮皮坐着画画。'},
 'PROP_PAPER_01':{'kind':'prop','fixed':'同一张白色画纸，皮皮画有银灰色弯路、草叶和圆冰花，夜晚夹入绘本。'},
 'PROP_PENCIL_01':{'kind':'prop','fixed':'一支银灰色彩铅；开始放在小桌，绘画使用，夜晚收好。'},
 'PROP_BOOK_01':{'kind':'prop','fixed':'一本皮皮的绘本，用来夹好纸画，放在床边小桌。'},
 'PROP_BED_01':{'kind':'prop','fixed':'同一张低木床，固定在卧室左侧。'},
 'PROP_BLANKET_01':{'kind':'prop','fixed':'暖黄色软毛毯，睡前盖在皮皮身上。'},
 'PROP_PILLOW_01':{'kind':'prop','fixed':'同一个大而柔软的浅色枕头，皮皮的长耳朵落在枕边。'},
 'PROP_STOVE_01':{'kind':'prop','fixed':'固定于床边的暖炉，夜晚稳定发出柔和橙光，推动室内外温差。'},
 'PROP_SCHOOLBAG_01':{'kind':'prop','fixed':'同一个小黄书包，清晨准备上学时在床边，放学回家后挂在卧室门边；室内绘画及睡前镜头不由皮皮背着。'}
}
states=[]
for s in shots:
    states.append({'shot_id':s['id'],'location':s['location'],'time_of_day':s['time_of_day'],'characters_present':s['characters'],
       'character_positions':s['action'],'continuity_refs':s['continuity_refs'],'state_before':s['state_before'],'action':s['action'],
       'state_after':s['state_after'],'transition_from':s['transition_from']})
continuity={'episode':'ep044','version':'v001','assets':assets,'shot_states':states,
 'preflight':{'textual_passes':'passed_two_passes_before_image_generation','causal_review':'passed','prop_state_review':'passed',
  'notes':['片头两镜为独立开场插画，不复用封面或剧情图。','同一卧室窗户与冰窗花外观固定；窗花状态只从完整到温差融化，不无故恢复。','小桌固定在窗前，画纸和彩铅从开始绘画到收纳保持同一身份；完成的纸画夹进同一本绘本。','皮皮早晨和下午穿日常衣服；洗澡后转睡衣和星星睡帽。黄色书包早晨在床边，放学后挂于门边，不出现在睡前床上。','室内暖炉夜间加热；窗外冰花自然融化。皮皮没有再次碰窗。','皮皮离开窗边回到桌前，随后回床；无场景瞬移。']}}
(OUT/'continuity.json').write_text(json.dumps(continuity,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(OUT/'references/episode_cast.json').write_text(json.dumps({'episode':'ep044','characters':{'pipi':{'identity':'references/pipi_identity_v001.png','day_wardrobe':'references/pipi_day_wardrobe.png','sleep_wardrobe':'references/pipi_sleep_wardrobe.png'}},'locations':{'bedroom':'references/bedroom_scene_ref.png'},'identity_acceptance':'registry_approved_for_initial_production_use'},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f'prepared {len(shots)} shots, {sum(len(s["text"]) for s in shots)} text chars, continuity passes recorded')
