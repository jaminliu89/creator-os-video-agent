# Agent Handoff

## 开发 Agent 必读
开始开发前必须阅读：
- `DEVELOPMENT_CONTRACT.md`
- `PRD.md`
- `ARCHITECTURE.md`
- `MASTER_TASK.md`
- `schemas/director-timeline.v1.schema.json`
- `docs/benchmarks/MONEYPRINTERTURBO_CAPTURE.md`
- `docs/DEPLOYMENT_VS_DIRECTOR_DIAGNOSIS.md`

## 当前唯一主线
不要继续扩散新的剪辑概念。当前主线是把已经存在的 Director / MG / Provider 能力闭成一个真实运行链路：

`Transcript → Beat Graph / Director IR → Visual Decision → Director Timeline → Pipeline IR → Providers → Render → QA → Evidence`

## 当前执行任务
1. 让现有 Director/Beat 输出生成有效的 `director-timeline.json`；
2. 校验其符合 `schemas/director-timeline.v1.schema.json`；
3. Pipeline Compiler 必须从 Director Timeline 生成 edit / motion / asset / audio jobs；
4. 增加至少一个本地或零成本 Asset Adapter/fixture 路径；
5. 用同一份逐字稿生成 Neutral 与 Directed 两版真实视频；
6. 输出时间对齐、语义映射、素材来源、渲染结果和人工盲评 evidence；
7. 所有失败必须记录，不允许 silent fallback。

## MoneyPrinterTurbo 决策
MoneyPrinterTurbo 不是新的主产品，也不是 Director Brain。

允许借鉴/复用：
- TTS/timestamp plumbing；
- stock media adapters；
- subtitle/transcription pipeline；
- FFmpeg probe/transcode/mux/normalize；
- batch/retry/job execution；
- encoding controls。

禁止把以下逻辑提升为核心：
- keyword → stock footage = visual intelligence；
- renderer 自己决定叙事；
- random/simple clips = editorial policy；
- script 直接一跳生成 final video 而没有 Director Timeline。

## Provider 边界
保留 ChatCut、Remotion、HyperFrames、FFmpeg、HeyGen、D-ID、stock、image/video generation、TTS/music/SFX 等适配接口。

不要为了接入某个 Provider 改写 Director Timeline 的语义。Provider 不支持时必须结构化 downgrade/fail。

## 诊断规则
如果问题是模糊、码率、字幕漂移、mux、崩溃、速度，先查 deployment/runtime。

如果问题是镜头“差不多相关但不对”、节奏平、素材提前出现、每句话都一样、动效过度，属于 Director / Visual Decision / Timeline 层，不允许继续靠调编码参数解决。

## 工作方式
每个开发任务必须包含：
1. 修改文件；
2. 真实运行方式；
3. 测试/证据；
4. 验证结果；
5. 错误与冲突记录；
6. 更新 `MASTER_TASK.md` 状态。

## 完成定义
不是代码数量，也不是“能生成 MP4”。

本阶段完成定义：同一份真实输入可以产出 Neutral 和 Directed 两版视频，Directed 版本的每个关键视觉动作都能追溯到 Director Timeline，并通过语义/时间 QA；随后进入盲评，验证它是否真的比中性素材拼接更好。
