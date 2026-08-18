# Creator OS Video Agent

## 定位

Creator OS 视频智能体执行层。

目标：让 AI Agent 理解视频素材、规划剪辑、调用工具、生成作品。

## 核心理念

不是剪辑软件，而是视频创作基础设施。

```
Creator OS
    |
Video Agent
    |
理解 -> 规划 -> 执行 -> 渲染
```

## 当前阶段

MVP：输入视频，输出自动剪辑方案与成片。

## 核心能力

- Video Understanding
- Director Agent
- Editor Agent
- MCP Tool Gateway
- Timeline Engine
- FFmpeg Render Pipeline

## 架构关系

- omnipotent-director: 导演规划
- creator-os-video-agent: 视频执行
- audio-transcriber-tts: 声音能力
- music-studio: 音乐能力
