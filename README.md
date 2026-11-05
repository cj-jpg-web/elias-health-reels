# Elias Health Reels

Standalone, single-agent workflow for reference-led Elias health videos.

1. Inspect and transcribe the supplied video from audio.
2. Compare original speech with faithful English; flag uncertainties and health claims separately.
3. Map actual shots and progressing prop states.
4. Allocate 4/6/8/10-second clips.
5. Generate separate consistent 9:16 starting images.
6. Deliver each image above its complete dialogue/action/voice prompt.
7. Audit generated clips and checkpoint accepted work.

Only Elias speaks. Completed actions stay completed. No delegation.

Read [SKILL.md](skill/SKILL.md). The portable `skill/` folder includes voice/visual contracts, templates, production lessons, approved character/kitchen assets, and inspection/transcription/plan-check helpers. Supply the entire folder to your agent.

Helpers require ffmpeg/ffprobe and Python dependencies in `skill/scripts/requirements.txt`; ASR needs model weights. Commands are in SKILL.md.

Tested real video probing, frame extraction and transcription, plus plan checks for invalid duration, extra speakers, prop resets and voice-block mismatch. These checks do not establish medical accuracy, lip sync, generated voice consistency or audience retention.

Third-party reference footage and episode transcripts are excluded. Translation is not endorsement; health claims require separate verification.
