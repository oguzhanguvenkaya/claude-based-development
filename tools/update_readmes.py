"""Mark README.md video lines with ✅ for downloaded videos.

Walks each lesson folder under data-science/raw/course-notes/sprint {1,2,3}/
and for each `[[NN-slug]]` wikilink in README.md, adds a ✅ prefix if
videos/NN-slug.mp4 exists.
"""

from __future__ import annotations
import re
from pathlib import Path

BASE = Path(r"c:\Users\oguzhan\Desktop\claude-based-development\data-science\raw\course-notes")

WIKILINK = re.compile(r"^(- )(?:✅ )?(\[\[(\d{2}-[a-z0-9-]+)\]\] — .+)$", re.MULTILINE)


def update_lesson(lesson_dir: Path) -> tuple[int, int]:
    readme = lesson_dir / "README.md"
    if not readme.exists():
        return 0, 0
    videos_dir = lesson_dir / "videos"
    text = readme.read_text(encoding="utf-8")
    marked = unmarked = 0

    def replace(m: re.Match[str]) -> str:
        nonlocal marked, unmarked
        prefix, body, slug = m.group(1), m.group(2), m.group(3)
        video_file = videos_dir / f"{slug}.mp4"
        if video_file.exists() and video_file.stat().st_size > 100_000:
            marked += 1
            return f"{prefix}✅ {body}"
        else:
            unmarked += 1
            return f"{prefix}{body}"

    new_text = WIKILINK.sub(replace, text)
    if new_text != text:
        readme.write_text(new_text, encoding="utf-8")
    return marked, unmarked


def main() -> None:
    total_marked = total_unmarked = 0
    for sprint_dir in sorted(BASE.glob("sprint *")):
        for lesson_dir in sorted(sprint_dir.iterdir()):
            if lesson_dir.is_dir() and (lesson_dir / "README.md").exists():
                m, u = update_lesson(lesson_dir)
                total_marked += m
                total_unmarked += u
                rel = lesson_dir.relative_to(BASE)
                print(f"{rel}: {m} marked, {u} unmarked")
    print(f"\nTOTAL: {total_marked} marked, {total_unmarked} unmarked")


if __name__ == "__main__":
    main()
