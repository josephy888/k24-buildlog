#!/usr/bin/env python3
"""
Build Log File Generator + Append Tool
"""

from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path
import os
import subprocess
import sys
import tempfile
import shutil

# Always store logs inside this folder (relative to script location)
DEFAULT_DIR = str((Path(__file__).resolve().parent / "car_build_logs"))

TEMPLATE = """\
# {project_name}

## Snapshot
- Car: EK (RHD, ~1999)
- Intended use: Weekend toy / spirited / wet drives
- Key goals: Reliability first, then refinement

---

# Updates Log

"""

def now_stamp() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M")

def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)

def resolve_log_path(file_arg: str) -> Path:
    p = Path(file_arg)
    if p.is_absolute() or any(sep in file_arg for sep in ("/", "\\")):
        return p
    return Path(DEFAULT_DIR) / p

def init_log(file_path: Path, project_name: str, force: bool = False) -> None:
    ensure_dir(file_path.parent)
    if file_path.exists() and not force:
        print(f"[!] File already exists: {file_path}")
        print("    Use --force to overwrite.")
        return
    file_path.write_text(TEMPLATE.format(project_name=project_name), encoding="utf-8")
    print(f"[OK] Created build log: {file_path}")

def format_entry(title: str, text: str | None, bullets: list[str] | None) -> str:
    header = f"## {now_stamp()} — {title}"
    lines = [header, ""]
    if text:
        lines.append(text.strip())
        lines.append("")
    if bullets:
        for b in bullets:
            if b.strip():
                lines.append(f"- {b.strip()}")
        lines.append("")
    lines.append("---")
    lines.append("")
    return "\n".join(lines)

def pick_editor() -> list[str] | None:
    editor = os.environ.get("EDITOR")
    if editor:
        return editor.split()

    candidates = ["code", "notepad", "nano", "vi", "vim"]
    for c in candidates:
        if shutil.which(c):
            return [c]
    return None

def open_in_editor() -> str:
    editor_cmd = pick_editor()

    fd, tmp_path = tempfile.mkstemp(prefix="buildlog_", suffix=".txt")
    os.close(fd)
    tmp = Path(tmp_path)
    tmp.write_text(
        "# Write your note below. Lines starting with # will be ignored.\n",
        encoding="utf-8"
    )

    try:
        if editor_cmd:
            subprocess.call(editor_cmd + [str(tmp)])
        else:
            print("Paste your note below. End with Ctrl-Z then Enter (Windows).")
            raw = sys.stdin.read()
            tmp.write_text(raw, encoding="utf-8")

        raw_lines = tmp.read_text(encoding="utf-8").splitlines()
        cleaned = "\n".join([ln for ln in raw_lines if not ln.startswith("#")]).strip()
        return cleaned
    finally:
        try:
            tmp.unlink(missing_ok=True)
        except Exception:
            pass

def add_entry(file_path: Path, title: str, text: str | None, bullets: list[str] | None) -> None:
    if not file_path.exists():
        print(f"[!] File not found: {file_path}")
        print("    Run init first.")
        sys.exit(1)

    if not text and not bullets:
        text = open_in_editor()

    entry = format_entry(title=title, text=text, bullets=bullets)
    with file_path.open("a", encoding="utf-8") as f:
        f.write(entry)
    print(f"[OK] Added entry to: {file_path}")

def main():
    parser = argparse.ArgumentParser(description="Build log file generator + append tool")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_init = sub.add_parser("init", help="Create a new build log")
    p_init.add_argument("--name", required=True, help="Project name")
    p_init.add_argument("--file", required=True, help="File name (e.g. EK_K24.md)")
    p_init.add_argument("--force", action="store_true")

    p_add = sub.add_parser("add", help="Add an update entry")
    p_add.add_argument("--file", required=True)
    p_add.add_argument("--title", required=True)
    p_add.add_argument("--text", default=None)
    p_add.add_argument("--bullets", nargs="*", default=None)

    args = parser.parse_args()

    if args.cmd == "init":
        file_path = resolve_log_path(args.file)
        init_log(file_path=file_path, project_name=args.name, force=args.force)

    elif args.cmd == "add":
        file_path = resolve_log_path(args.file)
        add_entry(file_path=file_path, title=args.title, text=args.text, bullets=args.bullets)

if __name__ == "__main__":
    main()
