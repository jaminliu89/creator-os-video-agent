# Deployment vs Director Diagnosis Matrix

Use this before spending time tuning codecs, models, prompts or deployment.

| Symptom | Primary layer | Deployment tuning likely helps? | Correct action |
|---|---|---:|---|
| blurry output / bitrate loss | renderer/encoding | yes | inspect resolution, bitrate, codec, transcode chain |
| audio missing / mux failure | renderer/media plumbing | yes | FFmpeg probe, stream mapping, container checks |
| subtitle drift | timing/transcription | yes | timestamp source, Whisper/TTS alignment, timebase checks |
| render is slow / crashes | runtime/deployment | yes | hardware encoder, memory, concurrency, retries |
| stock clip is related but feels wrong | director/visual decision | no | fix beat semantics and visual purpose |
| later concept appears too early | director timeline / temporal alignment | rarely | bind assets to beat time ranges and semantic refs |
| every sentence gets similar B-roll | director policy | no | use narrative function, contrast, hold/none decisions |
| video feels flat despite technically correct render | pacing/art direction | no | rhythm, emphasis, silence, visual contrast, MG planning |
| too many decorative animations | restraint policy | no | semantic gating and motion restraint |
| AI-video look / generic stock feeling | asset strategy | partly | improve source strategy only after Director Timeline is correct |

## Rule
Do not attempt to solve a director-layer defect with renderer tuning.

A render pipeline is accepted only when it preserves an already-valid Director Timeline. It is not allowed to invent narrative meaning in order to make the output look busier.

## Escalation sequence
1. Verify media plumbing and timestamps.
2. Verify beat boundaries and narrative functions.
3. Verify visual decision purpose per beat.
4. Verify provider routing preserves the decision.
5. Verify final render quality.
6. Run human preference review.
