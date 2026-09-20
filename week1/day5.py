# Daily step counts for a week
target_steps = 8000
step_counts_for_week = [8200, 5100, 11300, 6800, 9400, 42000, 10100]
for day, steps in enumerate(step_counts_for_week, start=1):
    if steps >= target_steps:
        print(f"Day {day}: Excellent job! You met your step goal for the day with {steps} steps.")

    step_counts_for_week = [8200, 5100, 11300, 6800, 9400, 42000, 10100]
    minimum_steps = 5000
    total=0
    valid_days=0
    for day, steps in enumerate(step_counts_for_week, start=1):
        if steps < minimum_steps:
            total += steps
            valid_days += 1
            print(f"Day {day}: You walked {steps} steps, which is below the minimum of {minimum_steps} steps.")
            continue #skip the rest of the loop for this day

        total += steps
        valid_days += 1
        print(f"Invalid days: {valid_days}, Total steps: {total}")
        print(f"Total steps ({valid_days} valid days): {total}")
        print(f"Average steps per valid day: {total / valid_days:.2f}")

        step_counts_for_week = [8200, 5100, 11300, 6800, 9400, 42000, 10100]
        steps < 8000
        steps = steps + 1
        print(f"Day {day}: You walked {steps} steps, which is below the minimum of {minimum_steps} steps.")
        print(f"Total steps ({valid_days} valid days): {total}")
        print(f"Average steps per valid day: {total / valid_days:.2f}")

        consecutive_streak_count = 0
        for day, steps in enumerate(step_counts_for_week, start=1):
            if steps >= 8000:
                consecutive_streak_count += 1
            else:
                consecutive_streak_count = 0
        print(f"Consecutive streak: {consecutive_streak_count}")


