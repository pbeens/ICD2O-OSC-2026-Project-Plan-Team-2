# Beginner Tutorial: Jupyter Notebook Foundations (Lesson 01)

## Related Lesson Files
- Lesson plan: [01-jupyter-notebooks-foundations-lesson-plan.md](01-jupyter-notebooks-foundations-lesson-plan.md)
- Tutorial: [01-jupyter-notebooks-foundations-tutorial.md](01-jupyter-notebooks-foundations-tutorial.md)
- Notebook: not yet created
- Assignment: not yet created

## Chapter Purpose
This chapter introduces the workspace students will use for beginner data analysis. In the previous lesson, students learned the big picture: data analysis is a process that moves from input to process to output. In this lesson, students begin learning the actual environment where that work happens.

For many beginners, a notebook is unfamiliar. Even the basic words can feel new: notebook, cell, code, markdown, output, kernel, import, library. If those terms are not explained carefully, students may follow steps without understanding what they are doing. That is why this tutorial is written more like a chapter than a quick reference. The goal is to make the notebook environment feel understandable and predictable.

## What A Jupyter Notebook Is
A **Jupyter Notebook** is an interactive digital document where text, code, and results live together in one place.

That description matters because a notebook is not just a coding file. It is closer to a lab workbook. A student can:
- write a title or explanation,
- run code,
- see the result immediately,
- then keep writing notes underneath.

This is one reason notebooks are so useful for learning. They let students see a process unfold step by step.

## Why A Notebook Is Better For Beginner Analysis
If a student writes everything in one long Python script, it can be hard to tell what each part is doing. A notebook solves that problem by breaking the work into smaller pieces called **cells**.

This helps beginners because:
- each cell can do one job,
- students can test ideas in small steps,
- the notebook can mix explanations with actions,
- and the results appear right below the code that created them.

That is especially helpful in data analysis, where students often need to inspect data, explain what they see, and then take the next step.

## Important Vocabulary For This Chapter
Before students start typing code, they should understand the basic language of the notebook environment.

- **Cell**: one block in a notebook
- **Markdown cell**: a text cell used for headings, notes, instructions, and explanations
- **Code cell**: a cell that contains Python commands
- **Output**: the result that appears after a code cell runs
- **Python**: the programming language used in this course
- **Kernel**: the engine running in the background that executes the code
- **Runtime**: another word for the active working environment, often used in Colab
- **Library**: prewritten code that provides useful tools
- **Import**: the command that loads a library into the notebook
- **Variable**: a name that stores a value in memory
- **DataFrame**: a table structure in `pandas`

Students do not need to memorize all of this immediately. The point is to make the words familiar before they appear in action.

## The Three Main Cell Types Students Notice
In a beginner notebook, three parts appear over and over:

### Markdown Cells
Markdown cells are for human-readable writing. They can include:
- titles,
- headings,
- instructions,
- reflections,
- and short explanations.

These cells matter because a notebook should not feel like unexplained code floating in empty space. Markdown tells the reader what is happening.

### Code Cells
Code cells contain commands written in Python. When a student runs a code cell, the notebook asks the kernel to execute those commands.

This means code cells are action cells. They are where something happens.

### Output
Output is what appears after a code cell runs. Output might be:
- text,
- a table,
- an error message,
- or a chart.

The output helps students check whether their code did what they expected.

## Why Cell Order Matters
One of the most important beginner ideas is that notebooks remember what has already been run. This means order matters.

If a student tries to use a variable before creating it, the notebook will not know what that name means. If a student restarts the kernel, the notebook forgets the earlier work and needs the cells run again from the top.

This is why teachers often say:

> Run the notebook from top to bottom.

That advice is not just a classroom rule. It is how the notebook keeps its internal state organized.

## A First Mini Notebook
The best way to understand the notebook environment is to walk through a very small example. Each cell below has one job.

### Cell 1: A Markdown Title
```md
# Lesson 01: Jupyter Notebook Basics
Goal: Learn notebook workflow before full data analysis.
```

This opening cell does not run Python code. Instead, it labels the notebook and states the purpose of the lesson. That may seem small, but it is good practice. A notebook should explain itself.

### Cell 2: Import The Libraries
```python
import pandas as pd
import plotly.express as px
print("Libraries loaded.")
```

This is often the first real code cell in a notebook because it prepares the tools.

Here is what each part means:
- `import` tells Python to load a library
- `pandas` is a library for working with tables
- `plotly.express` is a library for making charts
- `as pd` and `as px` give those libraries short nicknames
- `print("Libraries loaded.")` displays a message so the student can see that the cell worked

This cell matters because later code depends on these libraries being available.

### Cell 3: Create A Small Practice Table
```python
sample = pd.DataFrame(
    {
        "Category": ["A", "B", "C"],
        "Value": [10, 15, 8]
    }
)
sample
```

This cell creates a tiny table directly inside the notebook.

Important ideas:
- `sample` is a variable name
- `pd.DataFrame(...)` creates a DataFrame
- a **DataFrame** is a table in `pandas`
- `"Category"` and `"Value"` are column names
- the lists below them are the data values for those columns
- placing `sample` on the final line tells the notebook to display the table

This is a good beginner example because it creates visible output quickly. Students can see that code can produce a table immediately.

### Cell 4: Preview The Top Rows
```python
sample.head()
```

This cell uses a **method**. A method is an action that an object can perform.

`head()` means "show me the top rows." The parentheses matter because they show that this is an action being called.

This is useful in real analysis because datasets can be large. Students rarely want to display the full dataset at the very beginning.

### Cell 5: Check The Column Names
```python
sample.columns
```

This cell uses a **property**. A property is information about an object, not an action.

There are no parentheses because `columns` is something the table has, not something the table does.

This distinction is worth teaching carefully:
- **Method** = action, often with parentheses
- **Property** = information, usually without parentheses

### Cell 6: Make A Tiny Chart
```python
fig = px.bar(sample, x="Category", y="Value", title="Sample Chart")
fig.show()
```

This cell turns the table into a simple bar chart.

Important parts:
- `px.bar(...)` creates a bar chart
- `x="Category"` chooses the category labels
- `y="Value"` chooses the numeric values
- `title="Sample Chart"` adds a title
- `fig` stores the chart object in a variable
- `fig.show()` displays the chart

This is often exciting for beginners because it turns a table into a visual result. It also reinforces the idea that notebooks can combine code with immediate output.

### Cell 7: Add A Reflection
```md
## Reflection
- What is the difference between a markdown cell and a code cell?
- What happens if you run cells out of order?
- Why do we keep imports near the top?
```

Reflection is part of the learning process. Students should not only run the notebook. They should be able to explain what they did and why it worked.

## Common Beginner Problems
Many notebook frustrations come from a few predictable issues. These are worth explaining directly.

### `NameError`
If students see a `NameError`, it usually means Python does not recognize a name they typed. In beginner notebooks, this often happens because:
- a required earlier cell was never run,
- the kernel was restarted,
- or the variable name was typed incorrectly.

### Old Or Missing Output
Sometimes the notebook still shows old output, or a chart does not appear as expected. In many cases, the fix is simple: rerun the notebook from top to bottom.

### Wrong Column Name
Computers care about exact spelling and capitalization. `"Value"` and `"value"` are different. That is why checking `sample.columns` is such a useful habit.

## What Students Should Understand By The End Of This Chapter
By the end of Lesson 01, students should be able to explain:
- what a Jupyter Notebook is,
- why notebooks are helpful for analysis,
- what markdown and code cells do,
- what an output is,
- what `import` means,
- what a library is,
- what a DataFrame is at a beginner level,
- and why notebook cells need to be run in order.

## Bridge To The Next Lesson
This chapter teaches the workspace. The next chapter teaches the first full dataset workflow. Students will load real data, inspect it, clean it, and build a chart. In other words, Lesson 01 prepares the environment so Lesson 02 can focus on actual beginner analysis.

## Reflection Questions
- Why is a notebook better for learning than one long block of code?
- What is the difference between a markdown cell and a code cell?
- Why do imports usually appear near the top of a notebook?
- What is the difference between a method and a property?
- Why does notebook execution order matter?

## Alignment Notes
- Curriculum source: `resources/ICD2O_2023.md`
- Assessment source: `resources/growSuccess.md`
- Evidence collection: observations, conversations, student products
