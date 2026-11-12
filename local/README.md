# 当前制作工具入口

新集剧本统一采用v5，唯一JSON源在`02_100集剧本/用户长稿v5/结构化JSON/`。旧版剧本导出器已从当前工具集移除。

- `export_opening_scripts.py --validate-only`：校验100集v5 JSON、开场标记、逐集摘要和片头独立配图要求。
- `export_opening_scripts.py --output-dir <02_100集剧本/阅读与审校下的v5目录>`：从唯一JSON源导出合集、片头清单、100份单集Markdown和一致性报告。
- `cloud_preflight.py`：检查云端制作依赖、v5稿源、角色参考素材及004基准工程；不调用TTS或图片生成，不渲染视频。
- `setup_cloud.sh`：准备云端Python和系统依赖。

视频制作按`CHANNEL_MASTER.md`、`云端接手.md`及`docs/production/EPISODE_WORKFLOW.md`执行。历史单集目录中的工具快照仅用于解释对应版本，不覆盖`local/`当前工具。
