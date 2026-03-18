# ICD2O OSC 2026 Project Plan Team 2

Resource and analysis workspace for developing the ICD2O project plan.

## Project Goals
- Collect and organize links to relevant datasets and references.
- Build Jupyter notebooks for exploration, cleaning, analysis, and project planning evidence.
- Keep work reproducible and easy to open in both local Jupyter and Google Colab.

## Repository Structure
- `datasets/`: lightweight sample files, metadata notes, and data references.
- `notebooks/`: Jupyter notebooks organized by input format:
  - `notebooks/zip/`
  - `notebooks/csv/`
  - `notebooks/excel/`
  - `notebooks/json/`
- `references/`: source lists, summaries, and planning documents.
- `lesson-plans/`: 5E lesson plans based on selected beginner notebooks.
- `logs/` (optional): ingestion or processing notes.

Create folders as needed when they are first used.

## Python Setup
### 1) Install Python
Install Python 3.11+ and ensure `python` is available in your terminal.

Windows (example with winget):
```powershell
winget install -e --id Python.Python.3.11
```

Manual install:
- Download from `https://www.python.org/downloads/`
- During install, enable **Add Python to PATH**

### 2) Create and activate `.venv`
From the repository root:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run once:
```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

### 3) Install libraries
With `.venv` activated:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Core libraries used in notebooks include `pandas`, `numpy`, `plotly`, and `geopandas`.
The repository also uses `markitdown[pdf]` for PDF-to-text baseline extraction in the `resources/` workflow.

### 4) Start Jupyter
```powershell
jupyter lab
```

Open notebooks from `notebooks/`.

## Notebook Standard
Each notebook should include at the top:
- Title
- Objective
- Data source(s)
- Date/author

Each notebook should include at the bottom:

```md
---
### Open In Colab
[Open this notebook in Google Colab](https://colab.research.google.com/github/<OWNER>/<REPO>/blob/<BRANCH>/notebooks/<NOTEBOOK_FILE>.ipynb)
```

## Dataset Link Tracker
Dataset/resource intake is tracked in:

- `references/dataset-links.md`

## Classroom Manual
- `references/student-teacher-manual.md` (student/teacher guide for Grade 10 beginner workflow)

## Project Plan
- `Project Plan Team 2.md` (active front-end project plan document populated from the project plan template)

## Lesson Plans
- `lesson-plans/lesson-00-data-analysis-big-picture-5e.md` (big-picture intro to data analysis and IPO model)
- `lesson-plans/lesson-01-jupyter-notebooks-foundations-5e.md` (Jupyter workflow foundations)
- `lesson-plans/lesson-02-extreme-heat-events-5e.md` (first full beginner dataset analysis lesson)

## Resources Workflow
- `resources/README.md` (PDF-to-Markdown workflow and lesson-planning resource guidance)
- Resource files such as PDFs can be placed in `resources/` and a conversion request can be given to turn them into Markdown.
- After conversion, the original PDFs can be deleted if desired.
- Markdown files are usually better than PDFs for AI ingestion because the text is easier to parse, search, chunk, and reuse reliably.
- The PDF workflow also creates a MarkItDown baseline text file for fidelity checking against the cleaned Markdown output.

## Working Notes
- Keep documentation current when notebooks or data sources are added.
- Do not overwrite user-created analysis without explicit request.
- If data is downloaded/transformed, note notebook and output location.
- Flag uncertain licensing or source credibility before use.
