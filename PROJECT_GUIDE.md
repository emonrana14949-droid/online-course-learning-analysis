# Project Guide — Online Course Learning Analysis

This guide explains **everything** in this project, step by step, in simple words.
Read it from the top. By the end, you will understand the data, the code, and the results.

---

## 1. What is this project?

This project studies students on an **online learning platform** (like Udemy or Coursera).

We look at 420 learners. For each learner we know how much they studied,
how many lessons they finished, how they did in quizzes, and their final score.
Then we use Python to find patterns in that data.

### Questions this project answers

1. Which course has the highest completion rate?
2. Which course gives the highest average final score?
3. Do learners who watch more hours score better?
4. Which age group completes courses most often?
5. How does satisfaction relate to performance?

### Important: the data is not real

The dataset is **synthetic practice data**. That means a Python script *created* the data.
No real students were surveyed.

Why do we do this? Because it lets us practise the full Data Science workflow —
making data, cleaning it, analysing it, drawing charts, and writing conclusions —
before we work with real data.

So the **workflow is real**, but the **numbers are made up**. Do not present the
results as real research findings.

### Tools used

- **Python** — the programming language.
- **NumPy** — creates the random dataset and does number calculations (like the trend line).
- **Pandas** — loads the data into tables and calculates summaries (averages, groups, correlations).
- **Matplotlib** — draws the charts.

---

## 2. What is inside the project?

Here is every folder and file, one by one.

```text
online-course-learning-analysis/
├── README.md
├── PROJECT_GUIDE.md        ← this file
├── requirements.txt
├── .gitignore
├── data/
│   └── online_course_dataset.csv
├── src/
│   ├── generate_dataset.py
│   └── analysis.py
├── notebooks/
│   └── online_course_analysis.ipynb
└── outputs/
    ├── insights.md
    ├── tables/   (4 CSV files)
    └── charts/   (4 PNG images)
```

- **`README.md`** — The front page of the project. It gives a short summary,
  the list of columns, and the quick-start commands. Start there for the short version.
- **`PROJECT_GUIDE.md`** — This file. The full, slow explanation of everything.
- **`requirements.txt`** — A list of the Python libraries the project needs
  (pandas, numpy, matplotlib). The `pip` tool reads this file and installs them all at once.
- **`.gitignore`** — A list of files that Git should not upload, such as
  `__pycache__/` folders and virtual environments. It keeps the repository clean.
- **`data/online_course_dataset.csv`** — The dataset. One row per learner (420 rows),
  14 columns. A CSV file is a simple text table that Excel and Python can both open.
  This file is *created* by `generate_dataset.py`.
- **`src/generate_dataset.py`** — The script that *makes* the dataset and saves it as the CSV file.
- **`src/analysis.py`** — The script that *studies* the dataset. It makes all the tables,
  all the charts, and the insights file.
- **`notebooks/online_course_analysis.ipynb`** — A Jupyter notebook version of the exploration.
  A notebook lets you run small pieces of code one by one and see the result under each piece.
  Good for learning and for presentations.
- **`outputs/tables/`** — Four CSV tables made by the analysis (explained in Section 7).
- **`outputs/charts/`** — Four chart images (PNG) made by the analysis (explained in Section 7).
- **`outputs/insights.md`** — A short text file with the main findings, written automatically
  by `analysis.py`. This is the "answer sheet" of the project.

**The flow is simple:**

```text
generate_dataset.py  →  data/online_course_dataset.csv  →  analysis.py  →  outputs/ (tables, charts, insights)
```

---

## 3. The dataset, column by column

The dataset has **420 rows** (one learner per row) and **14 columns**.

Here are the first two real rows, so you can see what the data looks like:

| learner_id | age | gender | course | enrolled_month | total_lessons | lessons_completed | watch_hours | quiz_attempts | avg_quiz_score | assignments_submitted | satisfaction_rating | final_score | completion_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LRN-001 | 20 | Male | Excel for Business | Nov | 45 | 13 | 5.67 | 3 | 60.83 | 1 | 2 | 59.94 | Dropped |
| LRN-002 | 39 | Male | Web Development | Sep | 65 | 51 | 40.34 | 16 | 89.72 | 8 | 4 | 95.76 | In Progress |

Now each column, one by one:

1. **`learner_id`** — A code name for the learner. Example: `LRN-001`, `LRN-002`.
   It is not a real name. It just gives every row a unique ID.
2. **`age`** — The learner's age in years. A whole number from 18 to 45.
3. **`gender`** — `Female` or `Male`.
4. **`course`** — The course the learner joined. There are only 5 possible values:
   `Python Basics`, `Data Analysis with Pandas`, `Machine Learning`,
   `Web Development`, `Excel for Business`.
5. **`enrolled_month`** — The month in 2025 when the learner joined.
   Short month names: `Jan`, `Feb`, …, `Dec`.
6. **`total_lessons`** — How many lessons the course has in total.
   This depends only on the course: Python Basics = 40, Excel for Business = 45,
   Data Analysis with Pandas = 55, Web Development = 65, Machine Learning = 80.
7. **`lessons_completed`** — How many lessons this learner actually finished.
   Always between 0 and `total_lessons`.
8. **`watch_hours`** — Total video watching time, in hours. Example: `40.34` hours.
   The minimum is 0.1 and the maximum is 120.
9. **`quiz_attempts`** — How many times the learner tried quizzes. A whole number, 0 to 60.
10. **`avg_quiz_score`** — The learner's average quiz score, out of 100. Example: `89.72`.
11. **`assignments_submitted`** — How many assignments the learner handed in. A whole number, 0 to 12.
12. **`satisfaction_rating`** — How happy the learner is, from 1 (very unhappy) to 5 (very happy).
13. **`final_score`** — The learner's final course score, out of 100. Example: `95.76`.
14. **`completion_status`** — Where the learner ended up. Three possible values:
    - `Completed` — finished 90% or more of the lessons.
    - `In Progress` — finished 35% to 89% of the lessons.
    - `Dropped` — finished less than 35% of the lessons.

**A quick way to think about the columns:** columns 1–5 describe *who* the learner is.
Columns 6–11 describe *what the learner did*. Columns 12–14 describe *the result*.

---

## 4. How to run the project from zero

### Step 1 — Install Python

Install Python 3 from [python.org](https://www.python.org/downloads/) if you do not have it.
Check it works by opening a terminal (Command Prompt / Terminal) and typing:

```bash
python --version
```

You should see something like `Python 3.11.x`.

### Step 2 — Go into the project folder

```bash
cd online-course-learning-analysis
```

### Step 3 — Install the libraries

```bash
pip install -r requirements.txt
```

This reads `requirements.txt` and installs pandas, numpy and matplotlib.

### Step 4 — Create the dataset

```bash
python src/generate_dataset.py
```

You will see a message like:

```text
Dataset created: .../data/online_course_dataset.csv
Rows: 420 | Columns: 14
```

### Step 5 — Run the analysis

```bash
python src/analysis.py
```

You will see a message like:

```text
Analysis complete.
Tables saved to: .../outputs/tables
Charts saved to: .../outputs/charts
Insights saved to: .../outputs/insights.md
Best course by average final score: Machine Learning
Watch hours vs final score correlation: 0.73
```

### Step 6 — Look at the results

- Open **`outputs/insights.md`** to read the main findings.
- Open the PNG images in **`outputs/charts/`** to see the charts.
- Open the CSV files in **`outputs/tables/`** (Excel can open them) to see the numbers.
- Or open **`notebooks/online_course_analysis.ipynb`** in Jupyter / VS Code / Colab
  to explore the data step by step yourself.

**Good to know:** you can run the two scripts again and again.
Because the random seed is fixed (see Section 5), you get the *same* dataset every time.

---

## 5. Code explanation: `src/generate_dataset.py`

This script **creates the fake dataset**. Let us walk through it in order.

### 5.1 The top comment and the imports

```python
from pathlib import Path

import numpy as np
import pandas as pd
```

- The text in triple quotes at the very top is a **docstring** — a note that explains
  what the file does. Python ignores it when running.
- `import numpy as np` loads NumPy and gives it the short name `np`.
- `import pandas as pd` loads Pandas with the short name `pd`.
- `Path` helps the script find the project folder on any computer.

### 5.2 Where to save the file

```python
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "online_course_dataset.csv"
```

`__file__` is the location of this script. `parents[1]` goes one folder up,
so `PROJECT_ROOT` is the main project folder. `DATA_PATH` is then the full path
of the CSV file inside the `data/` folder. This way the script works no matter
where you run it from.

### 5.3 The course list

```python
COURSE_LESSONS = {
    "Python Basics": 40,
    "Data Analysis with Pandas": 55,
    "Machine Learning": 80,
    "Web Development": 65,
    "Excel for Business": 45,
}
```

This is a **dictionary**. It says how many lessons each course has.
Machine Learning is the longest course (80 lessons); Python Basics is the shortest (40).

### 5.4 The random seed — why 42?

```python
rng = np.random.default_rng(42)
n = 420
```

- `rng` is a **random number generator**. It makes all the random values in this script.
- The number `42` is the **seed**. Random numbers in a computer are not truly random —
  they come from a formula that starts at the seed.
- **Same seed = same "random" numbers every time.** So everyone who runs this script
  gets exactly the same 420 learners. This is very important for a project:
  your teacher can run your code and see the same results you saw.
- `n = 420` is the number of learners (rows) we will create.

### 5.5 Who the learners are

```python
age = rng.integers(18, 46, size=n)
gender = rng.choice(["Female", "Male"], size=n, p=[0.48, 0.52])
```

- `rng.integers(18, 46, size=n)` picks 420 whole numbers from 18 up to 45
  (the top number, 46, is not included). These are the ages.
- `rng.choice(...)` picks one value for each learner. The `p=[...]` part is the
  **probability**: 48% Female, 52% Male.
- The course is picked the same way, with probabilities
  `[0.24, 0.23, 0.20, 0.18, 0.15]` — so Python Basics is the most popular course
  and Excel for Business the least.
- `enrolled_month` is picked evenly from the 12 month names.

```python
total_lessons = np.array([COURSE_LESSONS[c] for c in course])
```

This line looks up each learner's course in the dictionary from Section 5.3
and writes down how many lessons that course has.

### 5.6 Engagement — the hidden engine of the dataset

```python
engagement = np.clip(rng.beta(2.2, 1.6, size=n), 0.02, 1.0)
lessons_completed = np.round(total_lessons * engagement).astype(int)
completion_ratio = lessons_completed / total_lessons
```

- `engagement` is a number between 0 and 1 for each learner.
  It means "how much of the course this learner got through".
  It comes from a **beta distribution**, which gives many learners a medium value,
  some low, and fewer very high. `np.clip(..., 0.02, 1.0)` keeps it between 2% and 100%.
- `lessons_completed` = total lessons × engagement, rounded to a whole number.
- `completion_ratio` = lessons completed ÷ total lessons. It is just engagement
  measured again from the finished numbers, and it drives many columns below.

**Why build the data this way?** In real life, one thing causes many other things:
a learner who finishes more lessons also watches more hours, tries more quizzes,
and usually scores better. This script copies that idea, so the final dataset
has realistic patterns for the analysis to find.

### 5.7 Watch hours, quizzes and assignments

```python
watch_hours = np.clip(
    lessons_completed * rng.normal(0.55, 0.15, size=n) + rng.normal(0, 1.5, size=n),
    0.1, 120,
)
```

- Each finished lesson gives about **0.55 hours** of watching on average
  (`rng.normal(0.55, 0.15)` means "random numbers around 0.55, spread 0.15").
- A little extra random noise (`rng.normal(0, 1.5)`) is added, because real
  learners are not all the same.
- `np.clip(..., 0.1, 120)` forces the result to stay between 0.1 and 120 hours.

The other two columns follow the same idea:

- **`quiz_attempts`** ≈ lessons completed × about 0.35, plus noise, clipped to 0–60.
- **`assignments_submitted`** ≈ engagement × a random number from 6 to 12,
  plus noise, clipped to 0–12.

### 5.8 The score formulas

These are the most important lines in the script. Read them slowly.

```python
avg_quiz_score = (
    42
    + completion_ratio * 22
    + watch_hours * 0.28
    + assignments_submitted * 0.9
    + rng.normal(0, 7, size=n)
)
avg_quiz_score = np.clip(avg_quiz_score, 0, 100)
```

In plain words: **quiz score = 42 base points**
+ up to 22 points for finishing the course
+ 0.28 points for every watch hour
+ 0.9 points for every assignment
+ a random luck factor between about −14 and +14.
Then it is clipped to stay between 0 and 100.

```python
final_score = (
    30
    + completion_ratio * 28
    + watch_hours * 0.30
    + avg_quiz_score * 0.28
    + assignments_submitted * 0.8
    + rng.normal(0, 6, size=n)
)
```

The final score works the same way, and it also **uses the quiz score**.
This is why, later in the analysis, watch hours and lessons completed
show a strong correlation with the final score — the script built that link in,
the same way real study behaviour creates it in real data.

### 5.9 Satisfaction and completion status

```python
satisfaction_rating = np.clip(
    np.round(1 + completion_ratio * 2.6 + (final_score / 100) * 1.3 + rng.normal(0, 0.6, size=n)),
    1, 5,
).astype(int)
```

Learners who finish more of the course and score higher give higher ratings.
The result is rounded and clipped to a whole number from 1 to 5.

```python
completion_status = np.where(
    completion_ratio >= 0.9,
    "Completed",
    np.where(completion_ratio >= 0.35, "In Progress", "Dropped"),
)
```

`np.where` is an "if" for whole columns at once. The rule is:

- ratio ≥ 0.90 (90% of lessons) → **Completed**
- ratio ≥ 0.35 → **In Progress**
- otherwise → **Dropped**

### 5.10 Saving the CSV

```python
df = pd.DataFrame({ "learner_id": ..., "age": age, ... })
DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(DATA_PATH, index=False)
```

- All the columns are put together into a Pandas **DataFrame** (a table).
  The `learner_id` column is made here: `LRN-001`, `LRN-002`, …, `LRN-420`.
  Some columns (watch hours, quiz score, final score) are rounded to 2 decimal
  places with `np.round(..., 2)` to keep the CSV tidy.
- `mkdir(...)` creates the `data/` folder if it does not exist yet.
- `df.to_csv(DATA_PATH, index=False)` saves the table as the CSV file.
  `index=False` means "do not add an extra row-number column".
- The last lines print how many rows and columns were created.

---

## 6. Code explanation: `src/analysis.py`

This script **studies the dataset**. It reads the CSV and produces every output.

### 6.1 Setup

The imports and paths are the same idea as before. Two new things:

```python
try:
    plt.style.use("seaborn-v0_8-whitegrid")
except OSError:
    plt.style.use("ggplot")
```

This picks a nice chart style. If that style is not available on the computer,
it falls back to another style instead of crashing.

There is also a helper function, `save_bar_chart(...)`. Three of the four charts
are bar charts with the same look, so instead of repeating the same code three
times, the script writes it once and reuses it. It takes a series of values,
a title, axis labels, a file path and a colour, draws the bar chart, and saves
it as a PNG image at 160 dpi (good quality).

### 6.2 Loading and cleaning the data

```python
df = pd.read_csv(DATA_PATH)
df = df.drop_duplicates().copy()
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors="coerce")
```

- `pd.read_csv` loads the CSV into a DataFrame.
- `drop_duplicates()` removes any repeated rows — a standard cleaning step.
- The last two lines find all number columns and make sure they are really
  stored as numbers. If a bad value appears, `errors="coerce"` turns it into
  "missing" instead of crashing the program.

### 6.3 New columns created by the analysis

The analysis adds three helpful columns that are **not** in the CSV:

```python
df["age_group"] = pd.cut(
    df["age"],
    bins=[17, 24, 31, 38, 120],
    labels=["18-24", "25-31", "32-38", "39+"],
)
df["completion_rate_pct"] = (df["lessons_completed"] / df["total_lessons"] * 100).round(2)
df["is_completed"] = (df["completion_status"] == "Completed").astype(int)
```

- **`age_group`** — `pd.cut` puts each age into a group: 18-24, 25-31, 32-38, or 39+.
  This lets us compare age groups instead of single ages.
- **`completion_rate_pct`** — lessons completed ÷ total lessons × 100,
  so each learner gets a completion percentage.
- **`is_completed`** — 1 if the learner's status is `Completed`, else 0.
  This trick is important: the **average** of a 0/1 column is the **percentage**
  of learners who completed. That is how the completion percentages below are made.

### 6.4 The four summary tables

**Table 1 — `summary_statistics.csv`**

```python
df.describe(include="all").round(2).to_csv(TABLE_DIR / "summary_statistics.csv")
```

`describe()` gives a quick health check of every column: how many values,
the mean, the standard deviation, the minimum, the maximum, and more.
For text columns it shows the most common value and how often it appears.

**Table 2 — `average_scores_by_course.csv`**

```python
by_course = (
    df.groupby("course")
    .agg(
        students=("learner_id", "count"),
        completion_pct=("is_completed", lambda s: round(s.mean() * 100, 2)),
        avg_watch_hours=("watch_hours", "mean"),
        avg_quiz_score=("avg_quiz_score", "mean"),
        avg_final_score=("final_score", "mean"),
    )
    .round(2)
    .sort_values("avg_final_score", ascending=False)
)
```

`groupby("course")` splits the 420 learners into 5 groups, one per course.
`.agg(...)` then calculates, for each course: how many students, the completion
percentage (the mean of `is_completed` × 100), average watch hours, average quiz
score, and average final score. Finally the table is sorted so the course with
the highest final score is on top. **This is the most important table in the project.**

**Table 3 — `completion_by_age_group.csv`** — The same groupby idea, but grouped
by `age_group`. It shows students, completion percentage, average watch hours
and average final score for each age group.

**Table 4 — `correlation_matrix.csv`**

```python
corr = df[corr_cols].corr(numeric_only=True).round(2)
```

`.corr()` calculates the **correlation** between every pair of these five columns:
watch hours, lessons completed, avg quiz score, final score, satisfaction rating.
Correlation is a number from **−1 to +1**:

- Close to **+1** → when one goes up, the other goes up too.
- Close to **0** → no clear link.
- Close to **−1** → when one goes up, the other goes down.

### 6.5 The four charts

- **Chart 1 — `completion_rate_by_course.png`** (green bar chart).
  Takes the `completion_pct` column from the by-course table, sorted highest first.
  Made with the `save_bar_chart` helper.
- **Chart 2 — `watch_hours_vs_final_score.png`** (scatter plot + trend line).
  Each dot is one learner: x = watch hours, y = final score.

  ```python
  slope, intercept = np.polyfit(df["watch_hours"], df["final_score"], 1)
  ```

  `np.polyfit(..., 1)` asks NumPy to find the straight line that fits the dots best.
  That black line is the **trend line**: it shows the general direction of the dots.
- **Chart 3 — `average_quiz_score_by_course.png`** (purple bar chart).
  The `avg_quiz_score` column from the by-course table, sorted highest first.
- **Chart 4 — `satisfaction_rating_distribution.png`** (pink histogram).
  `ax.hist(...)` counts how many learners gave each rating (1, 2, 3, 4, 5).
  A dashed black line marks the **mean** (average) rating.

### 6.6 How `insights.md` is written

At the end, the script picks out the headline numbers:

```python
best_course = by_course.index[0]                                  # top row after sorting
highest_completion_course = by_course["completion_pct"].idxmax()  # course with max completion %
watch_final_corr = corr.loc["watch_hours", "final_score"]         # one cell of the correlation table
overall_completion = round(df["is_completed"].mean() * 100, 2)
```

Then it puts those numbers into a ready-made text template (an f-string)
and saves it with `INSIGHTS_PATH.write_text(...)`. So the insights file is
**written by the code, not typed by a person** — if the data changes,
the insights update automatically. Finally, the script prints a short summary
to the terminal.

---

## 7. How to read the outputs

### The charts

- **`completion_rate_by_course.png`** — Compare the bar heights.
  The tallest bar is the course most learners finish. In this project all bars
  are short (under 10%) — see the note below.
- **`watch_hours_vs_final_score.png`** — Look at the *direction* of the cloud of dots.
  The dots rise to the right, and the trend line slopes up: learners who watched
  more hours generally scored higher. Dots far from the line are unusual learners —
  for example, someone who watched little but still scored high.
- **`average_quiz_score_by_course.png`** — Compare which course's learners do
  best in quizzes on average. This is not the same ranking as the final score chart,
  because the final score also includes completion and assignments.
- **`satisfaction_rating_distribution.png`** — The shape shows the mood of the learners.
  Tall bars on the right (4 and 5) mean most learners were happy.
  The dashed line is the average rating.

### The tables

- **`summary_statistics.csv`** — Start here to check the data makes sense:
  ages between 18 and 45, scores between 0 and 100, 420 rows.
- **`average_scores_by_course.csv`** — The main comparison table.
  Read it together with Charts 1 and 3 — they are pictures of this table.
- **`completion_by_age_group.csv`** — Check whether older or younger learners
  finish more often, and whether the groups have similar sizes
  (a percentage from a tiny group is not reliable).
- **`correlation_matrix.csv`** — Find the `final_score` row or column and read across:
  the biggest number is the factor most strongly linked to the final score.

### Why is the completion rate so low?

Only **7.14%** of learners are marked `Completed`. This is not a bug.
Remember the rule from Section 5.9: `Completed` needs **90% or more** of the lessons
finished, and the engagement values in this dataset put most learners in the middle.
So most learners land in `In Progress` (321 learners) or `Dropped` (69),
and only 30 reach 90%. Real online courses also have low completion rates,
so the pattern is realistic — but the exact numbers are still synthetic.

---

## 8. Key results of this project

These are the actual numbers from `outputs/insights.md`:

- Dataset size: **420 learners** across **5 courses**.
- Overall course completion rate: **7.14%** of learners finished their course
  (30 Completed, 321 In Progress, 69 Dropped).
- The course with the highest average final score is **Machine Learning (76.46)**.
- The course with the highest completion rate is **Web Development (9.09% completed)**.
- Correlation between watch hours and final score: **0.73** — a strong positive link.
- Correlation between lessons completed and final score: **0.79** — an even stronger link.

**How to say this in one sentence:** "Learners who completed more lessons and
watched more hours scored much higher, Machine Learning learners had the best
average final score, but very few learners in any course actually finished."

---

## 9. Viva / presentation help

Questions a teacher may ask, with short model answers.

**Q1. Why did you use Pandas?**
Pandas is made for table data. It loads a CSV into a DataFrame in one line,
and it gives us easy tools to clean data, group it (`groupby`), and calculate
averages and correlations. Doing the same work with plain Python lists would
take much longer code.

**Q2. Why did you use NumPy?**
NumPy creates fast random data and does number work on whole columns at once.
In this project it generates the dataset, and in the analysis it fits the
trend line with `np.polyfit`.

**Q3. What is correlation?**
Correlation measures how two things move together, from −1 to +1.
Here, watch hours and final score have a correlation of 0.73, which means
learners who watched more usually scored more. 0 would mean no link,
and a negative number would mean one goes up while the other goes down.

**Q4. Does watching more videos *cause* a higher score?**
We cannot say that from this data. Correlation does not prove causation.
Maybe watching more helps learning — or maybe strong, motivated learners both
watch more *and* score more. Also, this dataset is synthetic: the link was
built into the score formula on purpose, to practise the workflow.

**Q5. What does the trend line in the scatter plot mean?**
It is the straight line that best fits all the dots, calculated by `np.polyfit`.
Its upward slope shows the general pattern: more watch hours, higher final score.
Single dots can sit far from the line — the line shows the average pattern,
not a rule for every learner.

**Q6. Why did you fix the random seed to 42?**
So the results are reproducible. With the same seed, the generator makes the
same dataset every time, so anyone can run my code and get exactly my numbers.
Without a seed, every run would give different results.

**Q7. What does `groupby` do?**
It splits the table into groups — for example, one group per course —
then calculates something for each group, like the average final score.
That is how the by-course and by-age-group tables were made.

**Q8. Why is the completion rate only 7.14%? Is something wrong?**
Nothing is wrong. "Completed" was defined strictly: a learner must finish at
least 90% of the lessons. Most learners in the data finish 35–89%, so they are
"In Progress". Real online courses also have low completion rates.

**Q9. What is the difference between a bar chart and a histogram?**
A bar chart compares separate categories — here, one bar per course.
A histogram shows how one number column is spread out — here, how many learners
gave each satisfaction rating. In this project the histogram uses the ratings
1 to 5 as its bins.

**Q10. Is this real data? What would you do with real data?**
No, it is synthetic data generated by a script, made for practice.
With real platform data, I would keep the same analysis code, replace the CSV,
and add proper documentation: where the data came from, how it was collected,
and permission/privacy notes. The conclusions would also need more care,
because real data has messier problems like missing values.

---

## 10. What to learn next / how to extend

1. **Use real data.** Download a public online-course or student dataset
   (for example from Kaggle) and run the same analysis on it.
   Compare how the workflow changes when the data is messy.
2. **Predict completion with Machine Learning.** Use scikit-learn to train a
   simple model (like logistic regression) that predicts `is_completed`
   from watch hours, lessons completed and quiz attempts — then measure
   how accurate it is.
3. **Build a dashboard.** Turn the charts into an interactive Streamlit page
   where a user can pick a course and see its numbers update.
4. **Go deeper with statistics.** Add per-course box plots of final scores,
   check whether the difference between courses is statistically significant,
   and look at *why* learners drop out — for example, the average lessons
   completed in the first month for Dropped vs Completed learners.

---

*End of guide. If anything is still unclear, run the notebook
(`notebooks/online_course_analysis.ipynb`) and change one number at a time —
that is the fastest way to learn what each part does.*
