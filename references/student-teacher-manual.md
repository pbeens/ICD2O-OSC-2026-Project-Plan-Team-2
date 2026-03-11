# ICD2O Data Analysis Manual (Student + Teacher)

Audience: Grade 10 ICD2O students with no prior Python or data analysis experience.  
Course context: Introductory, classroom-first, guided practice.

## Purpose
This manual supports a beginner pathway from:
1. understanding what data is,
2. reading and interpreting tables/charts,
3. running simple Python notebook code,
4. creating and explaining basic visualizations.

## Learning Outcomes
By the end of this sequence, students should be able to:
- describe rows, columns, variables, and observations,
- load a CSV dataset in a notebook,
- inspect data quality at a basic level (missing values, data types),
- create simple charts with Plotly Express,
- write short evidence-based conclusions from charts.

## Course Sequence (Recommended Start)
### Module 0: Importing and Library Setup (Start Here)
Student goals:
- Understand what `import` means in Python.
- Recognize the core libraries used in this course.
- Run import cells and confirm the notebook is ready.

Teacher focus:
- Explain libraries as "toolboxes" with simple examples.
- Standardize import names used in all class notebooks.
- Reinforce that imports are usually run once at the top of a notebook.

Activities:
- Mini-lesson on `import` vs `from ... import ...`.
- Guided setup cell:
  - `import pandas as pd`
  - `import plotly.express as px`
- Quick check: students run `pd.__version__` and create a tiny sample chart.

Deliverable:
- Notebook setup cell runs without errors and student can explain what `pd` and `px` represent.

### Module 1: Foundations
Student goals:
- Understand what a dataset is.
- Learn key terms: variable, row, column, category, numerical value.
- Identify responsible data use and interpretation limits.

Teacher focus:
- Establish classroom norms and vocabulary.
- Use non-technical examples before opening Python.
- Connect charts to curriculum expectations (statistics/data management basics).

Activities:
- Vocabulary mini-lesson and exit ticket.
- Read one small CSV table together (projector).
- Class discussion: "What claims can/can't we make from this data?"

Deliverable:
- 1-page concept check (definitions + simple interpretation questions).

### Module 2: First Notebook (Direct CSV Only)
Student goals:
- Open a notebook.
- Run cells safely in order.
- Load a CSV from URL.
- View first rows and create one bar chart.
- Understand what a DataFrame is and how `df` naming works.
- Explain `NaN`, `dropna()`, `drop(index=..., errors=...)`, and `copy()` at a beginner level.

Teacher focus:
- Model "run one cell at a time."
- Explain errors as normal feedback, not failure.
- Keep workflow procedural and repeatable.
- Use a short explanatory Markdown section above each code cell.

Activities:
- Guided run of `notebooks/csv/extreme-heat-events-exploration.ipynb`.
- Read and run the import setup cell:
  - `import pandas as pd`
  - `import plotly.express as px`
- Run a simplified load-and-preview cell that:
  - defines the dataset URL,
  - creates `df` with `pd.read_csv(...)`,
  - displays `df.head()`.
- Use the current guided steps:
  - Step 3: display column names with `df.columns`.
  - Step 4: rename unsuitable columns (very long name + `Unnamed` placeholders) to:
    - `Trend`
    - `Number of Stations`
    - `Percentage`
  - Step 5: display the full DataFrame (`display(df)`) so students can inspect what needs cleanup.
  - Step 6: remove incomplete rows with `df = df.dropna().copy()`, then remove row index `1` with `df = df.drop(index=1, errors="ignore").copy()`.
  - Step 7: convert `Number of Stations` to numeric with `pd.to_numeric(..., errors="coerce")`.
  - Step 8: build a bar chart with:
    - x-axis: `Trend`
    - y-axis: `Number of Stations`
- Label chart parts: title, x-axis, y-axis, and bar height meaning.
- Short write-up: "Which trend category has the most stations, and what does that suggest?"

Deliverable:
- Screenshot/export of first chart + 3-sentence interpretation.

Teacher script notes for Module 2:
- DataFrame language:
  - "A DataFrame is a table object in pandas."
  - "`df` is a short, common variable name for data frame."
  - "In `df.head()` and `df.dropna()`, `head`/`dropna` are methods (actions)."
  - "In `df.columns`, `columns` is a property/attribute (stored information)."
- Cleanup language:
  - "`NaN` means Not a Number, usually missing/invalid data."
  - "`dropna()` removes rows containing `NaN`."
  - "`index=1` targets row label 1."
  - "`errors=\"ignore\"` prevents a crash if that label is missing."
  - "`.copy()` creates an independent result for safer follow-up edits."
- Pacing/style language:
  - "Keep each code cell focused on one task only."
  - "Use a separate conversion cell before plotting when teaching data types."

## Teaching Notes
- Prefer direct CSV/Excel datasets for core lessons.
- Defer ZIP/spatial datasets to advanced extension only.
- Use consistent chart templates to reduce cognitive load.
- Assess interpretation quality more than coding sophistication early on.

## Assessment Framework (Simple)
- Knowledge: key vocabulary and concepts.
- Skills: loading data, basic chart creation, simple checks.
- Communication: clarity of chart interpretation.
- Application: connecting findings to real-world context.

## Next Sections To Build
1. Module 3: Cleaning basics (missing values, duplicates, filters).
2. Module 4: Comparing groups (bar charts, grouped summaries).
3. Module 5: Intro to relationships (scatter plot + trendline concept).
4. Culminating mini-project rubric (student + teacher versions).
