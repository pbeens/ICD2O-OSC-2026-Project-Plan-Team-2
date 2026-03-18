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
2. Create a Markdown version in the same folder.
3. Preserve the document's structure using Markdown headings, lists, and tables where possible.
4. Remove structural noise such as repeated running headers, page numbers, and rotated sidebar artifacts.
5. Reconstruct the table of contents as a Markdown table if the PDF includes one.

## Ingestion Rule

For AI ingestion and document-loading workflows:
- Markdown is the ingestion format.
- PDF is the source/archive format.
- If `resources/name.md` exists, skip `resources/name.pdf`.
- Prefer loading `*.md` files and ignoring `*.pdf` files unless the original PDF is specifically needed for verification.

## Helper Utilities

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
