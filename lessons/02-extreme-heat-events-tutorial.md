# Beginner Tutorial: Extreme Heat Events Data Analysis (ICD2O)

## Purpose
This walkthrough teaches the full beginner workflow without needing to read detailed theory inside the notebook.

This tutorial is written for students who may be seeing terms like `pandas`, DataFrame, method, property, and `NaN` for the first time. It explains the big picture first, then the technical details.

## What You Will Learn
- What a DataFrame is and why we use `df`
- The difference between a method and a property
- What `NaN` means in plain language
- How to clean simple data step by step
- How to make and interpret a bar chart

## Dataset
- Topic: Extreme heat events in Canada
- Format: Direct CSV (beginner-friendly)
- Source: Government of Canada (CSV URL used directly in code)

Important vocabulary before you start:
- **Dataset**: a collection of related information
- **CSV**: a table file where values are separated by commas
- **Row**: one record in the table
- **Column**: one type of information in the table
- **DataFrame**: the pandas version of a table
- **Library**: extra prewritten code we can import and use

## Before The Code: What Are `pandas` And `plotly`?
- `pandas` is a Python library for working with tables of data.
- `plotly` is a Python library for making charts.
- A **library** is a collection of prewritten code tools.
- We use libraries because they save time and give us commands built for common tasks.

Think of it this way:
- Python is the language.
- `pandas` is a toolbox for table work.
- `plotly` is a toolbox for charts.

## Step 1: Import Tools
Big picture: Load the libraries that handle tables and charts.

```python
import pandas as pd
import plotly.express as px
```

How it works:
- `import` means "load this library so I can use it in this notebook."
- `pandas` is used for table-like data.
- `plotly.express` is used for quick, readable charts.
- `as pd` gives `pandas` a short nickname.
- `as px` gives `plotly.express` a short nickname.

Why this matters:
- Without importing the libraries first, later code like `pd.read_csv(...)` or `px.bar(...)` would not work.

## Step 2: Load the CSV into a DataFrame
Big picture: Read the online CSV into a table we can work with.

```python
data_url = "https://www.canada.ca/content/dam/eccc/documents/csv/cesindicators/extreme-heat-events/2025/cumulative-days-extreme-heat.csv"
df = pd.read_csv(data_url)
display(df.head())
```

How it works:
- `data_url` is a variable. A **variable** stores a value using a name.
- The string in quotes is the web address of the CSV file.
- `pd.read_csv(data_url)` tells pandas to read the CSV from that address.
- A **DataFrame** is a table in pandas (rows and columns).
- We name it `df` because that is the common short name for “data frame”.
- `df.head()` is a **method** (it uses parentheses) that shows top rows.
- `display(...)` shows the result in a clear notebook-friendly way.

Why we do this:
- Loading the dataset is the moment where raw information becomes something we can inspect and analyze in Python.

## Step 3: Check Column Names
Big picture: See what columns exist before cleaning.

```python
display(df.columns)
```

How it works:
- `df.columns` is a **property** (no parentheses).
- Property = information about the table.
- Method = an action the table performs.
- Column names matter because we must spell them correctly when we refer to them later in code.

## Step 4: Rename Columns for Clarity
Big picture: Replace long or unclear names with simpler names.

```python
df.columns = ["Trend", "Number of Stations", "Percentage"]
display(df.head())
```

How it works:
- Cleaner names make later code easier to read and debug.
- This does not change the meaning of the data. It only changes the labels we use inside the notebook.
- Clear names are especially helpful for beginners because shorter labels reduce typing mistakes.

## Step 5: View Full Table Before Cleaning
Big picture: Inspect rows to spot missing or invalid values.

```python
display(df)
```

How it works:
- We look for values that should be numbers but are text/blank.
- This is an important habit in data analysis: look at the data before making assumptions about it.

## Step 6: Remove Missing Rows (`NaN`)
Big picture: Remove rows with missing values.

```python
df = df.dropna().copy()
display(df)
```

How it works:
- `NaN` means “Not a Number” (usually blank or missing data).
- `dropna()` removes rows containing missing values.
- `copy()` creates a clean independent result so later edits are safer.

Why this matters:
- If missing values stay in the table, they can cause errors or misleading results later.
- Cleaning is not about making the data look nice. It is about making the data usable and trustworthy enough for the current task.

## Step 7: Remove an Unwanted Row by Index
Big picture: Delete a row that should not be part of analysis.

```python
df = df.drop(index=1, errors="ignore").copy()
display(df)
```

How it works:
- `drop(index=1)` asks pandas to remove row index 1.
- `errors="ignore"` prevents a crash if that row is not present.
- The **index** is the row label/position pandas uses to identify rows.
- `errors="ignore"` is useful for beginners because it makes the notebook more forgiving when the table is slightly different than expected.

## Step 8: Convert a Column to Numeric
Big picture: Ensure chart values are real numbers.

```python
df["Number of Stations"] = pd.to_numeric(df["Number of Stations"], errors="coerce")
display(df.dtypes)
```

How it works:
- `pd.to_numeric(...)` converts text numbers to numeric type.
- `errors="coerce"` turns unconvertible values into `NaN`.
- This is useful because charts and calculations need real numbers, not number-looking text.
- If a value cannot become a number, `errors="coerce"` marks it as missing instead of crashing the notebook.

## Step 9: Build the Bar Chart
Big picture: Visualize stations by trend category.

```python
fig = px.bar(
    df,
    x="Trend",
    y="Number of Stations",
    title="Extreme Heat Events in Canada: Number of Stations by Trend",
    labels={"Trend": "Trend Category", "Number of Stations": "Number of Stations"}
)
fig.show()
```

How it works:
- `x` chooses category labels.
- `y` chooses numeric values.
- The chart helps us compare categories quickly.
- The variable `fig` stores the chart object before it is shown.
- `fig.show()` displays the finished chart in the notebook.

## Step 10: Interpret Results
Write 2-3 evidence-based observations:
- Which trend category is highest?
- Which is lowest?
- What might this suggest about extreme heat patterns?

Reminder:
- An **observation** describes what the chart shows.
- An **interpretation** explains what that evidence might mean.
- Students should try to mention the actual categories or values they see, not just say "the chart is interesting."

## Checkpoint Questions
- What is a DataFrame?
- Why do we use the variable name `df`?
- Give one method and one property from this lesson.
- What does `NaN` mean?
- Why is `errors="ignore"` useful in `drop()`?

## Beginner Summary
- `pandas` helps us work with tables.
- A DataFrame is a table in `pandas`.
- `df` is just a short variable name for that table.
- Methods do actions, and properties give information.
- `NaN` means missing or unusable data.
- Cleaning comes before charting because charts are only as good as the data behind them.

## Curriculum + Assessment Alignment
- Curriculum source: `resources/ICD2O_2023.md`
- Assessment source: `resources/growSuccess.md`
- Evidence types to collect: observations, conversations, student products
