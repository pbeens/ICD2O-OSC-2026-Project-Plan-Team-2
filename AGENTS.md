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
- Design notebooks for beginners using very small, sequential steps.
- Keep code cells to one task at a time (for example: conversion in one cell, charting in a later cell).
- Add a short markdown explanation before or after key operations so students know what is happening.
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

## Working Conventions For Agents
- Keep documentation up to date whenever new notebooks or data sources are added.
- Do not delete or overwrite user-created analysis without explicit request.
- Prefer small, traceable edits with clear commit messages.
- If a notebook is created or renamed, ensure its Colab footer link matches the new path.
- When uncertain about data licensing or source credibility, flag it in notes before use.

## Definition of Done For New Notebook Creation
- Notebook saved under `notebooks/` with clear name.
- Intro section completed (goal, sources, author/date).
- Core analysis cells run without obvious errors.
- Final Markdown cell includes a valid Colab link.
- Related dataset link is recorded in repository documentation.
