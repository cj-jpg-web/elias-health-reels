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
Complete the source-shot and generation-clip tables in references/templates.md BEFORE generating images. Assign source shot IDs separately from clip IDs. Record source intervals, visible evidence, dialogue, visual focus, framing, entry state, principal action, exit state and transition. Do not infer an unseen action from the spoken instructions.
Track actual preparation states, including quantity, texture, utensil location and grip. Carry completed actions forward. When explaining an ingredient later, hold/show it; DO NOT add it again. Ingredient continuity alone is not visual progression.
State what each shot advances: a physical change, demonstration, explanation or reveal. Preserve a purposeful source hold; do not invent activity merely to make every frame different. Follow actual source composition and purpose rather than a generic hook/remedy/outro template.

## 4. Allocate clips
Use 4, 6, 8 or 10 seconds. A source shot may span clips; each split must continue rather than restart the action.
Treat generation clips and editorial scenes as different units. Split at complete speech/action beats, not automatically at sentence boundaries. Use the shortest allowed duration that comfortably completes the measured beat; extend to the next supported duration when needed. Preserve a hold across clips when the source holds. Do not create extra presenter scenes or lengthen a short reference merely to fill slots.
Measure an English read/voice guide when available. Word count is a heuristic, not proof of fit. Allow action and finishing margin. If exact wording does not fit, lengthen/repartition or explicitly propose compression.
Run scripts/reference_tools.py lint episode.json. Structural checks do not prove medical truth, voice quality, pixel continuity or actual timing.

## 5. Create starting images
Use image generation and approved character/setting references. Character-sheet-only generation is insufficient to lock the kitchen. Use accepted neighboring images to preserve cookware and physical state, not to copy every pose and composition. Explicitly separate invariants (identity/set/props/state) from shot variables (focus/framing/pose/action).
Generate ONE separate 9:16 image per scene, not a collage. Use the pose BEFORE action and correct already-completed ingredient states.
Preserve identity, wardrobe, kitchen geometry, light, pot handle count, utensils, liquid, supporting identities and contact positions. Inspect every result and correct only failed details.
Use the wider waist-up view for presenter shots; choose source-supported action views when hands, contents or texture are the actual subject. Do not keep Elias's whole torso in every shot at the expense of action clarity. Camera variation is not a substitute for progression. Do not recreate an approved asset unless it fails a specific requirement.

## 5a. Required sequence review before delivery
Read references/sequence-review.md. Inspect ALL generated starting frames together in numeric order alongside their assigned actions and source-shot evidence. A contact sheet is for internal review only; deliver separate images.
Check both adjacent frames and the whole sequence: redundant compositions, skipped actions, premature finished states, repeated additions, quantity/texture jumps and unjustified new scenes. A starting frame must precede its assigned action, not illustrate the finished action. Allow similar frames for an intentional continuous source hold; record why.
Record pass/fix decisions with the actual defect and evidence in the checkpoint. Do not mark a sequence passed just because individual images look attractive or state labels are consistent. Correct only failed images/planning, then recheck affected neighbors before delivery. If an image is unavailable, label that review pending rather than claim it passed.
The lint helper checks declared structure only. It does not inspect pixels or establish sequence quality. Perform the visual review yourself, without delegation. Do not regenerate a failed episode merely to test a skill update unless the user requests production.

## 6. Deliver image + prompt together
Display each actual image as an INLINE VISIBLE PREVIEW immediately ABOVE its complete numbered prompt, not a click-only file link. Keep numeric order and identify superseded/corrected versions.
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
