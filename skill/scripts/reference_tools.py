#!/usr/bin/env python3
"""Inspect a reference, transcribe audio, or lint a declared scene plan."""
import argparse
import hashlib
import json
import math
import re
import subprocess
from pathlib import Path


def probe(path):
    return json.loads(subprocess.check_output([
        "ffprobe", "-v", "error", "-show_format", "-show_streams", "-of", "json", str(path)
    ]))


def inspect_video(path, output, interval):
    import io
    from PIL import Image, ImageDraw
    if interval <= 0:
        raise ValueError("interval must be positive")
    output.mkdir(parents=True, exist_ok=True)
    metadata = probe(path)
    duration = float(metadata["format"]["duration"])
    metadata["source_sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
    metadata["evidence_scope"] = "timestamped sampled frames; not full audiovisual playback"
    (output / "metadata.json").write_text(json.dumps(metadata, indent=2))
    count = max(1, math.ceil(duration / interval))
    pages = []
    for start in range(0, count, 25):
        n = min(25, count - start)
        sheet = Image.new("RGB", (1000, math.ceil(n / 5) * 380), "white")
        draw = ImageDraw.Draw(sheet)
        for j in range(n):
            timestamp = min((start + j) * interval, max(0, duration - .05))
            data = subprocess.check_output([
                "ffmpeg", "-v", "error", "-ss", str(timestamp), "-i", str(path),
                "-frames:v", "1", "-vf",
                "scale=200:356:force_original_aspect_ratio=decrease,pad=200:356:(ow-iw)/2:(oh-ih)/2",
                "-threads", "1", "-f", "image2pipe", "-vcodec", "png", "-"
            ])
            x, y = (j % 5) * 200, (j // 5) * 380
            sheet.paste(Image.open(io.BytesIO(data)), (x, y))
            draw.text((x + 3, y + 358), f"{timestamp:.2f}s", fill="black")
        dest = output / f"timeline-{start // 25 + 1:02d}.jpg"
        sheet.save(dest)
        pages.append(str(dest))
    has_audio = any(s["codec_type"] == "audio" for s in metadata["streams"])
    if has_audio:
        subprocess.run([
            "ffmpeg", "-v", "error", "-y", "-i", str(path), "-ar", "16000",
            "-ac", "1", "-f", "f32le", str(output / "audio.f32")
        ], check=True)
    return {"duration": duration, "pages": pages, "has_audio": has_audio}


def transcribe(path, output, language, model):
    import numpy as np
    from faster_whisper import WhisperModel
    output.mkdir(parents=True, exist_ok=True)
    raw = output / "audio.f32"
    subprocess.run([
        "ffmpeg", "-v", "error", "-y", "-i", str(path), "-ar", "16000",
        "-ac", "1", "-f", "f32le", str(raw)
    ], check=True)
    # A waveform avoids PyAV metadata_errors incompatibility seen in production.
    waveform = np.fromfile(raw, dtype=np.float32)
    engine = WhisperModel(model, device="cpu", compute_type="int8")
    segments, info = engine.transcribe(waveform, language=language, beam_size=5)
    rows = [{"start": s.start, "end": s.end, "text": s.text.strip()} for s in segments]
    result = {"source": path.name, "method": "faster-whisper", "model": model,
              "language": info.language, "review_status": "machine transcript; human/caption cross-check required",
              "segments": rows}
    (output / "transcript.json").write_text(json.dumps(result, ensure_ascii=False, indent=2))
    (output / "transcript.txt").write_text("\n".join(r["text"] for r in rows))
    return result


def lint(plan):
    errors, warnings = [], []
    scenes = plan.get("scenes", [])
    if not scenes:
        errors.append("No scenes")
    if plan.get("translation_mode") not in ("faithful", "condensed-approved", "adaptation-approved"):
        errors.append("Declare translation_mode")
    total, ids, previous = 0, set(), {}
    voice_blocks = []
    for scene in scenes:
        sid = scene.get("id", "?")
        if sid in ids:
            errors.append(f"{sid}: duplicate id")
        ids.add(sid)
        duration = scene.get("duration", 0)
        if duration not in (4, 6, 8, 10):
            errors.append(f"{sid}: duration must be 4/6/8/10")
        total += duration if isinstance(duration, (float, int)) else 0
        if scene.get("speaker") != "Elias":
            errors.append(f"{sid}: only Elias may speak")
        for key in ("dialogue", "image", "prompt", "entry_state", "exit_state", "actions"):
            if not scene.get(key):
                errors.append(f"{sid}: missing {key}")
        entry = scene.get("entry_state", {})
        for prop, state in previous.items():
            if prop in entry and entry[prop] != state:
                errors.append(f"{sid}: {prop} resets from {state!r} to {entry[prop]!r}; explain inter-shot change")
        previous = scene.get("exit_state", {})
        prompt = scene.get("prompt", "")
        if "VOICE — ELIAS:" not in prompt:
            errors.append(f"{sid}: missing voice block")
        else:
            voice_blocks.append(prompt.split("VOICE — ELIAS:", 1)[1].split("CAMERA", 1)[0].strip())
        words = len(re.findall(r"\b[\w’'-]+\b", scene.get("dialogue", "")))
        if isinstance(duration, (int, float)) and duration > 0 and words * 60 / duration > 180:
            warnings.append(f"{sid}: speech above 180 wpm; timed read needed")
    if len(set(voice_blocks)) > 1:
        errors.append("Voice blocks differ across scenes")
    if total != plan.get("target_seconds"):
        errors.append(f"Total {total}s differs from target {plan.get('target_seconds')}")
    return {"ok": not errors, "total_seconds": total, "errors": errors, "warnings": warnings,
            "scope": "declared structure only; not medical, audiovisual or retention validation"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    subs = parser.add_subparsers(dest="command", required=True)
    for command in ("inspect", "transcribe"):
        p = subs.add_parser(command)
        p.add_argument("source", type=Path)
        p.add_argument("output", type=Path)
        if command == "inspect":
            p.add_argument("--interval", type=float, default=4)
        else:
            p.add_argument("--language", default="tl")
            p.add_argument("--model", default="small")
    p = subs.add_parser("lint")
    p.add_argument("plan", type=Path)
    args = parser.parse_args()
    if args.command == "inspect":
        result = inspect_video(args.source, args.output, args.interval)
    elif args.command == "transcribe":
        result = transcribe(args.source, args.output, args.language, args.model)
    else:
        result = lint(json.loads(args.plan.read_text()))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if args.command == "lint" and not result["ok"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
