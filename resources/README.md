# Resources Workflow

This folder stores lesson-planning resources, policy documents, templates, and Markdown conversions made from PDFs.

## Purpose

Use `resources/` for:
- source PDFs
- Markdown versions of PDFs for easier ingestion
- lesson-planning templates
- supporting classroom reference material

Keep converted Markdown files beside their source PDFs when practical.

Examples:
- `resources/growSuccess.pdf`
- `resources/growSuccess.md`

## PDF to Markdown Workflow

When converting a PDF in this repository:

1. Put the source PDF in `resources/`.
2. Create a MarkItDown baseline text file in the same folder.
3. Create a cleaned Markdown version in the same folder.
4. Preserve the document's structure using Markdown headings, lists, and tables where possible.
5. Remove structural noise such as repeated running headers, page numbers, and rotated sidebar artifacts.
6. Reconstruct the table of contents as a Markdown table if the PDF includes one.
7. Compare the cleaned Markdown against the MarkItDown baseline to help detect missing content.
8. Run the structure check so PDF TOC headings are confirmed to exist as Markdown headings, not just as plain body text.

## Ingestion Rule

For AI ingestion and document-loading workflows:
- Markdown is the ingestion format.
- PDF is the source/archive format.
- If `resources/name.md` exists, skip `resources/name.pdf`.
- Prefer loading `*.md` files and ignoring `*.pdf` files unless the original PDF is specifically needed for verification.

## Helper Utilities

Create a MarkItDown baseline text file from a PDF:

```bash
python3 utils/generate_markitdown_baseline.py resources/<file>.pdf
```

This produces:

```text
resources/<file>.markitdown.txt
```

Use this baseline text file as a fidelity reference while reviewing the cleaned Markdown output.

Validate PDF TOC headings against the Markdown structure:

```bash
python3 utils/check_pdf_conversion_structure.py resources/<file>.pdf resources/<file>.md
```

This catches problems where a heading such as `Strand A` or `A1` is present only as paragraph text instead of a real Markdown heading.

Check for rotated-sidebar / word-salad noise:

```bash
python3 utils/check_noise.py resources/<file>.md
```

Optionally strip detected noise in place:

```bash
python3 utils/check_noise.py resources/<file>.md --fix
```

Apply a light formatting cleanup pass:

```bash
python3 utils/fix_markdown_lints.py resources/<file>.md
```

## Related Skill

The repository-local skill for this workflow is:

- `skills/pdf2md-document-restoration/SKILL.md`

Use that skill when the task is to convert a PDF into clean, ingestion-friendly Markdown.
