#List comprehension Exercise
print("=== LIST COMPREHENSION EXCERCISE ===")
people = [
    {"name": "James",   "steps": [9200, 10500, 8800, 11000, 7600, 9400, 10200]},
    {"name": "Sandra",  "steps": [7000, 7500, 6800, 8000, 7200, 8500, 7800]},
    {"name": "Mwangi",  "steps": [10000, 11500, 9800, 12000, 10500, 11000, 10800]},
    {"name": "Patrick", "steps": [8500, 9000, 8800, 9200, 8600, 9400, 9100]},
]

# 1. All step counts above 10,000 across all people
all_steps = [s for p in people for s in p["steps"]]
high_steps = [s for s in all_steps if s > 10000]
print("Steps above 10,000:", high_steps)

# 2. Names with average steps above 9,000
high_avg_names = [p["name"] for p in people if sum(p["steps"]) / len(p["steps"]) > 9000]
print("High average performers:", high_avg_names)

print("=== Standard loop approach ===")
weekly_steps = [9200, 7500, 10500, 8800, 6900, 11000, 9600]

goal_days = []
missed_days = []
for steps in weekly_steps:
    if steps >= 8000:
        goal_days.append(steps)
    else:
        missed_days.append(steps)

print(goal_days)

#list comprehension approach
print("=== List comrehension approach ===")
weekly_steps = [9200, 7500, 10500, 8800, 6900, 11000, 9600]

missed_days = [steps for steps in weekly_steps if steps <= 8000]

print(missed_days)

#Transforming Items
print("=== Transforming Items ===")
weekly_steps = [9200, 7500, 10500, 8800, 6900, 11000, 9600]

# Convert each step count to km
km_steps= [round(s * 1.3 / 1000, 2) for s in weekly_steps]
print("Steps:", weekly_steps)
print("km   :", km_steps)

weekly_steps = [9200, 7500, 10500, 8800, 6900, 11000, 9600]

# Convert each step count to km
calories_steps = [round(s * 0.04 / 1000, 2) for s in weekly_steps]
print("Steps:", weekly_steps)
print("calories   :", calories_steps)

#Filtering a list of Dictionaries
print("=== Filtering a list of Dictionaries ===")
clients = [
    {"name": "James",   "goal": "fat loss",    "sessions": 4},
    {"name": "Mwangi",  "goal": "muscle gain", "sessions": 5},
    {"name": "Sandra",  "goal": "endurance",   "sessions": 3},
    {"name": "Patrick", "goal": "fat loss",    "sessions": 4},
    {"name": "Grace",   "goal": "fat loss",    "sessions": 3},
]

# Get names of all fat loss clients
fat_loss_names = [c["name"] for c in clients if c["goal"] == "fat loss"]
print("Fat loss clients:", fat_loss_names)

# Get all clients with 4 or more sessions per week
active_clients = [c for c in clients if c["sessions"] >= 4]
print("Active clients:", [c["name"] for c in active_clients])
#comprehension Vs Loop
comprenhension_loop = "Use a comprehension when you are building a new list from an existing one with a simple transformation or filter. Use a regular loop when the logic is complex, when you need to do multiple things per item, or when readability would suffer."
print(comprenhension_loop)

#build status
weekly_steps = [9200, 7500, 10500, 8800, 6900, 11000, 9600]

# Build a list of status strings for each day
statuses = ["Goal hit" if s >= 8000 else "Below goal" for s in weekly_steps]

for i, status in enumerate(statuses):
    print(f"Day {i+1}: {weekly_steps[i]} steps - {status}")

day_weeks = 21
for x in range(1, day_weeks + 1):
    print(f"Day {x}")
    if x >= 16:
        break