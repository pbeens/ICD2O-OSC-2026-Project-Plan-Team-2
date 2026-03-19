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

## Curriculum Source Of Truth
- The active curriculum document for this repository is `resources/ICD2O_2023.md`.
- The active assessment/pedagogy reference for this repository is `resources/growSuccess.md`.
- For lesson planning work, map expectations and learning goals to `resources/ICD2O_2023.md`, and align assessment/evaluation approaches with `resources/growSuccess.md`.
- Use `resources/5E Lesson Plan Template.md` as the lesson plan format template, and use both `resources/ICD2O_2023.md` and `resources/growSuccess.md` for lesson requirement content.
- Use `resources/Project Plan Template.md` as the template for the root-level project plan front-end document.
- The active root-level project plan document is `Project Plan Team 2.md`.
- Track curriculum coverage in `references/expectations-compliance.md`.
- Track teacher-facing assignment-design framework notes in `references/pact-framework.md`.

## Expected Repository Structure
- `datasets/`
  - Optional local sample files or metadata notes.
  - Prefer lightweight files and references over committing very large raw data.
- `notebooks/`
  - Jupyter notebooks (`.ipynb`) for each analysis topic.
  - Organize notebooks by source/input type when helpful, for example `notebooks/csv/`, `notebooks/excel/`, `notebooks/json/`, and `notebooks/zip/`.
- `lessons/`
  - Lesson plans, tutorials, assignments, and other lesson-specific teacher/student files.
- `references/`
  - Notes, summaries, source lists, and planning docs.
- `resources/`
  - Curriculum, policy, templates, and converted source/reference materials.
- `skills/`
  - Repository-local skills for specialized workflows.
- `utils/`
  - Helper scripts used for repository workflows such as PDF conversion checks.
- `logs/` (optional)
  - Data ingestion logs or processing notes.
- `README.md` (recommended)
  - High-level project summary and quick-start instructions.
- `_quarto.yml` / `index.qmd` / `styles.css` (optional)
  - Quarto site layer for publishing a curated teacher-facing view of selected repository content while keeping the existing Markdown and notebook files as the main editable sources.

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

## Beginner Tutorial Requirements
- Treat every beginner tutorial in `lessons/` as if the student may have zero prior exposure to programming or data-analysis vocabulary.
- Write beginner tutorials more like short book chapters than sparse lesson notes. Use connected explanatory paragraphs, transitions between sections, and enough narrative context that a student can read the tutorial straight through and understand the story of the lesson.
- Define unfamiliar terms the first time they appear in the tutorial, especially terms like Python, Jupyter Notebook, library, `import`, `pandas`, `plotly`, DataFrame, variable, method, property, CSV, dataset, column, row, index, kernel/runtime, and `NaN`.
- Do not assume students know what a tool is just because it appears in code. Add a plain-language explanation before or immediately after the code example.
- For each step in a beginner tutorial, include:
  - a short big-picture explanation of why the step exists,
  - the code or concept,
  - a plain-language explanation of what key commands/terms mean,
  - and why that step matters to the overall workflow.
- Prefer over-explaining unfamiliar vocabulary rather than leaving gaps that force a student to guess.
- When using code examples, explain nicknames and shorthand such as `as pd`, `as px`, and `df`.
- Tutorials should help a student understand both what to type and what the words mean.
- When possible, include chapter-style elements such as a clear purpose, a conceptual introduction, worked explanations, bridges to the next lesson, and reflection questions that revisit the main ideas.

## Required Colab Link Footer (Every Notebook)
Add a final Markdown cell at the bottom of each notebook:

```md
---
### Open In Colab
[Open this notebook in Google Colab](https://colab.research.google.com/github/<OWNER>/<REPO>/blob/<BRANCH>/<NOTEBOOK_PATH>)
```

Replace placeholders:
- `<OWNER>`: GitHub username or org
- `<REPO>`: repository name
- `<BRANCH>`: usually `main`
- `<NOTEBOOK_PATH>`: exact notebook path relative to the repository root, for example `notebooks/csv/02-extreme-heat-events-exploration.ipynb`

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
- For ICD2O lesson requirements, use `resources/ICD2O_2023.md` as the authoritative curriculum reference unless the user explicitly provides a replacement.
- For assessment and evaluation design in lesson plans, use `resources/growSuccess.md` as the authoritative policy reference unless the user explicitly provides a replacement.
- In lesson plans, format `Curriculum Expectations` as a bulleted list, with one expectation per bullet.
- In lesson plans, format `Learning Goals` as a bulleted list, with one goal per bullet.
- In lesson plans, format `Materials/Resources` as a bulleted list, with one material/resource per bullet.
- Treat the lesson plan as the front-facing anchor document for each lesson. It should give the big picture of what the lesson is for, what students will do, what resources are used, and how the related lesson files fit together.
- At the top of every lesson-related file (`lesson plan`, `tutorial`, `assignment`, and lesson-specific notebook notes when applicable), include a `Related Lesson Files` section that links to the other documents for that lesson.
- In `Related Lesson Files`, list the document types in this order: `Lesson plan`, `Tutorial`, `Notebook`, `Assignment`.
- If a related file does not exist yet, write `not yet created` instead of omitting it.
- In every lesson plan, include an explicit teacher-facing sequence that states what to open first after reviewing the lesson plan (normally the companion tutorial, then the notebook if one exists).
- In every lesson plan, explicitly encourage the teacher to read through the companion tutorial before commencing the assignment or notebook-based task so the teacher has the full explanatory arc before students begin working.
- In every lesson plan, include a clear ordered activity list so the classroom process is visible at a glance.
- For beginner lessons, keep the 5E lesson plan concise and create a separate companion tutorial file in `lessons/` for detailed, step-by-step concept and code explanations.
- Store lesson plan and companion tutorial in the same `lessons/` folder using matched names when possible (for example, `01-topic-lesson-plan.md` and `01-topic-tutorial.md`).
- Lesson assignment filenames should follow the same sequence prefix pattern: `NN-topic-assignment.md`.
- In the 5E lesson plan `Materials/Resources`, include a bullet linking to the companion tutorial file.
- In every lesson assignment, explain clearly how the notebook is incorporated into the work. If students are expected to run, read, modify, submit from, or take evidence from a Jupyter notebook, say so directly in the assignment instructions rather than assuming the notebook relationship is obvious.
- When a lesson uses a notebook, keep the document flow explicit and consistent: `Lesson Plan -> Tutorial -> Notebook -> Assignment`. The lesson plan should frame that flow, the tutorial should prepare the teacher and student for the notebook work, and the assignment should tell students exactly how the notebook fits into the task.
- Use sequential lesson numbering for pathway clarity (for example: `Lesson 00` big-picture foundations, `Lesson 01` tools/workflow, then dataset analysis lessons).
- Lesson plan filenames should start with the lesson number: `NN-topic-lesson-plan.md` and `NN-topic-tutorial.md`.
- Lesson plan header format should be `# Lesson NN: <Title>[^1]` (lesson number at the beginning; do not include `5E` in the header line).
- Use `Lesson 00` only for explicit onboarding/foundational context-setting lessons; otherwise begin sequence at `Lesson 01`.
- Keep `Project Plan Team 2.md` synchronized with lesson-plan sequencing, major deliverables, and assessment approach whenever lessons are added, renamed, or re-scoped.
- When lesson sequence changes, update both `Project Plan Team 2.md` and the lesson list in `README.md` in the same edit pass.
- When lesson mappings change, update `references/expectations-compliance.md` in the same edit pass, including covered and not-yet-covered expectations.
- In `Project Plan Team 2.md`, maintain a `% of Expectations Covered` metric that matches `references/expectations-compliance.md` (specific expectations basis).
- In `Project Plan Team 2.md`, place document links inside existing sections (for example: compliance links in Curriculum Alignment, lesson links in Deliverables, and file/resource links in Resources & Risk), instead of creating an extra standalone links section.
- In teacher-facing front documents (`Project Plan Team 2.md` and `README.md`), include a short document-flow description for `Lesson Plan -> Tutorial -> Notebook -> Assignment` and state the recommended use order explicitly.
- If the repository uses a Quarto site layer, keep `_quarto.yml` synchronized with the curated set and order of published lesson, reference, and notebook pages whenever that sequence changes.
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
- `create-assignment`: Generate a paste-ready prompt for the Assignment Strengthener GPT using a lesson plan/tutorial and current curriculum coverage context. Use when the user asks to create or strengthen an assignment for a lesson, topic, or notebook. (file: `skills/create-assignment/SKILL.md`)

### How to use repository skills
- Discovery: Check `skills/` for repository-local skills before inventing a custom workflow for specialized tasks.
- Trigger rule: If the user explicitly mentions a repository skill by name, or the task clearly matches its description, open that skill's `SKILL.md` and follow it.
- Scope: Use only the parts of the skill that are necessary for the current request; do not load unrelated references or scripts unless the skill requires them.
- Path resolution: Resolve any relative paths in a repository skill relative to that skill's own folder first.
- Fallback: If a skill is missing files, does not fit the task cleanly, or conflicts with higher-priority instructions, state that briefly and continue with the best direct approach.
