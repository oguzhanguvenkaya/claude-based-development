"""Mark README.md video lines with ✅ (video) and 📝 (transcript) indicators.

Walks each lesson folder under data-science/raw/course-notes/sprint {1,2,3}/
and for each `[[NN-slug]]` wikilink in README.md, prepends ✅ if
videos/NN-slug.mp4 exists, and 📝 if transcripts/NN-slug.md exists.
"""

from __future__ import annotations
import re
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent / "data-science" / "raw" / "course-notes"

WIKILINK = re.compile(r"^(- )(?:[✅📝]\s)*(\[\[(\d{2}-[a-z0-9-]+)\]\] — .+)$", re.MULTILINE)


def update_lesson(lesson_dir: Path) -> tuple[int, int, int]:
    """Returns (videos_marked, transcripts_marked, unmarked)."""
    readme = lesson_dir / "README.md"
    if not readme.exists():
        return 0, 0, 0
    videos_dir = lesson_dir / "videos"
    transcripts_dir = lesson_dir / "transcripts"
    text = readme.read_text(encoding="utf-8")
    videos_marked = transcripts_marked = unmarked = 0

    def replace(m: re.Match[str]) -> str:
        nonlocal videos_marked, transcripts_marked, unmarked
        prefix, body, slug = m.group(1), m.group(2), m.group(3)
        markers = []
        video_file = videos_dir / f"{slug}.mp4"
        if video_file.exists() and video_file.stat().st_size > 100_000:
            markers.append("✅")
            videos_marked += 1
        transcript_file = transcripts_dir / f"{slug}.md"
        if transcript_file.exists():
            markers.append("📝")
            transcripts_marked += 1
        if not markers:
            unmarked += 1
        marker_str = "".join(f"{tok} " for tok in markers)
        return f"{prefix}{marker_str}{body}"

    new_text = WIKILINK.sub(replace, text)
    if new_text != text:
        readme.write_text(new_text, encoding="utf-8")
    return videos_marked, transcripts_marked, unmarked


def main() -> None:
    total_v = total_t = total_u = 0
    for sprint_dir in sorted(BASE.glob("sprint *")):
        for lesson_dir in sorted(sprint_dir.iterdir()):
            if lesson_dir.is_dir() and (lesson_dir / "README.md").exists():
                v, t, u = update_lesson(lesson_dir)
                total_v += v
                total_t += t
                total_u += u
                rel = lesson_dir.relative_to(BASE)
                print(f"{rel}: ✅={v} 📝={t} unmarked={u}")
    print(f"\nTOTAL: ✅={total_v} videos, 📝={total_t} transcripts, unmarked={total_u}")


if __name__ == "__main__":
    main()
