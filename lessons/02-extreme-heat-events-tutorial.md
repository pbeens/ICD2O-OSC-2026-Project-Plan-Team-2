# Beginner Tutorial: Extreme Heat Events Data Analysis (ICD2O)

## Related Lesson Files
- Lesson plan: [02-extreme-heat-events-lesson-plan.md](02-extreme-heat-events-lesson-plan.md)
- Tutorial: [02-extreme-heat-events-tutorial.md](02-extreme-heat-events-tutorial.md)
- Notebook: [../notebooks/csv/02-extreme-heat-events-exploration.ipynb](../notebooks/csv/02-extreme-heat-events-exploration.ipynb)
- Assignment: not yet created

## Chapter Purpose
This chapter is the first full beginner data-analysis walkthrough in the course. In Lesson 00, students learned the big picture of analysis through the IPO model. In Lesson 01, they learned what a notebook is and how code cells work. Now they are ready to combine those ideas and move through a real workflow from beginning to end.

This tutorial is intentionally more descriptive than a set of notebook notes. It is written so a beginner can read it almost like a textbook chapter. The goal is not only to tell students what to type, but also to explain what the words mean, why each step happens, and how the steps connect into a larger process.

## The Question Behind The Lesson
Every data-analysis lesson should begin with a question. In this case, the question is related to extreme heat events in Canada. A useful classroom version of the question might be:

> What patterns can we see in extreme heat event data, and what might those patterns suggest?

That question matters because data analysis is never just about opening a file. It is about using information to understand something.

## The Dataset
This lesson uses a direct CSV file from a Government of Canada source.

Important vocabulary:
- **Dataset**: a collection of related information
- **CSV**: a table file where values are separated by commas
- **Row**: one record in the table
- **Column**: one category of information in the table

When the CSV is loaded into `pandas`, it becomes a **DataFrame**, which is `pandas`' table structure.

## Before The Code: The Main Tools
This lesson uses two Python libraries:

- `pandas`
- `plotly.express`

Students should understand these at a beginner level before moving on.

### What Is Python?
**Python** is the programming language used in this course. A programming language is a formal way of writing instructions that a computer can follow.

### What Is A Library?
A **library** is a collection of prewritten code tools. Libraries save time because programmers do not have to build every tool themselves from scratch.

### What Is `pandas`?
`pandas` is a Python library used for working with tables of data. It helps students:
- load data,
- inspect rows and columns,
- clean missing values,
- rename columns,
- and transform tables into forms that are easier to analyze.

### What Is `plotly.express`?
`plotly.express` is a Python library used for making charts. It helps students turn data into visual outputs that are easier to compare and explain.

An easy way to remember the tools is this:
- Python is the language
- `pandas` is the table toolbox
- `plotly` is the chart toolbox

## The Workflow We Will Follow
This lesson follows a beginner-friendly sequence:
1. import the tools
2. load the CSV
3. inspect the table
4. clean the data
5. convert values when needed
6. build a chart
7. interpret the result

This structure is important. It reminds students that the chart comes near the end, not at the beginning.

## Step 1: Import The Tools
The first step in many notebooks is to import the libraries the lesson needs.

```python
import pandas as pd
import plotly.express as px
```

Here is what each part means:
- `import` means "load this library so I can use it"
- `pandas` is the full library name
- `as pd` gives it a short nickname
- `plotly.express` is the charting library
- `as px` gives it a short nickname too

These short nicknames are common in beginner and professional notebooks. They make the code shorter and easier to read after students become familiar with them.

This step belongs to the **Input** part of IPO because it prepares the tools for the work ahead.

## Step 2: Load The CSV Into A DataFrame
Once the tools are ready, the next step is to bring the dataset into the notebook.

```python
data_url = "https://www.canada.ca/content/dam/eccc/documents/csv/cesindicators/extreme-heat-events/2025/cumulative-days-extreme-heat.csv"
df = pd.read_csv(data_url)
display(df.head())
```

This short block introduces several important ideas.

### `data_url`
`data_url` is a **variable**. A variable is a name that stores a value in memory. In this case, the value is the web address of the CSV file.

### `pd.read_csv(data_url)`
This tells `pandas` to read the CSV from the web address and turn it into a table.

### `df`
The name `df` stands for **data frame**. It is a very common beginner and professional nickname for a DataFrame.

### DataFrame
A **DataFrame** is a table in `pandas`. It has rows and columns, much like a spreadsheet.

### `df.head()`
`head()` is a **method**. A method is an action an object performs. `df.head()` shows the first few rows, which helps students inspect the data without printing the full table.

### `display(...)`
`display(...)` is a notebook-friendly way to show the output clearly.

This step is important because it turns a distant file on the internet into a table the notebook can actually work with.

## Step 3: Check The Column Names
Before students clean or chart the data, they should see what columns exist.

```python
display(df.columns)
```

This introduces the idea of a **property**.

- A **method** does something
- A **property** tells us information

`df.columns` is a property because it gives information about the table. It does not perform an action in the same way that `df.head()` does.

This step matters because students need exact column names later. If the column names are long or awkward, students may make spelling mistakes when writing code.

## Step 4: Rename The Columns For Clarity
When column names are unclear or inconvenient, students can rename them.

```python
df.columns = ["Trend", "Number of Stations", "Percentage"]
display(df.head())
```

This means the notebook is replacing the current column labels with clearer ones.

That does **not** change the meaning of the data. It only changes how the notebook refers to those columns.

This is helpful because:
- shorter names are easier to type,
- clearer names are easier to read,
- and simpler labels reduce beginner errors.

## Step 5: Inspect The Full Table
Before cleaning, students should pause and look at the table more carefully.

```python
display(df)
```

This is part of the **Process** stage of IPO. It may seem passive, but it is a real analytic action. Students are checking whether the data looks complete and usable.

This step builds a valuable habit:

> Look at the data before changing the data.

That habit helps prevent blind editing.

## Step 6: Remove Missing Values
Sometimes datasets contain missing or unusable values. In data analysis, those often appear as `NaN`.

```python
df = df.dropna().copy()
display(df)
```

### What `NaN` Means
`NaN` stands for **Not a Number**. In beginner-friendly language, it often means a value is missing, blank, or not usable as a real number.

### What `dropna()` Does
`dropna()` removes rows that contain missing values.

### Why `copy()` Is Used
`copy()` creates a separate cleaned result so later edits are safer and clearer.

This matters because charts and calculations can become confusing or unreliable if missing values are left in place.

Students should understand that cleaning is not cosmetic. It is part of making the data trustworthy enough for the task.

## Step 7: Remove An Unwanted Row By Index
Sometimes a row should not be part of the analysis even if it is not technically blank.

```python
df = df.drop(index=1, errors="ignore").copy()
display(df)
```

### What Is The Index?
The **index** is the row label or position used by `pandas` to identify rows.

### What `drop(index=1)` Does
It asks `pandas` to remove the row with index 1.

### What `errors="ignore"` Does
If that row does not exist, `errors="ignore"` prevents the notebook from crashing.

This is useful in beginner notebooks because it keeps the workflow more forgiving. Students can focus on understanding the concept instead of being stopped by a fragile step.

## Step 8: Convert A Column To Numeric
Sometimes a column looks numeric to a human reader, but the computer has stored it as text. That can cause problems for charts and calculations.

```python
df["Number of Stations"] = pd.to_numeric(df["Number of Stations"], errors="coerce")
display(df.dtypes)
```

### Why This Step Exists
Charts need real numbers, not number-like text.

### What `pd.to_numeric(...)` Does
It converts values to a numeric type.

### What `errors="coerce"` Does
If a value cannot be converted, it becomes `NaN` instead of causing the notebook to stop with an error.

This is a good example of a practical beginner idea: sometimes the computer needs data to be translated into a form it can actually work with.

## Step 9: Build The Bar Chart
Once the data is ready, students can create a visual output.

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

This block creates a bar chart using `plotly.express`.

Important parts:
- `fig` is the variable storing the chart object
- `x="Trend"` chooses the category axis
- `y="Number of Stations"` chooses the numeric values
- `title=...` adds a title
- `labels=...` improves the chart labels
- `fig.show()` displays the chart

This belongs to the **Output** stage of IPO because it creates a visible result that can be interpreted.

## Step 10: Interpret The Output
A chart is only useful if students can say what it shows.

At this stage, students should write two or three evidence-based observations. For example, they might identify:
- which trend category is highest,
- which category is lowest,
- and what the comparison might suggest.

This is where students move from display to meaning.

Important distinction:
- An **observation** describes what is visible in the evidence.
- An **interpretation** explains what that evidence might mean.

Students should be encouraged to refer to the actual categories and values they see, not use vague phrases like "the chart is interesting."

## The Bigger Lesson
This chapter is not only about one dataset. It teaches a pattern students will use again:

1. prepare the tools
2. load the data
3. inspect the table
4. clean the data
5. build the output
6. explain the meaning

That pattern is the real learning goal. The extreme heat dataset is the example that makes the pattern visible.

## What Students Should Be Able To Explain After This Chapter
By the end of the lesson, students should be able to explain:
- what `pandas` does,
- what a DataFrame is,
- why `df` is a common name,
- what the difference is between a method and a property,
- what `NaN` means,
- why cleaning happens before charting,
- and why the chart is only one part of the analysis process.

## Reflection Questions
- Why do we inspect data before cleaning it?
- Why might a number-looking value still need conversion?
- What is the difference between `df.head()` and `df.columns`?
- Why does cleaning happen before charting?
- What does the final chart help us understand that a raw table does not show as clearly?

## Curriculum + Assessment Alignment
- Curriculum source: `resources/ICD2O_2023.md`
- Assessment source: `resources/growSuccess.md`
- Evidence types to collect: observations, conversations, student products
