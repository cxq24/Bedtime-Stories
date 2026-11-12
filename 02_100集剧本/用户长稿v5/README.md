# 用户长稿 v5｜逐集开场版

2026-11-12。v5以用户长稿v4为正文底稿，为001–100每集新增一段点明本集标题和主题的专属口播开场。原有故事正文逐字保留；v4目录继续作为历史版本。

## 稿源

- `结构化JSON/ep001.json`至`ep100.json`是v5唯一改稿源。
- [100集片头文案清单](../阅读与审校/用户长稿v5开场优化_v001/100集片头文案.md)可快速审阅所有开场；完整阅读稿见同目录下的导出合集。
- 每集新增段落 `p000`，位于原正文之前；口播、配音、字幕和时间轴均需包含此段。
- 每段均有 `kind: opening_introduction` 和 `illustration_requirement: standalone`。片头必须单独制作一张插画，不得拿封面或第一张剧情图复用。
- 001–003仍标为短稿参考，004–100保留用户长稿完整正文。此前已完成的v001媒体和快照仍按v4记录，未被本次稿件更新改写。
- 修改后导出阅读稿并运行一致性检查：
  `python3 local/export_opening_scripts.py --validate-only`
  `python3 local/export_opening_scripts.py --output-dir <02_100集剧本/阅读与审校下的新目录>`

## 制作要求

配音继续使用晓晓rate=-35%／pitch=-2Hz／volume=+0%；不设五分钟上限，不删正文或拉伸音频。制作时先将片头作为独立镜头规划，实测配音后校准时间，再为片头生成独立水彩插画；详细流程见`docs/production/STORYBOARD_SPEC.md`。
