# MCP Tool Specification

## 设计目标

让任何 Agent 可以控制视频生产能力。

## Tools

```json
{
 "create_project": "创建视频项目",
 "import_media": "导入素材",
 "analyze_video": "分析视频",
 "cut_clip": "裁剪片段",
 "merge_clip": "合并片段",
 "add_caption": "添加字幕",
 "add_music": "添加音乐",
 "export_video": "导出视频"
}
```

## 原则

Agent 不操作 UI。

Agent 修改结构化 Timeline 数据。
