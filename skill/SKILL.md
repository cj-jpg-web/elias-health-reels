---
name: direct-health-reference
description: Transcribe supplied health reference videos, translate faithfully into English, reproduce visual progression with Elias, and deliver separate consistent 9:16 scene images with literal action-and-dialogue prompts and evidence-scoped audits. Use for reference-led AI host reels, 4/6/8/10-second clips, voice consistency and corrections. Execute every role in one agent without delegation.
---

# Direct Health Reference

## Binding contract
- Work alone. Do not spawn subagents for any role, including audits and validation.
- Default to faithful translation and reference-matched shots, not a rewritten story. Preserve meaning, order, steps, quantities, instructed preparation times and selected endpoint. Do not silently add advice, jokes, straining, different quantities or a new premise.
- Distinguish recording a speaker's claim from endorsing it. Keep health verification separately visible. Never call unsupported remedies verified or invent evidence. If a source claim cannot responsibly be used as advice, identify that conflict and label a proposed revision; never disguise it as translation.
- Improve camera, emphasis and lighting only while preserving the source's action and information. Do not fabricate treatment outcomes through model transformations.
- Keep Elias the ONLY speaker. Supporting people demonstrate and react silently. Do not invent supporting people when none are needed.
- Honor the requested stage: script-only means no images. When a full package is authorized, complete it without repeated permission questions.
- Read [voice-and-visuals.md](references/voice-and-visuals.md), [templates.md](references/templates.md), and relevant [production-lessons.md](references/production-lessons.md).

## Runtime helpers
Require system ffmpeg/ffprobe. Install Python dependencies from scripts/requirements.txt only when unavailable. ASR needs cached model weights or network access; report download failures without substituting invented text. Run:
```bash
python scripts/reference_tools.py inspect source.mp4 episode/evidence --interval 4
python scripts/reference_tools.py transcribe source.mp4 episode/evidence --language tl --model small
python scripts/reference_tools.py lint episode/episode.json
```

## 1. Inspect and transcribe
Probe duration, dimensions, fps and audio. Sample the complete timeline and inspect shot changes/contact windows more densely. Use scripts/reference_tools.py inspect for a contact sheet and extracted audio.
Transcribe AUDIO using an available ASR tool or scripts/reference_tools.py transcribe. Cross-check captions without treating them as ground truth. Mark uncertain words/brands; normalize punctuation but do not invent missing speech.
State evidence scope: sampled frames, decoded audio/ASR, full audiovisual playback, or metadata. Never claim full viewing from sampled stills, or evaluate voice timbre/lip sync from ASR text.
Cache transcript and source hash. Reuse unchanged evidence. If ASR fails, report the limitation and label caption-only reconstruction. Keep third-party footage local and out of public repositories.

## 2. Translate before producing
Present timestamp | original speech | faithful English | uncertainty, then the English script alone when requested.
Preserve culturally specific/ambiguous meaning, explaining uncertainty separately. Label compression, omissions, localization and corrections. Do not call a condensed script exact.
Distinguish source endpoint from final runtime: “stop at 48 seconds” may mean the first 48s of source, not a 48s target. Establish the intended meaning when consequential; complete independent transcription meanwhile.

## 3. Map actual progression
Record each shot's source interval, dialogue, framing, entry prop state, action, exit state and next shot.
Track empty pot -> turmeric added -> ginger added -> simmered -> lemon added -> honey added -> finished drink. Carry completed actions forward. When explaining an ingredient later, hold/show it; DO NOT add it again.
Follow actual source compositions and shot purposes. Do not force a generic hook/remedy/outro template. Camera changes must not reset the process.

## 4. Allocate clips
Use 4, 6, 8 or 10 seconds. A source shot may span clips; each split must continue rather than restart the action.
Measure an English read/voice guide when available. Word count is a heuristic, not proof of fit. Allow action and finishing margin. If exact wording does not fit, lengthen/repartition or explicitly propose compression.
Run scripts/reference_tools.py lint episode.json. Structural checks do not prove medical truth, voice quality, pixel continuity or actual timing.

## 5. Create starting images
Use image generation and approved character/setting references. Character-sheet-only generation is insufficient to lock the kitchen. Use accepted neighboring images to preserve exact cookware and grips.
Generate ONE separate 9:16 image per scene, not a collage. Use the pose BEFORE action and correct already-completed ingredient states.
Preserve identity, wardrobe, kitchen geometry, light, pot handle count, utensils, liquid, supporting identities and contact positions. Inspect every result and correct only failed details.
Default to approved wider waist-up framing: elbows and work surface visible, sparse greenery, active props legible. Vary angles only when useful. Do not recreate an already approved asset.

## 6. Deliver image + prompt together
Display each actual image immediately ABOVE its complete numbered prompt. Keep numeric order and identify superseded/corrected versions.
Each prompt must contain exact dialogue, word-matched literal actions, end pose/prop state, camera/audio and the IDENTICAL complete voice block from voice-and-visuals.md. Avoid “gesture naturally” as the meaningful direction.
Exclude additional speech, captions, music, logos and unplanned cuts. Do not introduce new preparation during explanation.

## 7. Audit generated clips
Probe/decode and sample actual outputs; transcribe actual audio. Compare words, completion time, identity, background/plant drift, props, contact, flicker, framing and neighboring state.
Report only checked dimensions. ASR does not establish appealing voice/accent or exact audiovisual synchronization. Mark unreviewed playback/audio aspects.
Give keep/trim/regenerate with evidence and targeted corrections. Separate technical validity, user preference, medical accuracy and unmeasured retention.

## 8. Persist and resume
Keep an episode checkpoint: source hash, source cutoff, translation mode/version, final runtime, voice reference, scene plan, accepted image versions, prompts, clip audits and next unfinished step.
Resume accepted work; do not restart or imply work continues after the turn ends.
Save deliverables through the applicable persistent-file workflow. Sync skill changes with the authorized GitHub repo. Do not publish third-party footage, secrets, private media locators or raw chat history. Use only approved original character/setting assets.
