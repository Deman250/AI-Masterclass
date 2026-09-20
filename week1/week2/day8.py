# Create a dictionary called my_log
my_log = {
    "steps": 9400,
    "water_glasses": 7,
    "fasting_protocol": "OMAD",
    "sleep_hours": 7,
    "cold_showers": True
}

for key, value in my_log.items():
    print(f"{key}: {value}")

print()
if my_log["steps"] >= 8000:
    print("Steps hit!")
else:
    print("steps goal missed!")      