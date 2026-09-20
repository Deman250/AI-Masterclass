#Week 4 exercises and Summary
print("=== File writing ===")
# Write a program that saves your name and city to a text file
# then reads it back and prints it
import tempfile, os
path = tempfile.mktemp(suffix='.txt')
with open(path, 'w') as f:
    f.write("Name: Daniel\nCity: Nairobi\n")
with open(path) as f:
    print(f.read())

print("=== Exercise 2: ERROR HANDLING ===")
# Wrap a division operation in try/except
# Handle ZeroDivisionError and ValueError separately
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except ValueError as e:
        return f"Invalid input: {e}"

print(safe_divide(10, 2))
print(safe_divide(10, 0))

print("=== Exercise 3: JSON ===")
import json
# Create a Python dictionary and convert it to JSON
# Then parse it back and access a value
data = {"name": "Daniel", "age": 28, "city": "Nairobi"}
json_str = json.dumps(data, indent=2)
print(json_str)
parsed = json.loads(json_str)
print(f"Name: {parsed['name']}")

print("=== Exercise 4: CHALLENGE ===")
import json, tempfile
# Save a list of 3 students (name, score) to JSON
# Read it back and print only students who scored above 70
students = [
    {"name": "Daniel", "score": 85},
    {"name": "James", "score": 62},
    {"name": "Amina", "score": 91}
]
path = tempfile.mktemp(suffix='.json')
with open(path, 'w') as f:
    json.dump(students, f)
with open(path) as f:
    loaded = json.load(f)
for s in loaded:
    if s['score'] > 70:
        print(f"{s['name']}: {s['score']}")

print("=== Exercise 5: TRADE APPLICATION - CARPENTRY WORKSHOP LOG ===")
import io

# Carpentry workshop daily log: day, chairs made, timber used (metres)
workshop_log = """Monday,8,24
Tuesday,6,18
Wednesday,10,30
Thursday,7,21
Friday,9,27
"""

total_chairs = 0
total_timber = 0
days = 0

f = io.StringIO(workshop_log)
for line in f:
    line = line.strip()
    if line:
        day, chairs, timber = line.split(",")
        chairs = int(chairs)
        timber = int(timber)
        print(f"{day}: {chairs} chairs | {timber}m timber")
        total_chairs += chairs
        total_timber += timber
        days += 1

print(f"\nTotal chairs made: {total_chairs}")
print(f"Total timber used: {total_timber}m")
print(f"Average chairs per day: {total_chairs // days}")

print("=== Exercise 6: FARMING APPLICATION - DAILY COW MILK LOG ===")
import io

# Carpentry workshop daily log: day, chairs made, timber used (metres)
workshop_log = """Monday,8,24
Tuesday,6,18
Wednesday,10,30
Thursday,7,21
Friday,9,27
"""

total_chairs = 0
total_timber = 0
days = 0

f = io.StringIO(workshop_log)
for line in f:
    line = line.strip()
    if line:
        day, chairs, timber = line.split(",")
        chairs = int(chairs)
        timber = int(timber)
        print(f"{day}: {chairs} chairs | {timber}m timber")
        total_chairs += chairs
        total_timber += timber
        days += 1

print(f"\nTotal chairs made: {total_chairs}")
print(f"Total timber used: {total_timber}m")
print(f"Average chairs per day: {total_chairs // days}")

farmers_log = "two hundred"
try:
    total_milk = int(farmers_log)
    print(f"Total milk produced: {total_milk} litres")
except ValueError as e:
    print(f"Invalid milk log entry: two hundred is not a number")
