# Production lessons — 2026-11-05

These are recorded production observations and user preferences, not medical validation or measured retention.

- The user rejected replacing a supplied Filipino reference's premise with a debunking story. Transcribe first, translate faithfully, and keep any proposed corrections separately labelled. Do not generate image batches before a requested script review.
- A 65.92s source used lung-model hook -> turmeric/ginger -> lemon/honey -> ingredient explanation -> finished drink -> supplement pitch. A source cutoff near 48s excludes the later pitch. Source video is deliberately not bundled.
- Local faster-whisper small plus on-screen caption checks recovered audio; some spelling/brand words remained uncertain. “Magpalambot” had no clear object: do not insert “throat” or “mucus” as certainty.
- PyAV rejected metadata_errors in this environment. ffmpeg extraction to 16kHz mono float32 plus passing a NumPy waveform bypassed that mismatch.
- User approved wider waist-up framing and less background greenery. A later generated video brought hanging plants back: audit actual output against its accepted image.
- One image changed a two-handled pot into a saucepan. Fix with the preceding accepted frame, not generic text alone.
- Do not repeat preparation while explaining ingredients. Track entry/exit states rather than making every line another demonstration.
- A generated opening measured about 10.03s; ASR ended its last phrase around 9.92s. This confirms approximate wording/completion, not voice quality or lip sync.
- A repeated voice block is not guaranteed identical audio. Reuse preset/reference where supported.
- User wants ONE agent doing all roles; no specialist spawning or independent-review agents.

## Content boundaries
Reference claims are not medical evidence. Do not label lung-cleansing, tar removal or simulated organ transformations verified. Keep factual review separate from translation and identify material publication conflicts explicitly. Never manufacture an outcome to match an unsupported claim.

## Future entries
Record asset/version, source of observation, user feedback, fix, checks, remaining uncertainty and whether a lesson is tested or proposed. Never infer virality from a nice-looking sample.
