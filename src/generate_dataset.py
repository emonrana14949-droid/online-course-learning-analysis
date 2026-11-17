"""Generate a synthetic online course dataset for the learning analysis project.

The dataset is practice data only. It is designed to look like an online
learning platform dataset so the Pandas, NumPy and visualization workflow can
be practised before using real platform data.
"""

from pathlib import Path

import numpy as np
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "online_course_dataset.csv"

COURSE_LESSONS = {
    "Python Basics": 40,
    "Data Analysis with Pandas": 55,
    "Machine Learning": 80,
    "Web Development": 65,
    "Excel for Business": 45,
}


def main() -> None:
    rng = np.random.default_rng(42)
    n = 420

    age = rng.integers(18, 46, size=n)
    gender = rng.choice(["Female", "Male"], size=n, p=[0.48, 0.52])
    course = rng.choice(
        list(COURSE_LESSONS.keys()),
        size=n,
        p=[0.24, 0.23, 0.20, 0.18, 0.15],
    )
    enrolled_month = rng.choice(
        ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        size=n,
    )

    total_lessons = np.array([COURSE_LESSONS[c] for c in course])

    # Engagement: how much of the course each learner got through.
    engagement = np.clip(rng.beta(2.2, 1.6, size=n), 0.02, 1.0)
    lessons_completed = np.round(total_lessons * engagement).astype(int)
    lessons_completed = np.minimum(lessons_completed, total_lessons)
    completion_ratio = lessons_completed / total_lessons

    watch_hours = np.clip(
        lessons_completed * rng.normal(0.55, 0.15, size=n) + rng.normal(0, 1.5, size=n),
        0.1,
        120,
    )

    quiz_attempts = np.clip(
        np.round(lessons_completed * rng.normal(0.35, 0.10, size=n) + rng.normal(0, 1, size=n)),
        0,
        60,
    ).astype(int)

    assignments_submitted = np.clip(
        np.round(engagement * rng.integers(6, 13, size=n) + rng.normal(0, 1, size=n)),
        0,
        12,
    ).astype(int)

    avg_quiz_score = (
        42
        + completion_ratio * 22
        + watch_hours * 0.28
        + assignments_submitted * 0.9
        + rng.normal(0, 7, size=n)
    )
    avg_quiz_score = np.clip(avg_quiz_score, 0, 100)

    final_score = (
        30
        + completion_ratio * 28
        + watch_hours * 0.30
        + avg_quiz_score * 0.28
        + assignments_submitted * 0.8
        + rng.normal(0, 6, size=n)
    )
    final_score = np.clip(final_score, 0, 100)

    satisfaction_rating = np.clip(
        np.round(1 + completion_ratio * 2.6 + (final_score / 100) * 1.3 + rng.normal(0, 0.6, size=n)),
        1,
        5,
    ).astype(int)

    completion_status = np.where(
        completion_ratio >= 0.9,
        "Completed",
        np.where(completion_ratio >= 0.35, "In Progress", "Dropped"),
    )

    df = pd.DataFrame(
        {
            "learner_id": [f"LRN-{i:03d}" for i in range(1, n + 1)],
            "age": age,
            "gender": gender,
            "course": course,
            "enrolled_month": enrolled_month,
            "total_lessons": total_lessons,
            "lessons_completed": lessons_completed,
            "watch_hours": np.round(watch_hours, 2),
            "quiz_attempts": quiz_attempts,
            "avg_quiz_score": np.round(avg_quiz_score, 2),
            "assignments_submitted": assignments_submitted,
            "satisfaction_rating": satisfaction_rating,
            "final_score": np.round(final_score, 2),
            "completion_status": completion_status,
        }
    )

    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(DATA_PATH, index=False)
    print(f"Dataset created: {DATA_PATH}")
    print(f"Rows: {len(df)} | Columns: {len(df.columns)}")


if __name__ == "__main__":
    main()
