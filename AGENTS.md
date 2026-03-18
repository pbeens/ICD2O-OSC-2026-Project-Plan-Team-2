# AGENTS.md

## Repository Overview
- Name: `ICD2O OSC 2026 Project Plan Team 2`
- Primary use: Resource and analysis workspace for developing the ICD2O project plan.
- Main collaborators:
  - Peter (repository owner/maintainer)
  - Yolanda (shares dataset/resource links)
- Current state (as of 2026-03-11): repository initialized for planning work; content will be added over time.

## Project Goals For This Repo
- Collect and organize links to relevant datasets and references.
- Build Jupyter notebooks for exploration, cleaning, analysis, and project planning evidence.
- Keep work reproducible and easy to open in both local Jupyter and Google Colab.

## Expected Repository Structure
- `datasets/`
  - Optional local sample files or metadata notes.
  - Prefer lightweight files and references over committing very large raw data.
- `notebooks/`
  - Jupyter notebooks (`.ipynb`) for each analysis topic.
- `references/`
  - Notes, summaries, source lists, and planning docs.
- `logs/` (optional)
  - Data ingestion logs or processing notes.
- `README.md` (recommended)
  - High-level project summary and quick-start instructions.

Create folders as needed when first used. Keep names clear and topic-based.

## Dataset Link Intake Workflow
When Yolanda sends a new dataset/resource link:
1. Add it to a tracking table (in `README.md` or `references/dataset-links.md`).
2. Record:
   - Source name
   - URL
   - Date received
   - License/usage notes (if available)
   - Intended use in project plan
3. If data is downloaded/transformed, document notebook and output location.

## Notebook Standards
- Store notebooks in `notebooks/`.
- Use descriptive file names, for example:
  - `notebooks/demographics-exploration.ipynb`
  - `notebooks/school-survey-cleaning-v1.ipynb`
- Start each notebook with:
  - Title
  - Objective
  - Dataset description (what the file contains and what each row represents)
  - Data source(s)
  - Date/author
- End each notebook with a Colab launch link section.

## Beginner Classroom Notebook Requirements
- Use direct CSV or Excel sources only for beginner classroom notebooks.
- Do not use ZIP-based ingestion in the beginner workflow.
- Design notebooks for beginners using very small, sequential steps.
- Keep code cells to one task at a time (for example: conversion in one cell, charting in a later cell).
- Add a short markdown explanation before or after key operations so students know what is happening.
- For each step, start the markdown with a short big-picture explanation of what the following code cell does, then follow with the technical details of how the code works.
- Include early vocabulary support:
  - what a DataFrame is,
  - why `df` is used as the table variable name,
  - the difference between methods (for example `df.head()`) and properties (for example `df.columns`).
- When cleaning data, explain `NaN` in plain language and explain commands used (for example `dropna()`, `drop(index=...)`, `errors="ignore"`, `copy()`).
- Avoid unnecessary transformation steps; only include cleanup logic that is actually needed by the current dataset.

## Required Colab Link Footer (Every Notebook)
Add a final Markdown cell at the bottom of each notebook:

```md
---
### Open In Colab
[Open this notebook in Google Colab](https://colab.research.google.com/github/<OWNER>/<REPO>/blob/<BRANCH>/notebooks/<NOTEBOOK_FILE>.ipynb)
```

Replace placeholders:
- `<OWNER>`: GitHub username or org
- `<REPO>`: repository name
- `<BRANCH>`: usually `main`
- `<NOTEBOOK_FILE>`: exact notebook filename

For this repository, use:
- `<OWNER>` = `pbeens`
- `<REPO>` = `ICD2O-OSC-2026-Project-Plan-Team-2`
- `<BRANCH>` = `main`

Colab link validation technique:
1. Build the Colab URL with the exact GitHub owner/repo/path (do not use local profile names like `Peter` unless that is the real GitHub owner).
2. Convert it to the matching GitHub URL and open it in a browser:
   - `https://github.com/pbeens/ICD2O-OSC-2026-Project-Plan-Team-2/blob/main/notebooks/<path>.ipynb`
3. If GitHub opens the notebook file successfully, the Colab link should resolve.
4. If Colab shows a `404` from `api.github.com/repos/...`, re-check owner/repo spelling and branch name first.

## Working Conventions For Agents
- Keep documentation up to date whenever new notebooks or data sources are added.
- Do not delete or overwrite user-created analysis without explicit request.
- Prefer small, traceable edits with clear commit messages.
- If a notebook is created or renamed, ensure its Colab footer link matches the new path.
- Keep keyword sections alphabetized by keyword name (for example, `## Keywords` in reference manuals).
- When uncertain about data licensing or source credibility, flag it in notes before use.
- When running Python commands in this repository, prefer the project virtual environment at `.venv` when it exists.
- For files in `resources/`, treat Markdown as the ingestion format and PDF as the source/archive format.
- If both `resources/name.md` and `resources/name.pdf` exist, prefer the Markdown file for AI ingestion and skip the PDF unless the original document is needed for verification.
- Use `resources/5E Lesson Plan Template.md` as the default template for all lesson plan creation unless the user explicitly requests a different format.
- For PDF-to-Markdown work, generate a MarkItDown baseline text file (`name.markitdown.txt`) beside the PDF and use it as a fidelity reference for checking omissions in the cleaned Markdown output.
- For PDF-to-Markdown work, also run `utils/check_pdf_conversion_structure.py` so PDF TOC headings are verified as real Markdown headings. A conversion should not be accepted if major headings only survived as body text.

## Definition of Done For New Notebook Creation
- Notebook saved under `notebooks/` with clear name.
- Intro section completed (goal, sources, author/date).
- Core analysis cells run without obvious errors.
- Final Markdown cell includes a valid Colab link.
- Related dataset link is recorded in repository documentation.

## Repository Skills
A repository-local skill is a set of instructions stored under `skills/` that agents should use when the task clearly matches the skill.

### Available repository skills
- `pdf2md-document-restoration`: High-fidelity conversion and cleanup of PDF documents into Markdown for this repository, especially for government documents, curriculum resources, technical manuals, and academic references. Use when the user wants a PDF made easier to ingest or reuse in lesson-planning work. The related helper utilities are `utils/generate_markitdown_baseline.py`, `utils/check_pdf_conversion_structure.py`, `utils/check_noise.py`, and `utils/fix_markdown_lints.py`. (file: `skills/pdf2md-document-restoration/SKILL.md`)

### How to use repository skills
- Discovery: Check `skills/` for repository-local skills before inventing a custom workflow for specialized tasks.
- Trigger rule: If the user explicitly mentions a repository skill by name, or the task clearly matches its description, open that skill's `SKILL.md` and follow it.
- Scope: Use only the parts of the skill that are necessary for the current request; do not load unrelated references or scripts unless the skill requires them.
- Path resolution: Resolve any relative paths in a repository skill relative to that skill's own folder first.
- Fallback: If a skill is missing files, does not fit the task cleanly, or conflicts with higher-priority instructions, state that briefly and continue with the best direct approach.
