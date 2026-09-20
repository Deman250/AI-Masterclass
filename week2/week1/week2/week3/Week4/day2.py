#Error handling: try and except 
#Exercise
from collections.abc import MutableSequence

class steps(MutableSequence):
    def __init__(self):
        self._records = []

    def __len__(self):
        return len(self._records)

    def __getitem__(self, index):
        return self._records[index]

    def __setitem__(self, index, value):
        if isinstance(index, slice):
            validated = [self._validate_step(v) for v in value]
            self._records[index] = validated
        else:
            self._records[index] = self._validate_step(value)

    def __delitem__(self, index):
        del self._records[index]

    def insert(self, index, value):
        self._records.insert(index, self._validate_step(value))

    def _validate_step(self, step_count):
        try:
            value = int(step_count)
        except (TypeError, ValueError):
            raise ValueError("Invalid step count")
        if value < 0:
            raise ValueError("Step count cannot be negative")
        return value

    def add_entry(self, step_count):
        value = self._validate_step(step_count)
        self._records.append(value)
        return value

    def total_steps(self):
        return sum(self._records)

    def average_steps(self):
        return sum(self._records) / len(self._records) if self._records else 0

    def report(self):
        return f"Total steps: {self.total_steps()} | Average steps: {self.average_steps():.1f}"

def safe_log_entry(data):
    try:
        steps = int(data["steps"])
    except (ValueError, TypeError, KeyError):
        print("Invalid steps data. Skipping entry.")
        return None

    water    = data.get("water", 0)
    protocol = data.get("protocol", "Unknown")

    print(f"Steps: {steps} | Water: {water} glasses | Protocol: {protocol}")
    return steps

entries = [
    {"steps": "9200", "water": 8,   "protocol": "OMAD"},
    {"steps": "bad",  "water": 7,   "protocol": "2MAD"},
    {"steps": "8800", "protocol": "OMAD"},
    {"steps": "11000","water": 9},
]

results = [safe_log_entry(e) for e in entries]
valid = [r for r in results if r is not None]
print(f"\nValid entries: {len(valid)}")

#Unhandled error example
# This will crash
steps = 9000 #steps = "nine thousand"
goal = 8000
if steps >= goal:  # Can't compare string to number
    print("Goal hit")

#this will not crash
steps = 9000
goal = 8000
if steps >= goal:  # Can't compare string to number
    print("Goal hit")

#try and except example
print("==== try and except example ====")
steps_data = ["9200", "7500", "ten thousand", "8800", "6900"]

for item in steps_data:
    try:
        steps = int(item)
        if steps >= 8000:
            print(steps, "- Goal hit")
        else:
            print(steps, "- Below goal")
    except ValueError:
        print(f"'{item}' is not a valid number. Skipping.")

print("==== Multiple except blocks ====")
def calculate_average(steps_list):
    try:
        total = sum(steps_list)
        avg = total / len(steps_list)
        return round(avg)
    except ZeroDivisionError:
        print("Error: List is empty. Cannot calculate average.")
        return 0
    except TypeError:
        print("Error: List contains non-numeric values.")
        return 0

print("Average:", calculate_average([9200, 10500, 8800, 11000]))
print("Average:", calculate_average([]))
print("Average:", calculate_average([9200, "eight thousand", 10500]))

print("==== else and finally blocks ====")
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    else:
        print(f"{a} / {b} = {result}")
    finally:
        print("(Calculation attempted)")
    print()

safe_divide(100, 4)
safe_divide(100, 0)
safe_divide(9200, 7)

print("==== Raising exceptions ====")
def log_steps(steps):
    if not isinstance(steps, int):
        raise TypeError("Steps must be an integer.")
    if steps < 0:
        raise ValueError("Steps cannot be negative.")
    print(f"Steps logged: {steps}")

try:
    log_steps(9200)
    log_steps(-500)
except ValueError as e:
    print("ValueError:", e)
except TypeError as e:
    print("TypeError:", e)

print("==== Error handling with data processing ====")
daily_logs = [
    {"day": "Monday",    "steps": "9200"},
    {"day": "Tuesday",   "steps": "not recorded"},
    {"day": "Wednesday", "steps": "10500"},
    {"day": "Thursday",  "steps": None},
    {"day": "Friday",    "steps": "8800"},
]

valid_steps = []
for log in daily_logs:
    try:
        steps = int(log["steps"])
        valid_steps.append(steps)
        print(f"{log['day']}: {steps} steps")
    except (ValueError, TypeError):
        print(f"{log['day']}: invalid data - skipped")

if valid_steps:
    avg = sum(valid_steps) / len(valid_steps)
    print(f"\nAverage from valid days: {round(avg)} steps")