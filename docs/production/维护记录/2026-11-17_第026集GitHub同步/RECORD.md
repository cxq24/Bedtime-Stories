# 第026集 GitHub 同步记录

- 日期：2026-11-17（UTC）。
- 目标仓库：`origin` → `https://github.com/cxq24/Bedtime-Stories.git`，目标分支 `main`。
- 用户请求：上传第026集视频到GitHub。
- 载荷范围：`episodes/ep026/v001/` 完整制作工程、`Outputs/2026-11-16/ep026-v001/` 封面与发布文本，以及主控和状态文件。视频最初被根目录`.gitignore`规则排除，后由补充提交明确加入。
- 视频规格：两版1080×1920、25fps、H.264/AAC、48kHz、276.40秒，6910帧；完整解码与技术检查通过。视频文件约53.0MiB和50.2MiB，均小于GitHub 100MiB单文件限制。已核实两文件均出现在远端`main`树的交付目录中。
- 工程提交：`d4353ec`（`Add episode 026 full production and delivery`），建立在当时远端提交`158f6a8`之上。
- 视频补传提交：`5db847b`（`Add episode 026 video files to delivery`），将`ep026.mp4`和`ep026_clean.mp4`明确写入Git；交付页现列出两版视频的链接。
- 连续性与文字检查：29张独立镜头图；763字口播、130条拼音字幕覆盖一致；联系表和成片技术检查通过。
- 完整人工听看尚未认证，用户验收待审，平台未发布。
