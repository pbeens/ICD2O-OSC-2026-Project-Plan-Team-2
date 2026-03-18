# Beginner Tutorial: Extreme Heat Events Data Analysis (ICD2O)

## Purpose
This walkthrough teaches the full beginner workflow without needing to read detailed theory inside the notebook.

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

## Step 1: Import Tools
Big picture: Load the libraries that handle tables and charts.

```python
import pandas as pd
import plotly.express as px
```

How it works:
- `pandas` is used for table-like data.
- `plotly.express` is used for quick, readable charts.

## Step 2: Load the CSV into a DataFrame
Big picture: Read the online CSV into a table we can work with.

```python
data_url = "https://www.canada.ca/content/dam/eccc/documents/csv/cesindicators/extreme-heat-events/2025/cumulative-days-extreme-heat.csv"
df = pd.read_csv(data_url)
display(df.head())
```

How it works:
- A **DataFrame** is a table in pandas (rows and columns).
- We name it `df` because that is the common short name for “data frame”.
- `df.head()` is a **method** (it uses parentheses) that shows top rows.

## Step 3: Check Column Names
Big picture: See what columns exist before cleaning.

```python
display(df.columns)
```

How it works:
- `df.columns` is a **property** (no parentheses).
- Property = information about the table.
- Method = an action the table performs.

## Step 4: Rename Columns for Clarity
Big picture: Replace long or unclear names with simpler names.

```python
df.columns = ["Trend", "Number of Stations", "Percentage"]
display(df.head())
```

How it works:
- Cleaner names make later code easier to read and debug.

## Step 5: View Full Table Before Cleaning
Big picture: Inspect rows to spot missing or invalid values.

```python
display(df)
```

How it works:
- We look for values that should be numbers but are text/blank.

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

## Step 7: Remove an Unwanted Row by Index
Big picture: Delete a row that should not be part of analysis.

```python
df = df.drop(index=1, errors="ignore").copy()
display(df)
```

How it works:
- `drop(index=1)` asks pandas to remove row index 1.
- `errors="ignore"` prevents a crash if that row is not present.

## Step 8: Convert a Column to Numeric
Big picture: Ensure chart values are real numbers.

```python
df["Number of Stations"] = pd.to_numeric(df["Number of Stations"], errors="coerce")
display(df.dtypes)
```

How it works:
- `pd.to_numeric(...)` converts text numbers to numeric type.
- `errors="coerce"` turns unconvertible values into `NaN`.

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

## Step 10: Interpret Results
Write 2-3 evidence-based observations:
- Which trend category is highest?
- Which is lowest?
- What might this suggest about extreme heat patterns?

## Checkpoint Questions
- What is a DataFrame?
- Why do we use the variable name `df`?
- Give one method and one property from this lesson.
- What does `NaN` mean?
- Why is `errors="ignore"` useful in `drop()`?

## Curriculum + Assessment Alignment
- Curriculum source: `resources/ICD2O_2023.md`
- Assessment source: `resources/growSuccess.md`
- Evidence types to collect: observations, conversations, student products
