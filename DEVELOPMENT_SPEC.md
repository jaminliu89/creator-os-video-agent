# AI Video Agent Plugin 开发规范

## 1. 项目定位

AI Video Agent Plugin 是一个通用视频能力插件，不是剪辑软件，不做 UI 编辑器。

目标：

让任何支持 Agent 的系统通过 MCP 调用视频处理能力。

核心能力：

- 视频理解
- 视频转录
- 高价值片段识别
- 自动切片
- 字幕生成
- 视频渲染

---

# 2. MVP 目标

唯一目标：

> 输入一个长视频，Agent 自动生成多个可发布短视频。

输入：

```
interview.mp4
```

输出：

```
clip_001.mp4
clip_002.mp4
clip_003.mp4
```

每个视频包含：

- 精彩片段
- 自动字幕
- 基础格式转换

---

# 3. 开发原则

## 必须遵守

1. 优先完成闭环，不追求功能数量。
2. 所有能力必须可以被 Agent 调用。
3. MCP Tool 是核心接口。
4. 模块化设计，未来支持外部编辑器 Adapter。

## 当前禁止

- 不开发完整剪辑器
- 不开发 SaaS 平台
- 不开发复杂特效系统
- 不复制剪映

---

# 4. 技术架构

```
Agent
 |
MCP Server
 |
Video Intelligence Layer
 |
Editing Engine
 |
FFmpeg Renderer
 |
Output Video
```

---

# 5. 模块开发顺序

## Phase 1 视频理解

目标：让 AI 看懂视频。

实现：

- 视频读取
- 音频提取
- Whisper 转录
- 场景检测
- 元数据分析

输出：

video_analysis.json

---

## Phase 2 内容分析 Agent

目标：找到值得剪辑的位置。

输入：

```
transcript
+ video metadata
```

输出：

```json
{
 "highlights": [
  {
   "start":120,
   "end":160,
   "reason":"情绪高潮"
  }
 ]
}
```

---

## Phase 3 MCP Tools

第一版工具：

```
analyze_video
transcribe_video
find_highlights
create_clip
generate_caption
render_video
```

所有工具必须：

- 输入明确
- 输出结构化 JSON
- 可被 Agent 调用

---

## Phase 4 视频生成

使用：

- FFmpeg
- 字幕引擎

完成：

- 视频裁剪
- 合并
- 字幕烧录
- 格式转换

---

# 6. Agent 开发任务说明

接手开发 Agent 必须先阅读：

```
README.md
PRD.md
DEVELOPMENT_CONTRACT.md
MASTER_TASK.md
DEVELOPMENT_SPEC.md
```

禁止自行改变项目定位。

---

# 7. MVP 验收标准

必须完成：

输入：

一个 30-60 分钟视频。

系统自动：

1. 转文字
2. 分析内容
3. 找出三个高潮
4. 自动剪辑
5. 添加字幕
6. 输出短视频

达到以上标准才进入下一阶段。

---

# 8. 后续扩展

未来支持：

- ChatCut Adapter
- Palmier Adapter
- CapCut Adapter
- Premiere Adapter
- Resolve Adapter

但 MVP 阶段不实现。
