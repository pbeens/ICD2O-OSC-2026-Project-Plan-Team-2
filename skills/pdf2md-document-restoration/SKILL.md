---
name: PDF2MD Document Restoration
description: High-fidelity conversion of PDF documents to Markdown for this repository.
---

# PDF2MD Document Restoration

This skill is for converting PDF documents in this repository into clean, ingestion-friendly Markdown files.

Use it for:
- government policy documents
- curriculum and classroom resources
- technical manuals
- academic or reference PDFs

The goal is a single high-quality Markdown output, not a benchmark or comparison between multiple conversion methods.

## Repository Workflow

### Input
- Source PDFs are typically stored in `resources/`.

### Output
- Save the Markdown file beside the PDF in `resources/` unless the user asks for a different location.
- Keep the base filename aligned where practical, for example:
  - `resources/growSuccess.pdf`
  - `resources/growSuccess.md`

## Core Rules

### 1. No summarization
- Preserve all meaningful content.
- Do not omit sections to save time or space.
- Remove only structural noise such as repeated running headers, page numbers, and rotated sidebar artifacts.

### 2. Semantic Markdown only
- Use valid GitHub Flavored Markdown.
- Map visible document hierarchy into headings such as `#`, `##`, and `###`.
- Convert lists into Markdown lists.
- Convert tables into Markdown tables when practical.
- Preserve footnotes, citations, and publication metadata where present.

### 3. Keep the document readable for ingestion
- Merge broken OCR line wraps into paragraphs.
- Remove duplicated headings caused by page headers.
- Reconstruct the table of contents as a Markdown table when the PDF provides one.
- Prefer clean structure over verbatim layout noise.

## Structural Noise Rules

Structural noise removal takes precedence over literal layout fidelity.

Remove:
- page numbers that interrupt flow
- repeated running headers/footers
- duplicated section titles caused by page templates
- rotated sidebar word-salad

### Rotated Sidebar Hard Rule

Any sequence of 3 or more consecutive lines where each line contains only a single character is noise and must be removed.

After conversion, run:

```bash
python3 utils/check_noise.py <markdown_file>
```

The file must pass with exit code `0`.

## Required QA Before Finishing

Before considering the conversion done:
1. Confirm the file contains Markdown headings.
2. Confirm the table of contents has been reconstructed if the PDF includes one.
3. Run `python3 utils/check_noise.py <markdown_file>` and confirm there are no noise runs.
4. Skim the top, one or two middle sections, and the end for extraction artifacts.

Optional cleanup:

```bash
python3 utils/fix_markdown_lints.py <markdown_file>
```

Use this only as a final formatting pass. Do not rely on it to repair content loss or major structural problems.

## Large Document Protocol

For large PDFs:
- map the section structure first
- process the whole document in contiguous order
- do not stop halfway through the file
- if a perfect one-pass cleanup is not realistic, produce a complete first-pass Markdown file and then do targeted cleanup passes

## When to Use This Skill

Use this skill when the user asks to:
- convert a PDF to Markdown
- make a PDF easier to ingest
- clean a raw PDF extraction
- prepare a policy or classroom resource for later lesson-plan work
