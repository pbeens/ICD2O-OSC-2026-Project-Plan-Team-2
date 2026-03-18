# 5E Lesson Plan Template[^1]

## Course

| ICD2O Digital Technology and Innovations in the Changing World |
| :---- |

## Teacher

| Peter |
| :---- |

## Lesson Number

| 2 |
| :---- |

## Title

| Beginner Data Analysis with Extreme Heat Events (Canada) |
| :---- |

## Curriculum Expectations

| - A1.1 apply computational thinking concepts and practices when planning and designing computational artifacts.<br>- A1.2 use a variety of tools and processes to plan, design, and share algorithms and computational artifacts.<br>- C2.2 write programs that use and generate data involving various sources and formats.<br>- C3.1 analyze existing code to understand the components and outcomes of the code.<br>- C3.2 modify an existing program, or components of a program, to enable it to complete a different task.<br>- C3.4 write programs that make use of external or add-on modules or libraries.<br>- A2.1 investigate current social, cultural, economic, environmental, and ethical issues related to digital technology that have personal, local, and global impacts, taking various perspectives into account. |
| :---- |

## Learning Goals

Students will be able to:

| - Explain what a DataFrame is and why `df` is used.<br>- Distinguish a method (example: `df.head()`) from a property (example: `df.columns`).<br>- Identify and explain `NaN` values in plain language.<br>- Clean a small dataset using `dropna()` and `drop(index=..., errors=\"ignore\")`.<br>- Build and interpret a basic bar chart using Plotly.<br>- Use clear data/programming vocabulary in oral and written explanations.<br>- Connect the visualization to an environmental issue (extreme heat) using evidence from the dataset. |
| :---- |

## Materials/Resources

| - Notebook: `notebooks/csv/extreme-heat-events-exploration.ipynb`<br>- Companion tutorial: [lesson-02-extreme-heat-events-tutorial.md](lesson-02-extreme-heat-events-tutorial.md)<br>- Curriculum reference: `resources/ICD2O_2023.md`<br>- Assessment/evaluation policy reference: `resources/growSuccess.md`<br>- Computer with Jupyter or Google Colab<br>- Internet access for direct CSV source<br>- Projector/teacher display |
| :---- |

## Lesson Body

| This lesson uses the `extreme-heat-events-exploration.ipynb` notebook as the beginner baseline because it follows a direct CSV workflow with small, sequential cleaning and plotting steps. |
| :---- |

### Engage

| Ask: “How could we tell if extreme heat events are becoming more common?” Show the notebook title/objective and preview the final bar chart so students know the lesson destination. |
| :---- |

### Explore

| Students run the first cells one at a time: import libraries, load CSV into `df`, check `df.head()`, and display `df.columns`. Teacher pauses after each step for quick checks. |
| :---- |

### Explain

| Mini-lesson during execution: define DataFrame, explain `df` naming convention, methods vs properties, and plain-language meaning of `NaN`. Walk through why we use `dropna()` and why `errors="ignore"` prevents crashes if an index is missing. |
| :---- |

### Elaborate

| Students complete numeric conversion for `Number of Stations`, generate the bar chart, then write 2-3 observations about patterns shown by trend categories. Optional extension: customize chart title/colors. |
| :---- |

### Evaluate

| Success criteria are shared before work begins and referenced during feedback. Evidence is gathered from observations (teacher conferencing while students run/debug cells), conversations (student explanations of methods/properties and cleaning decisions), and student products (completed notebook cells + exit ticket). Achievement Chart categories emphasized: Knowledge/Understanding (core terms and concepts), Thinking (cleaning/debugging decisions), Communication (clarity of vocabulary and explanations), and Application (correct tool use and evidence-based interpretation). Collect exit ticket: “One method, one property, one data-backed finding, and one next step.” |
| :---- |

## Homework

| Write a short paragraph explaining one data-cleaning command used in class and why it was needed for this dataset. |
| :---- |

## Comments

| Basis notebook selection rationale: This notebook is the most beginner-friendly option in the current repo because it uses direct CSV ingestion and avoids advanced structural cleanup patterns (for example, header-row reassignment loops). Requirements and evaluation approach are aligned to `resources/ICD2O_2023.md` and `resources/growSuccess.md`. |
| :---- |

[^1]:  [Why We Chose the 5E Lesson Plan Format](https://docs.google.com/document/d/1oTrJQprVIA7ggm6wgOXY9Z9adnE6T-9atT3vzn68zT0/edit?tab=t.0#heading=h.eh15dw7kt3ky)
