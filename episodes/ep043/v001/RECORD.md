# 第43集制作记录

- 制作规范：CHANNEL_MASTER、EPISODE_WORKFLOW、STORYBOARD_SPEC、VOICE_PROFILE、SUBTITLE_SPEC、VIDEO_SPEC、COVER_SPEC、PUBLISH_COPY_SPEC。
- 集数/版本：第43集《围巾留一小截》v001，2026-11-26（北京时间）。
- 唯一稿源：`02_100集剧本/用户长稿v5/结构化JSON/ep043.json`，779汉字，全文快照见`script.snapshot.json`。
- 配音：zh-CN-XiaoxiaoNeural，rate=-35%、pitch=-2Hz、volume=+0%，48kHz单声道；72个TTS短句单元，实测口播284.84秒，末尾静音8秒，计划总时长292.84秒。
- 分镜：33镜，真实音频锁定；含叠化最长可见时长14.04秒。源范围、状态、台词、服装和物件记录见`storyboard.json`、`continuity.json`。
- 图片：33张独立剧情图、原图尺寸941×1672；全片接触表见`checks/contact_sheet_33shots.jpg`。去除误入夜景的书包并修正围巾不遮口鼻。最终图像连续性审查通过。
- 角色/道具参考见`references/`；同一赤陶红绞花围巾`PROP_SCARF_01`从绕紧、松开到衣帽架上左长右短全程一致。
- 拼音：`episode.ass`、`episode.srt`、`subtitles.ruby.json`和`pinyin-review.json`；138条短语字幕，覆盖779/779汉字。多音字按上下文校对；完整配音发音听审未认证。
- 封面：1080×1920，独立标题版式“皮皮松开围巾”；底图取自本集松围巾插画`images/shot_15.png`，编辑源`cover.svg`。
- 三平台文案：`发布文案.md`，三个标题与封面逐字一致，正文含具体第一人称感受、开放问题和标签。
- 技术检查：发布版与母版完整解码通过；H.264/AAC、1080×1920、25fps、292.84秒规格正确；混音峰值0.541未削波；末条字幕于283.80秒清除，尾段无字幕。手机缩至360px抽查了样片与90/132/170/220/283/288秒画面，封面手机尺寸通过。
- 完整人工听看：未认证。用户验收：待审。平台发布：未发布。
- 仓库同步：已按用户要求同步完整工程和交付（含两版视频）到GitHub `cxq24/Bedtime-Stories` main；内容提交`aac6a0cac371f9f2e0734a1a4d4c7ed1cad65954`。GitHub接收成功，两视频均超过50MB建议值但小于100MB硬限制。
- 视频文件：`Outputs/2026-11-26/ep043-v001/ep043.mp4`（61,372,636字节）；`ep043_clean.mp4`（58,068,836字节）。
