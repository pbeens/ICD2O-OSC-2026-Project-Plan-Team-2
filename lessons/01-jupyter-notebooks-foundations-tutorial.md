# Beginner Tutorial: Jupyter Notebook Foundations (Lesson 01)

## Purpose
This walkthrough teaches notebook mechanics before full dataset analysis.

This lesson assumes students may be completely new to coding. The goal is not speed. The goal is understanding the workspace and the meaning of the main words they will see.

## What Is a Jupyter Notebook?
A Jupyter Notebook is an interactive document with:
- Markdown cells (text/explanations)
- Code cells (Python commands)
- Output cells (results, tables, charts)

In plain language:
- A **Jupyter Notebook** is a digital worksheet where we can write explanations and run code in the same file.
- **Interactive** means we do not just read it. We can run parts of it and see results right away.
- **Python** is a programming language. It is the language we will use in these notebooks.

Many beginners are surprised that a notebook is not just one block of code. It is designed for step-by-step work. That is why it is useful for learning.

## Why It Is Useful
- Combines explanation + code + results in one place
- Easier for step-by-step learning
- Supports reproducible analysis when run top-to-bottom

**Reproducible** means that if someone else opens the notebook and follows the same steps, they should be able to get the same result.

## Vocabulary You Should Know Before Coding
- **Cell**: one block inside the notebook. Each cell has one job.
- **Markdown cell**: a text cell used for notes, titles, instructions, and explanations.
- **Code cell**: a cell that contains Python commands.
- **Output**: the result produced after running a code cell.
- **Kernel**: the background engine that runs the code in the notebook.
- **Runtime**: another word students may see in tools like Colab; it means the working environment that runs the code.
- **Library**: prewritten code that gives us useful tools.
- **Import**: the command that loads a library into the notebook so we can use it.

## Core Workflow Rules
- Run cells in order from top to bottom
- Use `Shift+Enter` to run a cell
- If you restart runtime/kernel, rerun all cells
- Keep imports near the top

Why these rules matter:
- Notebooks remember what has already been run.
- If you run a later cell first, it may depend on something that has not been created yet.
- Restarting the kernel clears the notebook's working memory, so variables and imported libraries need to be loaded again.

## Notebook Cells You Can Copy

### Cell 1 (Markdown)
```md
# Lesson 01: Jupyter Notebook Basics
Goal: Learn notebook workflow before full data analysis.
```

Why this cell matters:
- Markdown helps us label the notebook clearly.
- Good notebooks explain what they are doing, not just what they are typing.

### Cell 2 (Code)
```python
import pandas as pd
import plotly.express as px
print("Libraries loaded.")
```

Big picture:
- This cell loads the tools we need before we start working with data.

How it works:
- `pandas` is a library for working with tables.
- `plotly.express` is a library for making charts.
- `as pd` and `as px` create short nicknames so the code is easier to type.
- `print("Libraries loaded.")` displays a message so we know the cell ran successfully.

Important beginner note:
- Students do not need to know everything a library can do.
- At this stage, they only need to understand that libraries give us helpful tools we did not have to write ourselves.

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

Big picture:
- This cell creates a small practice table directly inside the notebook.

How it works:
- `sample` is the variable name. A **variable** is a label that stores a value in memory.
- `pd.DataFrame(...)` creates a **DataFrame**, which is a table in pandas.
- `"Category"` and `"Value"` are the column names.
- `["A", "B", "C"]` and `[10, 15, 8]` are the column values.
- Typing `sample` on the last line displays the table as output.

Plain-language reminder:
- A DataFrame is like a spreadsheet table inside Python.

### Cell 4 (Code)
```python
sample.head()
```

Big picture:
- This cell previews the top rows of the table.

How it works:
- `head()` is a **method**. A method is an action an object can perform.
- The parentheses `()` help show that something is being run.
- `sample.head()` usually shows the first five rows.

### Cell 5 (Code)
```python
sample.columns
```

Big picture:
- This cell checks the names of the columns in the table.

How it works:
- `columns` is a **property**. A property is information about an object.
- There are no parentheses because we are not asking the table to do an action.
- This is one of the easiest ways to check spelling before using a column name later.

Method vs property:
- Method = action, usually with parentheses, like `sample.head()`
- Property = information, usually without parentheses, like `sample.columns`

### Cell 6 (Code)
```python
fig = px.bar(sample, x="Category", y="Value", title="Sample Chart")
fig.show()
```

Big picture:
- This cell turns the table into a bar chart.

How it works:
- `px.bar(...)` creates a bar chart using the `plotly.express` library.
- `x="Category"` tells the chart which column to use on the horizontal axis.
- `y="Value"` tells the chart which column to use for bar height.
- `title="Sample Chart"` adds a chart title.
- `fig.show()` displays the chart.

Plain-language reminder:
- A chart is a visual output. It helps us compare information more quickly than reading raw numbers alone.

### Cell 7 (Markdown)
```md
## Reflection
- What is the difference between a markdown cell and a code cell?
- What happens if you run cells out of order?
- Why do we keep imports near the top?
```

Why this cell matters:
- Reflection helps students explain the workflow in words, not just copy steps.
- If a student can explain what a notebook is doing, they are more likely to troubleshoot it successfully.

## Troubleshooting Basics
- `NameError`: usually means a required cell was not run.
- Empty/old chart: rerun cells top-to-bottom.
- Wrong column name: check `sample.columns`.

More detail:
- **`NameError`** means Python does not recognize a name you used. Usually the variable or library was never created because an earlier cell was skipped.
- If output looks old or missing, the notebook may be out of order. Running from top to bottom fixes many beginner problems.
- If a column name does not work, check capitalization and spelling carefully. Computers treat `"Value"` and `"value"` as different names.

## What Students Should Be Able To Explain After This Lesson
- What a Jupyter Notebook is
- What a code cell does
- What a markdown cell does
- What `import` means
- What a library is
- What a DataFrame is at a beginner level
- Why cell order matters

## Before Lesson 02
Students should be able to:
- Create and run both markdown and code cells
- Restart and rerun notebook correctly
- Explain execution order in one sentence

## Alignment Notes
- Curriculum source: `resources/ICD2O_2023.md`
- Assessment source: `resources/growSuccess.md`
- Evidence collection: observations, conversations, student products
