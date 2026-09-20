#Excercise
print("===EXCERSICE===")
def weekly_report(name, steps_list, goal=8000):
    days_on_target = 0
    for s in steps_list:
        if s >= goal:
            days_on_target += 1
    avg = sum(steps_list) / len(steps_list)
    print(f"--- {name}'s Week ---")
    print(f"Days tracked : {len(steps_list)}")
    print(f"Days on goal : {days_on_target}")
    print(f"Average steps: {round(avg, 0)}")
    print()

weekly_report("James", [9200, 7500, 10500, 8800, 6900, 11000, 9600])
weekly_report("Sandra", [10000, 10200, 9800, 11000, 10500], goal=10000)

print("===Default Parameters===")
def check_steps(steps, goal=8000):
    if steps >= goal:
        print(f"{steps} steps - Goal of {goal} hit.")
    else:
        print(f"{steps} steps - Goal of {goal} missed.")

# Uses the default goal of 8000
check_steps(9200)
check_steps(7500)

# Override the default goal
check_steps(9200, goal=10000)
check_steps(11500, goal=10000)

#Multiple parameters
print("===Multiple parameters===")
def log_day(steps, water=8, protocol="OMAD"):
    print(f"Steps: {steps} | Water: {water} glasses | Protocol: {protocol}")

log_day(9200)                        # Uses both defaults
log_day(10500, water=9)              # Override water only
log_day(8800, water=7, protocol="2MAD")  # Override both

#Keyword Arguments
print("===Keyword Arguments===")
def client_report(name, goal, sessions=4, bench_kg=60):
    print(f"{name} | Goal: {goal} | Sessions/week: {sessions} | Bench: {bench_kg}kg")

# Positional arguments
client_report("James", "fat loss")

# Keyword arguments: order does not matter
client_report(goal="muscle gain", name="Mwangi", bench_kg=100)

# Mix of positional and keyword
client_report("Sandra", "endurance", bench_kg=50)

#variable scope
print("===Variable scope===")
step_goal = 8000  # Global variable

def check_today(steps):
    result = "hit" if steps >= step_goal else "missed"  # result is local
    print(f"Goal {result}: {steps} steps")

check_today(9200)
check_today(7000)

# This would cause an error - result does not exist here:
# print(result)

print("===Daniel's BMI===")
def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 1)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

weight = 55
height = 1.55
bmi = calculate_bmi(weight, height)
category = bmi_category(bmi)

print(f"Weight: {weight}kg | Height: {height}m")
print(f"BMI: {bmi} | Category: {category}")
