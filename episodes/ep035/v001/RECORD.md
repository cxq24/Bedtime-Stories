# 第035集制作记录

- 制作版本：v001；日期（北京时间）：2026-11-23。
- 状态：成片已渲染，技术检查通过；人工完整听看未认证；用户验收待审；平台未发布。
- 稿源：`02_100集剧本/用户长稿v5/结构化JSON/ep035.json`，SHA-256 `04700faf5334a19a3ba5ff18d951276596758ee413d4e907a89505921b676122`；采用v5，746字，narration_sha256 `14251d3766aa20c8a9561d44a7d04198d1fc3c8502d370aea36abae9e419a49e`。剧本快照见`script.snapshot.json`。
- 配音：晓晓`zh-CN-XiaoxiaoNeural`，rate=-35%、pitch=-2Hz、volume=+0%、48kHz；全文合成，无删减或拉伸；时长261.04秒，完整时间线`voice-timeline.json`，生成音频单位MP3缓存记录见`audio/source/`。
- 混音：48kHz单声道；原始合成音乐和低电平环境底，无第三方采样；峰值voice 0.566/mix 0.575，未见削波。
- 分镜：27镜，25fps，0.96秒叠化，按真实配音边界锁定；最长可见镜头14.68秒。连续性两轮文字检查与全片联系表复核通过，图像/来源见`continuity.json`、`checks/contact_sheet_27shots.jpg`、`prompts/shot_prompts.json`。
- 角色/物件：白天皮皮沿用day_v001；栗栗、绒绒使用图库身份参考。夜间采用本集浅蓝睡衣造型，镜头08–26保持一致。布袋、栗子、矮桌、矮柜状态已逐镜核查。
- 开场：p000独立安排2镜及专属插画，并已进入口播、字幕和时间轴。
- 字幕：128条短语，746/746汉字带调拼音，逐字时间来自Edge TTS word-boundary；文本语境校核覆盖“板栗林、栗栗、数一数、抽绳、手腕”等词。完整音频发音人工听辨未认证。ASS为烧录源，SRT提供兼容稿；见`episode.ass`、`episode.srt`、`pinyin-review.json`。
- 封面：独立1080×1920 PNG，主标题“皮皮收好栗子”，依语义断行为“皮皮收好 / 栗子”；封面底图无字，360px检查通过；提示词和源图见`cover_base.png`、`cover.svg`、`prompts/cover.source.json`。
- 三平台文案：抖音、小红书、微信视频号的标题均与封面一致；正文有具体第一人称感受、开放问题和相关标签，见`发布文案.md`。
- 渲染：发布版`Outputs/2026-11-23/ep035-v001/ep035.mp4`；无字幕母版`ep035_clean.mp4`；均H.264/AAC、1080×1920、25fps、48kHz单声道，261.04秒，完整ffmpeg解码通过。完整规格/解码证据见`checks/final_technical_check.json`。
- 人工完整听看：未执行/未认证。用户验收：待审。平台发布：未发布。
- GitHub同步：已按用户本次要求准备同步到`cxq24/Bedtime-Stories`的`main`分支及`Outputs/2026-11-23/ep035-v001/`；同步提交号待完成后补记。
