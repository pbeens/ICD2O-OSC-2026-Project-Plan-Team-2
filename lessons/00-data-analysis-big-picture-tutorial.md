# Beginner Tutorial: Big Picture Data Analysis (Lesson 00)

## Why This Lesson Exists
Before coding, students need a clear mental model of what data analysis is for and how the parts fit together.

## What Is Data Analysis?
Data analysis is the process of turning raw data into useful information that supports decisions.

In simple terms:
- **Data** means pieces of information, such as numbers, names, dates, categories, or answers to survey questions.
- **Analysis** means carefully looking at that information so we can understand it better.
- When we do **data analysis**, we are not just "looking at numbers." We are asking a question, checking evidence, and deciding what the information means.

Example:
- Raw data: daily temperatures for many cities
- Analysis question: Which city had the most very hot days?
- Useful information: a chart or conclusion that helps us compare cities

## Why Do We Do Data Analysis?
- To move from guesses to evidence-based decisions
- To identify patterns and trends
- To compare options more fairly
- To communicate findings clearly

This matters because many real-world decisions are better when they are based on evidence instead of opinions alone. Schools, businesses, scientists, and governments all use data analysis to help answer questions.

Examples:
- A school might look at survey data to decide which clubs students want.
- A city might look at weather data to decide where cooling centres are needed.
- A business might look at sales data to decide which products are popular.

## Important Words You Will Hear In This Course
- **Evidence-based**: supported by information we can check, not just a guess.
- **Pattern**: something that repeats or appears regularly in the data.
- **Trend**: a general direction of change over time or across categories.
- **Dataset**: a collection of related data. A CSV file is one common way to store a dataset.
- **CSV**: short for "comma-separated values." It is a plain-text table file.
- **Tool**: a program or library that helps us work with data.
- **Library**: prewritten code that gives us useful commands. Later, we will use libraries like `pandas` and `plotly`.
- **pandas**: a Python library that helps us work with tables of data.
- **plotly**: a Python library that helps us make charts.

You do not need to memorize all of these right now. The goal is to become familiar with them before you see them inside code.

## The IPO Model
IPO stands for **Input, Process, Output**. It is a simple way to describe how a system works.

If you think about making toast:
- Input = bread, toaster, electricity
- Process = the toaster heats the bread
- Output = toast

We can use the same idea to understand data analysis.

### Input
What goes in.
- Tools and environment setup (for example `import pandas as pd`)
- Data source (CSV/Excel/API)
- Problem/question we are trying to answer

Plain-language meaning:
- **Tools and environment setup** means getting the software ready.
- `import pandas as pd` is a line of Python code that loads the `pandas` library so we can use its table tools.
- An **API** is a way for one program to get data from another program or website.

### Process
What we do to the input.
- Inspect data (`head`, column names, data types)
- Clean data (missing values, bad rows, types)
- Transform or organize data
- Calculate/compare values

Plain-language meaning:
- **Inspect** means look through the data carefully before changing it.
- **Clean** means fix problems such as blanks, missing values, or wrong formats.
- **Transform** means change the structure so the data is easier to use.
- **Calculate/compare** means answer the question by working with the numbers or categories.

### Output
What comes out.
- Tables and charts
- Observations and conclusions
- Decision recommendations

Plain-language meaning:
- An **observation** is something you notice from the evidence.
- A **conclusion** is what you decide the evidence means.
- A **recommendation** is a suggested action based on the evidence.

## IPO Applied to Our Course Sequence
- Lesson 01 (Jupyter basics): mostly Input skills
- Lesson 02 (Extreme Heat): full Input + Process + Output cycle

That means:
- In Lesson 01, students mainly learn the workspace and tools.
- In Lesson 02, students start doing the full job of data analysis, from loading data to explaining what the chart shows.

## Related Notebook
- [02-extreme-heat-events-exploration.ipynb](../notebooks/csv/02-extreme-heat-events-exploration.ipynb)

## Classroom Activity
Sort each task into IPO:
1. Import pandas
2. Load CSV file
3. Remove `NaN` rows
4. Convert a text column to numeric
5. Build a bar chart
6. Write one conclusion from the chart

Helpful vocabulary for this activity:
- **Import** means load a library so Python can use it.
- **NaN** means a value is missing or not usable as a number.
- **Numeric** means a value is stored as a real number instead of text.
- **Bar chart** is a chart that compares categories using bars of different heights.

Expected mapping:
- Input: 1, 2
- Process: 3, 4
- Output: 5, 6

## Common Misunderstanding to Correct
“Chart = analysis.”
- Not fully true. A chart is one output.
- Analysis includes preparing data and reasoning from evidence.

This is important because students often think the "interesting part" starts when the chart appears. In reality, a good chart depends on the steps before it:
- asking a good question,
- loading the correct data,
- checking for mistakes,
- cleaning the data when needed,
- and then explaining what the chart actually shows.

## What Students Should Understand By The End Of Lesson 00
- Data analysis is a process, not just a final chart.
- IPO is a simple model for describing that process.
- Words like `pandas`, CSV, dataset, and `NaN` are tools or ideas they will meet later, not things they are expected to already know.
- The goal of the next lessons is to make those terms familiar through practice.

## Reflection Prompts
- Why can dirty data lead to bad decisions?
- Which stage (Input/Process/Output) is easiest for you right now?
- Which stage needs more practice?

## Alignment Notes
- Curriculum source: `resources/ICD2O_2023.md`
- Assessment source: `resources/growSuccess.md`
- Evidence collection: observations, conversations, student products
