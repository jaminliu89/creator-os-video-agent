# AI Film Foundry v0.1 — Zero-planning-burden Preproduction Extension

Date: 2026-10-25
Status: CONTRACT + DETERMINISTIC LOCAL DEMO; NOT AUTONOMOUS FULL PIPELINE
Product owner: creator-os-video-agent (orchestration); skill-hub owns method/routing.

## Decision
Add an upstream **Preproduction** orchestration capability for idea/notes -> creative treatment -> complete shooting-ready package. This does NOT replace the existing `script/transcript -> Director IR -> Timeline -> Render` pipeline or `vlog-director` frozen core. Downstream accepts approved story, shot graph, asset and sound intent; editor/render pipeline stays unchanged.

## JTBD and user acceptance
Creator provides only an idea, e.g. '凌晨去看看城市苏醒，拍 20 分钟长 Vlog'. No questions about how to write, shoot, frame, pace, choose music or create look/mood boards are defaulted back to the creator. The system must provide substantive choices, complete speakable lines and a safe action-oriented field plan. Creator retains approval and can improvise/reject suggestions. Real-world unknowns become conditional prompts, not made-up facts.

## Scope
Vlog long form (15–60+ min), documentary/profile, cinematic diary, city/travel, challenge, scripted short, AI-generated fantasy, product/brand and wedding/event film. Cross-format core is scene intention, evidence, shot continuity, review and production constraints. Creative methods vary by genre.

## Architecture and collaboration
Host Agent (replaceable CLI / MCP / skill executor)
  -> Preproduction Orchestrator (stage DAG, resumption, QA, rights, budget, roadmap)
       -> Historical Asset & Material Recall
       -> Research Agent (browser provider abstraction)
       -> Story/Narrative (existing Narrative-Graph-Engine / vlog-director)
       -> Writer (existing writer-os and writing contracts)
       -> Director & mood/shot/previs (ai-director-engine, director-compiler)
       -> Producer, Safety, Rights, Independent Critic
  -> `PreproductionPackage v1` (scene ids, shot refs, detailed script, mood tiles, audio, timing, if/then branches)
  -> Existing Director IR / Director Timeline / execution orchestrator.

The platform/host, research browser and media provider are distinct replaceable concerns. Skills define craft/protocol, CLI runs deterministic jobs, MCP connects external systems, and an Agent Runtime manages plans, tools and retries.

## State graph
IDEA -> RECALL -> RESEARCH -> 3 TREATMENTS -> STORY_GRAPH -> FULL_SCRIPT -> MOODBOARD -> SHOTLIST -> CALENDAR/SAFETY/FEASIBILITY -> CRITIC/QA -> FIELD_PACKAGE -> USER_APPROVAL
CYCLES: criticize the failing chapter/shot, revise minimal upstream assets, cap retries, record reason.
REAL VLOG: preapproved plan -> live unscripted capture -> nightly material/story rewrite; do not hallucinate actual interactions.

## Mandatory outputs
1. angle alternatives + selected rationale;
2. scene-by-scene full spoken script, optional phrasing, VO, un-scriptable real-person question trees;
3. A-Line/B-Line plan and narrative drive, not necessarily fixed three acts;
4. mood board with actual color/light/composition/material/emotion specifications, reference provenance and rights state;
5. shot graph and VIDEO | AUDIO coverage with camera, safe execution and fallbacks;
6. field-ready minimal call sheet and gear checklist;
7. QA ledger that names original issue, revision and remaining limitations;
8. honest progress dashboard using real status and artifact links, not fictitious percentages.

## Research benchmark sample — NOT a global popularity top-10 ranking
| Study sample | Mechanism worth testing | Source or evidence |
| --- | --- | --- |
| Casey Neistat | filmmaking from daily observation, vlogging & spontaneous filmmaking, story/edit/pace | https://app.studio.com/casey-neistat-filmmaking |
| Peter McKinnon | purposeful B-roll, sound and editing-aware coverage | https://www.epidemicsound.com/blog/behind-the-creators-lens-peter-mckinnon/ |
| Ryan Trahan | simple premise, understandable progressive rule, authentic thumbnail | https://blog.youtube/creator-and-artist-stories/ryan-trahan-thumbnail-editing-secrets-to-going-viral/ |
| Michelle Khare | challenge + personal stakes -> long-form nonfiction episodes | https://blog.youtube/creator-and-artist-stories/michelle-khare-breaking-barriers-and-redefining-digital-content-creation/ |
| Lucy Moon | slower cinematic personal diary and emotion | https://blog.youtube/creator-and-artist-stories/discover-the-cinematic-vlogs-of-lucy-moon/ |
| Sam & Victor | ordinary life + multiple angles + productive imperfections | https://blog.youtube/creator-and-artist-stories/sam-and-victor/ |
| Kara & Nate | episodic travel progress and relationship continuity | https://karaandnate.com/about-us/ |
| MrBeast | highly legible premise and anticipation (optional, not global aesthetic) | https://www.mrbeastexplained.com/videos/how-a-video-is-made/ |
| Sean Evans / Hot Ones | meticulous research/interview preparation and escalated questions | https://blog.youtube/creator-and-artist-stories/youtube-emmy-contenders/ |
| Colin & Samir | long-form creator interviews and format/channel perspective | https://blog.youtube/news-and-events/colin-samir-favorites-made-on-youtube/ |

Evidence is heterogenous: interviews/course descriptions/reporting, not replicated creator production logs; mark technique inferences as inference. Test only distilled mechanism, never author identity/look imitation.

## Browser research selection
Lightpanda official https://github.com/lightpanda-io/browser: experimental/beta fast headless/CDP; check compatibility per site.
ego(lite) ego-browser official https://www.egolite.app/document/zh/docs/ego-browser: reuses Chromium session; context persistence may be useful for logged-in workflows only with explicit user authorization.
Fall back to official APIs, permitted browsing, existing search and approved browser adapters. NEVER bypass auth/paywalls or claim inaccessible footage was reviewed.

## Concrete V0 / local test evidence
A dependency-free `foundry.py` compiler prototype has been executed locally with one 20-minute Dawn City Vlog structured example, 8 scenes and 32 planned shots. Six offline unit tests passed (valid compile, missing scenes, duplicate IDs, consent safety, honest progress, HTML escaping). It emits director_package.md, moodboard.html, index.html, roadmap.json and qa.json. This evidence is **deterministic structured-input compilation only**; neither idea-to-script LLM automation nor remote browser/visual model generation was performed.
The runtime is available in the current conversation's downloadable prototype bundle; promotion into this repository remains tracked as a separate integration task.

## Workstreams (each demands measurable evidence)
P0: Commit and integrate tested compiler + schema and reproduce offline fixture in repo CI. Do not overclaim current demo.
P1: Host Agent from 1-sentence idea -> multiple treatments -> full draft using existing skill routing; explicit evidence and control budget.
P2: Reference/source pipeline, rights, mood board thumbnails/generated assets with provenance, legibility, aesthetic critique.
P3: long-form Vlog 20+ minute autonomous detailed script/shot/call sheet prototype; verify human speaking time, real-event branches and feasible shot day.
P4: real field test, nightly rewrite integration, human edit-hours and interventions measurement vs manual baseline.
P5: other genre production variants, AI-generation production-previs and provider adapters.

## DoD
Do not mark preproduction autonomous until source material retrieval, generation, self-critique, moodboard assets, field-ready script and feedback have been run end-to-end on at least one real 20-minute vlog. A tested file compiler and an author-written example only satisfy a portion of P0.
