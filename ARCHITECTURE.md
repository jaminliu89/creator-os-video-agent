# Architecture

```
Creator OS
   |
Director Agent
   |
Video Agent
   |
----------------
|      |        |
Vision Timeline Render
|      |        |
AI     JSON    FFmpeg
```

## 核心原则

1. Agent 负责决策
2. 工具负责执行
3. Timeline 是中间协议
4. 渲染引擎独立

## 与其他项目

- omnipotent-director: 创作决策
- creator-os-video-agent: 视频执行
- MCN-Matrix-Content-Engine: 分发运营
