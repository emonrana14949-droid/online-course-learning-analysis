"""Analyse the online course dataset with Pandas, NumPy and Matplotlib.

Run from the project root:
    python src/analysis.py

Outputs are saved to:
    outputs/tables/  (CSV summary tables)
    outputs/charts/  (PNG visualizations)
    outputs/insights.md
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "online_course_dataset.csv"
TABLE_DIR = PROJECT_ROOT / "outputs" / "tables"
CHART_DIR = PROJECT_ROOT / "outputs" / "charts"
INSIGHTS_PATH = PROJECT_ROOT / "outputs" / "insights.md"

try:
    plt.style.use("seaborn-v0_8-whitegrid")
except OSError:
    plt.style.use("ggplot")


def save_bar_chart(series: pd.Series, title: str, xlabel: str, ylabel: str, path: Path, colour: str = "#2f81f7") -> None:
    fig, ax = plt.subplots(figsize=(9, 4.8))
    series.plot(kind="bar", ax=ax, color=colour, edgecolor="white")
    ax.set_title(title, fontweight="bold")
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.tick_params(axis="x", rotation=25)
    for label in ax.get_xticklabels():
        label.set_ha("right")
    fig.tight_layout()
    fig.savefig(path, dpi=160)
    plt.close(fig)


def main() -> None:
    TABLE_DIR.mkdir(parents=True, exist_ok=True)
    CHART_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(DATA_PATH)

    # Basic cleaning and feature engineering with Pandas.
    df = df.drop_duplicates().copy()
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors="coerce")
    df["age_group"] = pd.cut(
        df["age"],
        bins=[17, 24, 31, 38, 120],
        labels=["18-24", "25-31", "32-38", "39+"],
    )
    df["completion_rate_pct"] = (df["lessons_completed"] / df["total_lessons"] * 100).round(2)
    df["is_completed"] = (df["completion_status"] == "Completed").astype(int)

    # Summary tables.
    df.describe(include="all").round(2).to_csv(TABLE_DIR / "summary_statistics.csv")

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
    by_course.to_csv(TABLE_DIR / "average_scores_by_course.csv")

    by_age_group = (
        df.groupby("age_group", observed=False)
        .agg(
            students=("learner_id", "count"),
            completion_pct=("is_completed", lambda s: round(s.mean() * 100, 2)),
            avg_watch_hours=("watch_hours", "mean"),
            avg_final_score=("final_score", "mean"),
        )
        .round(2)
    )
    by_age_group.to_csv(TABLE_DIR / "completion_by_age_group.csv")

    corr_cols = [
        "watch_hours",
        "lessons_completed",
        "avg_quiz_score",
        "final_score",
        "satisfaction_rating",
    ]
    corr = df[corr_cols].corr(numeric_only=True).round(2)
    corr.to_csv(TABLE_DIR / "correlation_matrix.csv")

    # Chart 1: completion rate by course.
    completion_by_course = by_course.sort_values("completion_pct", ascending=False)["completion_pct"]
    save_bar_chart(
        completion_by_course,
        "Course Completion Rate by Course",
        "Course",
        "Learners completed (%)",
        CHART_DIR / "completion_rate_by_course.png",
        colour="#1f9d6b",
    )

    # Chart 2: watch hours vs final score with a NumPy trend line.
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.scatter(df["watch_hours"], df["final_score"], color="#2f81f7", alpha=0.65, edgecolor="white", linewidth=0.4)
    slope, intercept = np.polyfit(df["watch_hours"], df["final_score"], 1)
    x_line = np.linspace(df["watch_hours"].min(), df["watch_hours"].max(), 100)
    ax.plot(x_line, slope * x_line + intercept, color="#111111", linewidth=1.6, label="Trend line")
    ax.set_title("Watch Hours vs Final Score", fontweight="bold")
    ax.set_xlabel("Watch hours")
    ax.set_ylabel("Final score")
    ax.legend()
    fig.tight_layout()
    fig.savefig(CHART_DIR / "watch_hours_vs_final_score.png", dpi=160)
    plt.close(fig)

    # Chart 3: average quiz score by course.
    quiz_by_course = by_course.sort_values("avg_quiz_score", ascending=False)["avg_quiz_score"]
    save_bar_chart(
        quiz_by_course,
        "Average Quiz Score by Course",
        "Course",
        "Average quiz score",
        CHART_DIR / "average_quiz_score_by_course.png",
        colour="#8250df",
    )

    # Chart 4: satisfaction rating distribution.
    fig, ax = plt.subplots(figsize=(9, 4.8))
    ax.hist(df["satisfaction_rating"], bins=np.arange(0.5, 6.5, 1), color="#f778ba", edgecolor="white")
    ax.axvline(df["satisfaction_rating"].mean(), color="#111111", linestyle="--", linewidth=1.5, label="Mean")
    ax.set_xticks([1, 2, 3, 4, 5])
    ax.set_title("Distribution of Satisfaction Ratings", fontweight="bold")
    ax.set_xlabel("Satisfaction rating (1-5)")
    ax.set_ylabel("Number of learners")
    ax.legend()
    fig.tight_layout()
    fig.savefig(CHART_DIR / "satisfaction_rating_distribution.png", dpi=160)
    plt.close(fig)

    best_course = by_course.index[0]
    highest_completion_course = by_course["completion_pct"].idxmax()
    watch_final_corr = corr.loc["watch_hours", "final_score"]
    lessons_final_corr = corr.loc["lessons_completed", "final_score"]
    overall_completion = round(df["is_completed"].mean() * 100, 2)

    insights = f"""# Key Insights — Online Course Learning Analysis

> This project uses synthetic practice data generated with NumPy. The patterns below are for learning the workflow only; they are not real research findings.

- Dataset size: **{len(df)} learners** across **{df['course'].nunique()} courses**.
- Overall course completion rate: **{overall_completion}%** of learners finished their course.
- The course with the highest average final score is **{best_course}** ({by_course.loc[best_course, 'avg_final_score']:.2f}).
- The course with the highest completion rate is **{highest_completion_course}** ({by_course.loc[highest_completion_course, 'completion_pct']:.2f}% completed).
- Correlation between watch hours and final score: **{watch_final_corr:.2f}**.
- Correlation between lessons completed and final score: **{lessons_final_corr:.2f}**.

## Charts

- `charts/completion_rate_by_course.png`
- `charts/watch_hours_vs_final_score.png`
- `charts/average_quiz_score_by_course.png`
- `charts/satisfaction_rating_distribution.png`

## Important note

Correlation does not prove causation. For a real project, replace the synthetic CSV with real platform data and document how it was collected.
"""
    INSIGHTS_PATH.write_text(insights, encoding="utf-8")

    print("Analysis complete.")
    print(f"Tables saved to: {TABLE_DIR}")
    print(f"Charts saved to: {CHART_DIR}")
    print(f"Insights saved to: {INSIGHTS_PATH}")
    print(f"Best course by average final score: {best_course}")
    print(f"Watch hours vs final score correlation: {watch_final_corr:.2f}")


if __name__ == "__main__":
    main()
