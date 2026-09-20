#Modular calculator
print("=== PROJECT:FITNESS AND DISCIPLINE CALCULATOR ===")
#Exercise1
#Takes weight in kg and height in metres. Returns BMI rounded to one decimal place.
print("=== Calculator 1:BMI ===")
import math
from os import name

def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 1)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# Test
weight = 84
height = 1.78
bmi = calculate_bmi(weight, height)
print(f"Weight : {weight} kg")
print(f"Height : {height} m")
print(f"BMI    : {bmi}")
print(f"Status : {bmi_category(bmi)}")
print("=== Steps Goal Checker ===")
#import math

def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 1)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# Test
weight = 84
height = 1.78
bmi = calculate_bmi(weight, height)
print(f"Weight : {weight} kg")
print(f"Height : {height} m")
print(f"BMI    : {bmi}")
print(f"Status : {bmi_category(bmi)}")

#import math

def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 1)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# Test
weight = 84
height = 1.78
bmi = calculate_bmi(weight, height)
print(f"Weight : {weight} kg")
print(f"Height : {height} m")
print(f"BMI    : {bmi}")
print(f"Status : {bmi_category(bmi)}")

#Takes a list of daily step counts and an optional goal (default 8,000). Returns a summary of the week.
print("=== Calculator 2: Step Goal Checker ===")
def weekly_step_summary(steps_list, goal=8000):
    days_hit = len([s for s in steps_list if s >= goal])
    average = sum(steps_list) / len(steps_list)
    best = max(steps_list)
    worst = min(steps_list)

    return {
        "days_on_goal": days_hit,
        "total_days": len(steps_list),
        "average": round(average),
        "best_day": best,
        "worst_day": worst
    }

weekly = [9200, 7500, 10500, 8800, 6900, 11000, 9600]
result = weekly_step_summary(weekly)

print("Step Summary:")
print(f"  Days on goal : {result['days_on_goal']}/{result['total_days']}")
print(f"  Average      : {result['average']} steps")
print(f"  Best day     : {result['best_day']} steps")
print(f"  Worst day    : {result['worst_day']} steps")

#Estimates calories burned from walking. Uses approximately 0.04 calories per step.
print("=== Calculator 3: Calorie Estimate ====")
import math

def estimate_calories(steps, calories_per_step=0.04):
    calories = steps * calories_per_step
    return math.floor(calories)

weekly_steps = [9200, 7500, 10500, 8800, 6900, 11000, 9600]
daily_cals = [estimate_calories(s) for s in weekly_steps]

print("Estimated daily calories burned from walking:")
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for day, cals in zip(days, daily_cals):
    print(f"  {day}: {cals} kcal")
print(f"  Total: {sum(daily_cals)} kcal")

#Takes a list of daily fasting protocols and returns a count of how many days used each protocol.
print("=== Calculator 4: Days on Protocol ===")
def protocol_summary(protocol_list):
    unique = list(set(protocol_list))
    summary = {}
    for p in unique:
        summary[p] = protocol_list.count(p)
    return summary

protocols = ["OMAD", "2MAD", "OMAD", "Autophagy Marathon", "OMAD", "2MAD", "OMAD"]
result = protocol_summary(protocols)

print("Protocol breakdown:")
for protocol, days in result.items():
    print(f"  {protocol}: {days} day(s)")


print("====== WEEK 3 SUMMARRY =======")
#Exercise 1
print("=== Funtions ===")
# Write a function called greet that takes a name
# and returns a greeting string
def greet(name):
    return f"Hello, {name}. Welcome to the program."

print(greet("Eric"))
print(greet("Amina"))
#Exercise 2
print("=== Default parameter ====")
# Write a function called power(base, exp=2)
# that returns base raised to exp
def power(base, exp=2):
    return base ** exp

print(power(3))      # 9
print(power(2, 10))  # 1024
#Exercise 3
print("=== List comrehension ===")
# Use a list comprehension to get all even numbers from 1 to 30
evens = [n for n in range(1, 31) if n % 2 == 0]
print(evens)

# Now get the squares of those even numbers
squares = [n**2 for n in evens]
print(squares)
#Exercise 4
print("==== Challenge ===")
# Write a function that takes a list of scores
# and returns the average, highest, and lowest
def analyse(scores):
    return {
        "average": sum(scores) / len(scores),
        "highest": max(scores),
        "lowest": min(scores)
    }

result = analyse([78, 91, 63, 85, 72])
for k, v in result.items():
    print(f"{k}: {v}")

for x in range(1, 26):
    if x >= 18:
        print("Wantam")
    else:
        print("dcp")

# Write your greet function here

def greet(name):
    return f"Hello, {name}!"

print(greet("Amerix"))
print(greet("SMP member"))
print(greet("Guest"))