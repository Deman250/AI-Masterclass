#Exercise
import io

# Simulated file: one line per day with step count
weekly_data = """Monday: 9200
Tuesday: 7500
Wednesday: 10500
Thursday: 8800
Friday: 6900
Saturday: 11000
Sunday: 9600
"""

goal = 8000
days_on_goal = 0

f = io.StringIO(weekly_data)
for line in f:
    line = line.strip()
    if ":" in line:
        day, steps_str = line.split(":", 1)
        steps = int(steps_str.strip())
        status = "Goal hit" if steps >= goal else "Below goal"
        print(f"{day}: {steps} steps - {status}")
        if steps >= goal:
            days_on_goal += 1

print(f"\nDays on goal: {days_on_goal}/7")
