# 第026集《水壶旁的小云》制作记录

版本：v001｜稿源：用户长稿 v5 JSON｜制作日期：2026-11-16（北京时间）

## 已完成

- 全文763字，含v5专属p000开场；使用晓晓 zh-CN-XiaoxiaoNeural（-35%、-2Hz、+0%），配音真实长度276.40秒，未删文、未整体变速。
- 按TTS词边界锁定29镜，镜头固定图、25fps，画面最长可见15.00秒（含叠化）。
- 逐字拼音字幕130条，覆盖763/763汉字；上下排版与分段文件已生成。
- `continuity.json`记录文字预检和29镜联系表复核；最后一句后保留8秒无字幕尾声。

## 制作阶段

| 阶段 | 状态 | 证据 |
| --- | --- | --- |
| v5剧本与口播 | 通过 | `script.snapshot.json`、`narration-units.json` |
| 配音 | 已合成，待完整听审 | `audio/source/`、`audio/voice.wav`、`voice-timeline.json` |
| 分镜与配音校准 | 通过 | `storyboard.json`、`正式分镜.md`、`character-alignment.json` |
| 连续性检查 | 通过 | `continuity.json`、`checks/storyboard_contact.jpg`；29幅剧情图无重复 |
| 拼音字幕 | 字级覆盖100%；发音听审待做 | `subtitles.ruby.json`、`episode.ass`、`episode.srt`、`拼音核对表.md` |
| 逐镜插画与封面 | 完成 | 29张独立镜头图与独立封面已生成；来源和实际参考图清单已记录 |
| 渲染与技术检查 | 通过 | 两版视频完整解码；规格、帧数、字幕覆盖、时长与音轨检查通过，见`checks/technical-report.json` |
| 完整人工听看 | 待审 | 尚未认证 |
| 用户验收 | 待审 | 尚未记录 |
| 平台发布/GitHub同步 | 未发布/未同步 | 本次未执行 |

已输出`Outputs/2026-11-16/ep026-v001/`中的有字幕版、无字幕版、封面及发布文案。完整人工听看和用户验收待审；尚未发布或同步GitHub。
