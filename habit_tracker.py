habits = [
    ("Exercise", True),
    ("Read Book", True),
    ("Study", False),
    ("Walk", True)
]

for habit, completed in habits:
    if completed:
        print(habit, "- Completed")
    else:
        print(habit, "- Not Completed")


def habit_report(habits):
    completed_count = sum(
        1
        for habit, completed in habits
        if completed
    )

    return {
        "completed": completed_count,
        "total": len(habits)
    }


report = habit_report(habits)

print("Habit Report:", report)