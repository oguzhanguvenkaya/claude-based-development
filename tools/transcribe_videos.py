"""Batch transcribe lesson videos via OpenAI gpt-4o-transcribe.

Walks <lesson>/videos/*.mp4 under data-science/raw/course-notes/sprint {1,2,3}/,
extracts mono 64 kbps mp3 (fits under OpenAI's 25 MB limit), sends to the
transcription endpoint, and writes <lesson>/transcripts/<slug>.md with YAML
frontmatter + plain-text transcript.

Idempotent: skips videos that already have a transcript file. Pass --force
to overwrite. Logs to tools/transcribe_videos.log.

Usage:
    export OPENAI_API_KEY=sk-...
    pip install openai
    python tools/transcribe_videos.py            # all videos
    python tools/transcribe_videos.py --dry-run  # list what would be done
    python tools/transcribe_videos.py --limit 3  # first 3 (smoke test)
    python tools/transcribe_videos.py --force    # re-transcribe everything
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from threading import Lock

REPO_ROOT = Path(__file__).resolve().parent.parent
BASE = REPO_ROOT / "data-science" / "raw" / "course-notes"
LOG = Path(__file__).resolve().parent / "transcribe_videos.log"

MODEL = "gpt-4o-transcribe"
LANGUAGE = "tr"
CONCURRENCY = 4
AUDIO_BITRATE = "64k"  # mono mp3 — ~30 MB/hour, well under 25 MB for typical lesson clips
MAX_FILE_BYTES = 25 * 1024 * 1024  # OpenAI hard limit

_log_lock = Lock()
_cost_lock = Lock()
_total_seconds_transcribed = 0.0


@dataclass
class Job:
    video: Path
    transcript: Path
    sprint: int
    lesson_dir: Path
    slug: str


def log(msg: str) -> None:
    line = f"[{datetime.now().isoformat(timespec='seconds')}] {msg}"
    with _log_lock:
        print(line, flush=True)
        with LOG.open("a", encoding="utf-8") as f:
            f.write(line + "\n")


def video_duration_seconds(video: Path) -> float:
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(video)],
        capture_output=True, text=True, check=False,
    )
    try:
        return float(out.stdout.strip())
    except ValueError:
        return 0.0


def extract_audio(video: Path, out_mp3: Path) -> None:
    cmd = [
        "ffmpeg", "-y", "-loglevel", "error",
        "-i", str(video),
        "-vn", "-ac", "1", "-c:a", "libmp3lame", "-b:a", AUDIO_BITRATE,
        str(out_mp3),
    ]
    subprocess.run(cmd, check=True)


def discover_jobs() -> list[Job]:
    jobs: list[Job] = []
    for sprint_dir in sorted(BASE.glob("sprint *")):
        try:
            sprint_no = int(sprint_dir.name.rsplit(" ", 1)[-1])
        except ValueError:
            continue
        for lesson_dir in sorted(sprint_dir.iterdir()):
            if not lesson_dir.is_dir():
                continue
            videos_dir = lesson_dir / "videos"
            if not videos_dir.is_dir():
                continue
            for mp4 in sorted(videos_dir.glob("*.mp4")):
                slug = mp4.stem
                transcript = lesson_dir / "transcripts" / f"{slug}.md"
                jobs.append(Job(mp4, transcript, sprint_no, lesson_dir, slug))
    return jobs


def render_markdown(job: Job, transcript_text: str, duration: float) -> str:
    lesson_slug = job.lesson_dir.name
    lesson_title = lesson_slug.split("-", 1)[-1].replace("-", " ").title() if "-" in lesson_slug else lesson_slug
    title = job.slug.split("-", 1)[-1].replace("-", " ").capitalize() if "-" in job.slug else job.slug
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    frontmatter = (
        "---\n"
        f"sprint: {job.sprint}\n"
        f"lesson_slug: {lesson_slug}\n"
        f"video_slug: {job.slug}\n"
        f"video_file: videos/{job.slug}.mp4\n"
        f"duration_seconds: {int(duration)}\n"
        f"model: {MODEL}\n"
        f"language: {LANGUAGE}\n"
        f"transcribed_at: {now}\n"
        f"tags: [transcript, sprint-{job.sprint}]\n"
        "---\n\n"
    )
    body = (
        f"# {title}\n\n"
        f"> Otomatik transkript — kaynak: `videos/{job.slug}.mp4` "
        f"(ders: {lesson_title}). Düzeltmeler için video referans alınmalıdır.\n\n"
        f"{transcript_text.strip()}\n"
    )
    return frontmatter + body


def transcribe_one(client, job: Job) -> tuple[Job, str | None, float]:
    """Returns (job, error_or_none, duration_seconds)."""
    duration = video_duration_seconds(job.video)
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp:
        tmp_path = Path(tmp.name)
    try:
        extract_audio(job.video, tmp_path)
        size = tmp_path.stat().st_size
        if size > MAX_FILE_BYTES:
            return job, f"audio too large after compression: {size} bytes (>25MB)", duration

        with tmp_path.open("rb") as f:
            response = client.audio.transcriptions.create(
                model=MODEL,
                file=f,
                language=LANGUAGE,
                response_format="text",
            )
        # SDK returns either an object or a plain string depending on response_format
        text = response if isinstance(response, str) else getattr(response, "text", "")
        if not text.strip():
            return job, "empty transcript response", duration

        job.transcript.parent.mkdir(parents=True, exist_ok=True)
        job.transcript.write_text(render_markdown(job, text, duration), encoding="utf-8")
        return job, None, duration
    except Exception as e:  # noqa: BLE001
        return job, f"{type(e).__name__}: {e}", duration
    finally:
        tmp_path.unlink(missing_ok=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--force", action="store_true", help="Re-transcribe even if transcript exists.")
    parser.add_argument("--dry-run", action="store_true", help="List jobs without calling the API.")
    parser.add_argument("--limit", type=int, default=0, help="Process at most N videos (0 = all).")
    parser.add_argument("--concurrency", type=int, default=CONCURRENCY, help="Parallel API calls.")
    args = parser.parse_args()

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key and not args.dry_run:
        log("ERROR: OPENAI_API_KEY environment variable not set.")
        return 2

    all_jobs = discover_jobs()
    pending = [j for j in all_jobs if args.force or not j.transcript.exists()]
    already_done = 0 if args.force else len(all_jobs) - len(pending)
    if args.limit:
        pending = pending[: args.limit]
    log(f"Discovered {len(all_jobs)} videos, {already_done} already transcribed, "
        f"{len(pending)} in this batch.")

    if args.dry_run:
        for j in pending:
            log(f"DRY  {j.sprint}/{j.lesson_dir.name}/{j.slug}")
        return 0

    if not pending:
        log("Nothing to do.")
        return 0

    # Import here so --dry-run works without openai installed
    try:
        from openai import OpenAI
    except ImportError:
        log("ERROR: `openai` package not installed. Run: pip install openai")
        return 2

    client = OpenAI(api_key=api_key)
    start = time.time()
    ok = fail = 0

    with ThreadPoolExecutor(max_workers=args.concurrency) as ex:
        futures = {ex.submit(transcribe_one, client, j): j for j in pending}
        for fut in as_completed(futures):
            job, err, dur = fut.result()
            rel = job.transcript.relative_to(REPO_ROOT)
            if err is None:
                ok += 1
                with _cost_lock:
                    global _total_seconds_transcribed
                    _total_seconds_transcribed += dur
                log(f"OK   {ok+fail}/{len(pending)}  {rel}  ({dur:.0f}s)")
            else:
                fail += 1
                log(f"FAIL {ok+fail}/{len(pending)}  {rel}  -> {err}")

    elapsed = time.time() - start
    minutes = _total_seconds_transcribed / 60.0
    cost = minutes * 0.006  # gpt-4o-transcribe billed similarly to whisper-1
    log(f"Done. ok={ok} fail={fail} elapsed={elapsed:.0f}s "
        f"transcribed_minutes={minutes:.1f} approx_cost=${cost:.2f}")
    return 0 if fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
