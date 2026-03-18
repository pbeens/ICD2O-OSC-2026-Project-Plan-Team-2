# Beginner Tutorial: Jupyter Notebook Foundations (Lesson 01)

## Purpose
This walkthrough teaches notebook mechanics before full dataset analysis.

## What Is a Jupyter Notebook?
A Jupyter Notebook is an interactive document with:
- Markdown cells (text/explanations)
- Code cells (Python commands)
- Output cells (results, tables, charts)

## Why It Is Useful
- Combines explanation + code + results in one place
- Easier for step-by-step learning
- Supports reproducible analysis when run top-to-bottom

## Core Workflow Rules
- Run cells in order from top to bottom
- Use `Shift+Enter` to run a cell
- If you restart runtime/kernel, rerun all cells
- Keep imports near the top

## Notebook Cells You Can Copy

### Cell 1 (Markdown)
```md
# Lesson 01: Jupyter Notebook Basics
Goal: Learn notebook workflow before full data analysis.
```

### Cell 2 (Code)
```python
import pandas as pd
import plotly.express as px
print("Libraries loaded.")
```

### Cell 3 (Code)
```python
sample = pd.DataFrame(
    {
        "Category": ["A", "B", "C"],
        "Value": [10, 15, 8]
    }
)
sample
```

### Cell 4 (Code)
```python
sample.head()
```

### Cell 5 (Code)
```python
sample.columns
```

### Cell 6 (Code)
```python
fig = px.bar(sample, x="Category", y="Value", title="Sample Chart")
fig.show()
```

### Cell 7 (Markdown)
```md
## Reflection
- What is the difference between a markdown cell and a code cell?
- What happens if you run cells out of order?
- Why do we keep imports near the top?
```

## Troubleshooting Basics
- `NameError`: usually means a required cell was not run.
- Empty/old chart: rerun cells top-to-bottom.
- Wrong column name: check `sample.columns`.

## Before Lesson 02
Students should be able to:
- Create and run both markdown and code cells
- Restart and rerun notebook correctly
- Explain execution order in one sentence

## Alignment Notes
- Curriculum source: `resources/ICD2O_2023.md`
- Assessment source: `resources/growSuccess.md`
- Evidence collection: observations, conversations, student products
