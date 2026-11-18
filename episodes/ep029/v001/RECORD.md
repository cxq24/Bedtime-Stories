# 第029集《雾抱了抱小篱笆》v001制作记录

- 稿源：`02_100集剧本/用户长稿v5/结构化JSON/ep029.json`，保存快照 `script.snapshot.json`。完整口播723个汉字（不含标点）。
- 配音：已用Edge TTS `zh-CN-XiaoxiaoNeural`、`-35%/-2Hz/+0%` 合成；23段，48kHz，实际时长248.36秒。句级MP3与WordBoundary元数据均已保存。尚未完成逐句听审。
- 分镜：按真实TTS词边界锁定33镜，覆盖完整口播，含叠化可见时长最长11.00秒。
- 连续性：已建立固定物件和场景草案；文字状态的逐镜审查尚未完成，不能标记通过。
- 插画：已生成2张候选插画：片头 `images/shot_02.png`、篱笆雾景 `images/shot_06.png`，使用皮皮身份参考。其余32张剧情图未生成。
- 拼音：按音频时间生成初稿（完整覆盖），人工听音和逐字复核待做。
- 封面、成片渲染、技术检查：未开始。人工完整听看、用户验收与发布均未记录。

## 云端预检

`local/setup_cloud.sh` 完成。`local/cloud_preflight.py` 执行失败：脚本对素材索引中的历史MP4路径触发断言；错误详情保留于本次会话。该异常未影响本集Edge TTS合成。

## 文件入口

- `voice.wav`、`voice-timeline.json`、`audio/source/`：配音与词边界
- `storyboard.json`、`storyboard.draft.json`、`正式分镜.md`：实测分镜
- `continuity.json`：固定物件及跨镜状态草案
- `images/shot_00.png`及`.source.json`：已生成片头候选及来源
- `subtitles.ruby.json`、`episode.ass`、`episode.srt`、`pinyin-review.json`：拼音字幕初稿
- `PRODUCTION_STATE.json`：机器可读阶段状态

## 仓库同步

2026-11-18，按用户指示将当前v001工程文件推送到GitHub `main`，提交 `ff86496`。同步范围为本目录现有全部69个文件（含配音WAV、句级MP3、两张插画与制作资料）；当前尚无渲染视频。
