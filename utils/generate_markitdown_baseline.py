"""
generate_markitdown_baseline.py — create a MarkItDown baseline text file from a PDF.

Usage:
    python3 utils/generate_markitdown_baseline.py resources/file.pdf

Output:
    resources/file.markitdown.txt
"""

from pathlib import Path
import sys

from markitdown import MarkItDown


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 utils/generate_markitdown_baseline.py <file.pdf>")
        sys.exit(1)

    pdf_path = Path(sys.argv[1])
    if not pdf_path.exists():
        print(f"File not found: {pdf_path}")
        sys.exit(1)

    if pdf_path.suffix.lower() != ".pdf":
        print(f"Expected a PDF file, got: {pdf_path}")
        sys.exit(1)

    output_path = pdf_path.with_suffix("").with_name(pdf_path.stem + ".markitdown.txt")

    converter = MarkItDown()
    result = converter.convert(str(pdf_path))
    output_path.write_text(result.text_content, encoding="utf-8")

    print(f"Created baseline: {output_path}")


if __name__ == "__main__":
    main()
