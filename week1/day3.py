exercises = 6
sets_per_exercise = 4
reps_per_set = 12
average_weight_per_rep = "40kg"
session_time_in_minutes = 60
# Calculate and print your report
total_sets = exercises * sets_per_exercise
total_reps = total_sets * reps_per_set
total_volume_weight_kg = total_reps * int(average_weight_per_rep.replace("kg", ""))
print(f"Today Amina did a total of {total_sets} sets of leg exercise, with a weight of {average_weight_per_rep}. The whole session took {session_time_in_minutes} minutes.")