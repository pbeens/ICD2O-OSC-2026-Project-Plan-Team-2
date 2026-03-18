"""
fix_markdown_lints.py — light formatting cleanup for Markdown generated from PDFs.

Usage:
    python3 utils/fix_markdown_lints.py <path_to_file.md>

This script is intentionally conservative. It normalizes a few common formatting
issues without trying to rewrite document structure.
"""

from pathlib import Path
import re
import sys


HEADING_RE = re.compile(r"^#{1,6} ")
LIST_RE = re.compile(r"^(\s*)([-*])\s+(.*)$")


def fix_markdown(file_path: Path) -> None:
    if not file_path.exists():
        print(f"File not found: {file_path}")
        sys.exit(1)

    lines = file_path.read_text(encoding="utf-8").splitlines()
    new_lines = []

    for line in lines:
        match = LIST_RE.match(line)
        if match:
            indent, _marker, content = match.groups()
            line = f"{indent}- {content.strip()}"

        if HEADING_RE.match(line):
            if new_lines and new_lines[-1].strip() and new_lines[-1] != "---":
                new_lines.append("")
            new_lines.append(line)
            new_lines.append("")
            continue

        new_lines.append(line.rstrip())

    content = "\n".join(new_lines).strip() + "\n"
    content = re.sub(r"\n{3,}", "\n\n", content)
    content = re.sub(r"(\n- .*)(\n#{1,6} )", r"\1\n\2", content)

    file_path.write_text(content, encoding="utf-8")
    print(f"Lint fix complete for: {file_path}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 utils/fix_markdown_lints.py <file.md>")
        sys.exit(1)

    fix_markdown(Path(sys.argv[1]))
