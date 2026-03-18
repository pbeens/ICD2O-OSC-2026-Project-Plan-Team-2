# Beginner Tutorial: Big Picture Data Analysis (Lesson 00)

## Related Lesson Files
- Lesson plan: [00-data-analysis-big-picture-lesson-plan.md](00-data-analysis-big-picture-lesson-plan.md)
- Tutorial: [00-data-analysis-big-picture-tutorial.md](00-data-analysis-big-picture-tutorial.md)
- Notebook: not yet created
- Assignment: [00-data-analysis-big-picture-assignment.md](00-data-analysis-big-picture-assignment.md)

## Chapter Purpose
This lesson is the first chapter in the course pathway. Before students can work inside a notebook, import a library, or build a chart, they need a clear mental model of what data analysis is actually for. If students do not understand the purpose of analysis, then later steps can feel like random computer actions instead of part of a meaningful process.

This tutorial is meant to read more like a short chapter than a checklist. The goal is to build understanding slowly. Students should be able to read it from top to bottom and feel like they are being introduced to a new subject, not dropped into a set of disconnected notes.

## What Data Analysis Really Means
When people hear the word "data," they often imagine a giant spreadsheet full of numbers. That is part of the picture, but it is not the whole picture. Data is simply information. It can be temperatures, survey answers, prices, bus times, names, dates, categories, or anything else that can be recorded and examined.

**Analysis** means studying something carefully so that we understand it better. So when we put those two ideas together, **data analysis** means studying information carefully so that we can answer a question, notice a pattern, or make a better decision.

That last part matters. Data analysis is not just about collecting information. It is about using information. A pile of numbers by itself does not help anyone very much. It becomes useful when someone asks a question such as:
- Which product sells the most?
- Which month is hottest?
- Which route is busiest?
- Which trend is increasing over time?

When we answer that kind of question with evidence instead of guessing, we are doing data analysis.

## Why People Use Data Analysis
In real life, people make decisions all the time. A school decides which clubs to support. A city decides where to place cooling centres. A business decides which products to keep selling. A scientist decides whether the evidence supports a claim.

All of those decisions become stronger when they are based on evidence. That is why data analysis matters. It helps people move from "I think" to "The evidence suggests."

Here are four big reasons people analyze data:

### 1. To Make Better Decisions
If a city wants to know whether extreme heat is becoming more common, guessing is not enough. The city needs temperature or weather data. If the data shows a clear pattern, then leaders can make a more informed decision.

### 2. To Notice Patterns
Sometimes the most important thing in a dataset is not one number, but a repeated pattern. Maybe sales increase every December. Maybe one neighbourhood has more traffic delays. Maybe one group answered a survey very differently from another group. Analysis helps us notice those patterns.

### 3. To Compare More Fairly
Data can help compare choices using the same evidence. For example, if students want to compare phone plans, they could compare price, data limit, and monthly cost instead of just choosing the advertisement they like best.

### 4. To Communicate Clearly
A good analysis does not stay hidden in a person's head. It becomes an output such as a chart, table, summary, or recommendation. That output helps other people understand the evidence too.

## Important Vocabulary For This Chapter
Because this course uses technical language, students need plain-language definitions early. The purpose here is not memorization. The purpose is familiarity.

- **Data**: pieces of information that can be recorded and examined
- **Analysis**: careful study of something to understand it better
- **Evidence**: information that supports a claim or decision
- **Pattern**: something that repeats or shows regularity
- **Trend**: a general direction of change
- **Dataset**: a collection of related data
- **CSV**: a file type used to store tables in plain text; it stands for "comma-separated values"
- **Tool**: something we use to help us do a task
- **Library**: prewritten code that gives programmers useful tools
- **pandas**: a Python library used for table-like data
- **plotly**: a Python library used for charts and visualizations

Students do not need to fully understand `pandas` or `plotly` yet. At this stage, it is enough to know that they are tools the class will use later.

## The Core Idea: Input, Process, Output
One of the most useful thinking tools in this course is the IPO model. IPO stands for **Input, Process, Output**. It is a simple way to describe how a system works.

Imagine making toast:
- **Input**: bread, toaster, electricity
- **Process**: the toaster heats the bread
- **Output**: toast

That same pattern works for many tasks, including computer tasks and data-analysis tasks. The reason IPO is so helpful is that it gives students a structure. Instead of seeing analysis as a confusing blur of computer commands, they can see it as a process with stages.

### Input
**Input** means what goes into the system.

In data analysis, input often includes:
- the question we want to answer
- the data source we are using
- the tools we need
- the environment we are working in

For example, if a notebook begins with `import pandas as pd`, that line is part of the input stage because it prepares the tool we need. If we load a CSV file, that is also part of input because we are bringing the data into the workspace.

### Process
**Process** means the work we do to the input.

In data analysis, process often includes:
- looking through the data
- checking column names
- cleaning missing or incorrect values
- changing formats when needed
- comparing values
- organizing the information so it can answer the question

This stage is often the most invisible part to beginners because the final chart usually gets the most attention. However, the process stage is where a lot of the real thinking happens.

### Output
**Output** means what comes out at the end.

In data analysis, outputs can include:
- a table
- a chart
- a written observation
- a conclusion
- a recommendation

An output is important because it communicates the result of the analysis. It is what another person can look at and understand.

## Why IPO Matters In This Course
Students often think the chart is the whole job. That is one of the biggest misunderstandings in beginner data analysis. A chart is only one output. Before the chart exists, someone has to:
- ask a question,
- load the correct data,
- inspect it,
- clean it if needed,
- and decide what the chart should show.

That is why IPO is taught before heavy coding. It helps students see that analysis is a structured process, not just a final image.

In this course sequence:
- **Lesson 00** introduces the big picture and vocabulary.
- **Lesson 01** focuses mostly on input skills, because students learn the notebook environment and tools.
- **Lesson 02** moves through the full cycle of input, process, and output using a real dataset.

## A Simple Example
Imagine a school wants to know which lunch option students prefer.

The workflow might look like this:

**Input**
- a survey of student choices
- a spreadsheet or CSV file of the results
- a question: "Which lunch option is most popular?"

**Process**
- count the responses
- group the answers by category
- check for missing or unclear responses
- compare the totals

**Output**
- a bar chart showing the most popular choices
- a short conclusion about the results

This is data analysis in a form that students can understand before they write any code.

## Classroom Activity: Sorting Tasks Into IPO
One way to strengthen understanding is to sort tasks into the three IPO categories.

Consider these six tasks:
1. Import `pandas`
2. Load a CSV file
3. Remove `NaN` rows
4. Convert a text column to numeric
5. Build a bar chart
6. Write one conclusion from the chart

To sort these properly, students need to think about what each action is doing.

- Tasks 1 and 2 belong to **Input** because they prepare the tools and load the information.
- Tasks 3 and 4 belong to **Process** because they change or clean the information.
- Tasks 5 and 6 belong to **Output** because they produce a visible result and a conclusion.

This activity matters because it forces students to notice that analysis is not one action. It is a sequence.

## More Vocabulary Connected To The Activity
Several words from this activity will appear again later in the course:

- **Import**: load a library so Python can use it
- **NaN**: missing or unusable numeric data; it stands for "Not a Number"
- **Numeric**: stored as a true number instead of text
- **Bar chart**: a chart that compares categories using bar heights

Students do not need complete technical mastery of these terms yet. The purpose here is to introduce them gently before they appear in code.

## A Common Misunderstanding
Many beginners think:

> "If I made a chart, I did data analysis."

That idea is incomplete. A chart can be part of data analysis, but it is not the whole process. If the data was loaded incorrectly, cleaned poorly, or misunderstood, then the chart may look convincing while still being misleading.

In other words, the output is only as strong as the input and process behind it.

## What Students Should Carry Forward
By the end of this chapter-like lesson, students should understand several key ideas:

- Data analysis is about answering questions with evidence.
- IPO is a useful way to organize and describe a workflow.
- Charts are important, but they are only one part of the full process.
- Terms like CSV, dataset, `pandas`, and `NaN` are not random jargon. They belong to the larger workflow students are about to learn.

## Bridge To The Next Lesson
The next lesson moves from ideas to tools. Students will learn what a Jupyter Notebook is, how notebook cells work, and why code must be run in order. That lesson still supports the big picture from this chapter. It simply brings students one step closer to doing the work themselves.

## Reflection Questions
- Why can bad or missing data lead to bad decisions?
- Which part of IPO feels easiest to understand right now?
- Which part still feels abstract or confusing?
- Why is a chart only one part of the full analysis process?

## Alignment Notes
- Curriculum source: `resources/ICD2O_2023.md`
- Assessment source: `resources/growSuccess.md`
- Evidence collection: observations, conversations, student products
