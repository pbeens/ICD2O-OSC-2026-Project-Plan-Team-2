"""
check_pdf_conversion_structure.py — validate that PDF TOC headings survived into Markdown headings.

Usage:
    python3 utils/check_pdf_conversion_structure.py <file.pdf> <file.md>

Exit code:
    0 — structure passes
    1 — missing or collapsed headings detected
"""

from pathlib import Path
import re
import sys

import fitz


HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")


def normalize(text: str) -> str:
    text = text.replace("–", "-").replace("—", "-").replace("’", "'")
    text = re.sub(r"<sup>\d+</sup>", "", text)
    text = re.sub(r"\s+", " ", text.strip())
    return text.lower()


def get_pdf_toc_titles(pdf_path: Path) -> list[tuple[int, str, str]]:
    pdf = fitz.open(pdf_path)
    titles = []
    for level, title, _page in pdf.get_toc(simple=True):
        norm = normalize(title)
        if norm:
            titles.append((level, title, norm))
    return titles


def get_md_headings(md_path: Path) -> list[tuple[int, str, str]]:
    headings = []
    for line in md_path.read_text(encoding="utf-8", errors="ignore").splitlines():
        match = HEADING_RE.match(line.strip())
        if match:
            hashes, title = match.groups()
            norm = normalize(title)
            if norm:
                headings.append((len(hashes), title, norm))
    return headings


def main() -> None:
    if len(sys.argv) != 3:
        print("Usage: python3 utils/check_pdf_conversion_structure.py <file.pdf> <file.md>")
        sys.exit(1)

    pdf_path = Path(sys.argv[1])
    md_path = Path(sys.argv[2])

    if not pdf_path.exists():
        print(f"PDF not found: {pdf_path}")
        sys.exit(1)
    if not md_path.exists():
        print(f"Markdown file not found: {md_path}")
        sys.exit(1)

    toc_titles = get_pdf_toc_titles(pdf_path)
    md_headings = get_md_headings(md_path)
    md_heading_norms = {norm for _level, _title, norm in md_headings}
    md_text = md_path.read_text(encoding="utf-8", errors="ignore")
    md_text_norm = normalize(md_text)

    missing = []
    collapsed = []
    for _level, title, norm in toc_titles:
        if norm in md_heading_norms:
            continue
        if norm in md_text_norm:
            collapsed.append(title)
        else:
            missing.append(title)

    print("\n============================================================")
    print(f"Structure Report: {md_path}")
    print("============================================================")
    print(f"  PDF TOC entries       : {len(toc_titles)}")
    print(f"  Markdown headings     : {len(md_headings)}")
    print(f"  Missing as headings   : {len(missing) + len(collapsed)}")
    print(f"  Missing entirely      : {len(missing)}")
    print(f"  Present only in body  : {len(collapsed)}")

    if missing:
        print("\n  Missing entirely (first 10):")
        for title in missing[:10]:
            print(f"    - {title}")

    if collapsed:
        print("\n  Present in body but not as headings (first 10):")
        for title in collapsed[:10]:
            print(f"    - {title}")

    if missing or collapsed:
        print("\n  [✗] STRUCTURE CHECK FAILED: reconstruct missing headings before accepting the conversion.\n")
        sys.exit(1)

    print("\n  ✓ Structure check passed. PDF TOC headings are represented as Markdown headings.\n")


if __name__ == "__main__":
    main()
