#working with JSON data
#Exercise
import json

week_report = {
    "name": "James",
    "steps": [9200, 10500, 8800, 11000, 7600],
    "protocols": ["OMAD", "2MAD", "OMAD", "Autophagy Marathon", "OMAD"]
}

# Convert to JSON
json_str = json.dumps(week_report, indent=2)
print("JSON output:")
print(json_str)

# Load back and calculate average
loaded = json.loads(json_str)
avg = sum(loaded["steps"]) / len(loaded["steps"])
print(f"\nAverage steps for {loaded['name']}: {round(avg)}")

#json.dump():python to JSON text
print("==== PYTHON to JSON text ====")
import json

daily_log = {
    "steps": 9200,
    "water_glasses": 8,
    "cold_shower": True,
    "fasting_protocol": "OMAD",
    "sleep_hours": 7.5
}

# Convert to JSON string
json_text = json.dumps(daily_log)
print("Type:", type(json_text))
print("JSON:", json_text)

# Pretty print with indentation
pretty = json.dumps(daily_log, indent=2)
print("\nPretty JSON:")
print(pretty)

#json.load(): JSON text to python
print("\n==== JSON text to PYTHON ====")
import json

# This is what an API response might look like
api_response = '{"steps": 9200, "water_glasses": 8, "cold_shower": true, "protocol": "OMAD"}'

# Convert JSON string to Python dictionary
data = json.loads(api_response)

print("Type:", type(data))
print("Steps:", data["steps"])
print("Cold shower:", data["cold_shower"])
print("Protocol:", data["protocol"])

print("==== working with JSON files ====")
import json

# Simulate writing
daily_log = {
    "steps": 9200,
    "water_glasses": 8,
    "protocol": "OMAD",
    "cold_shower": True,
    "sleep_hours": 7.5
}
json_string = json.dumps(daily_log, indent=2)
print("Saved JSON:")
print(json_string)

# Simulate reading it back
loaded_data = json.loads(json_string)
print("\nRead back as Python dict:")
for key, value in loaded_data.items():
    print(f"  {key}: {value}")

print("==== navigating nested JSON ====")
import json

# Simulate writing
daily_log = {
    "steps": 9200,
    "water_glasses": 8,
    "protocol": "OMAD",
    "cold_shower": True,
    "sleep_hours": 7.5
}
json_string = json.dumps(daily_log, indent=2)
print("Saved JSON:")
print(json_string)

# Simulate reading it back
loaded_data = json.loads(json_string)
print("\nRead back as Python dict:")
for key, value in loaded_data.items():
    print(f"  {key}: {value}")

print("==== JSON error handling ====")
import json

responses = [
    '{"steps": 9200, "protocol": "OMAD"}',
    'not valid json at all',
    '{"steps": 10500, "protocol": "2MAD"}'
]

for r in responses:
    try:
        data = json.loads(r)
        print(f"Parsed OK: {data['steps']} steps")
    except json.JSONDecodeError:
        print(f"Invalid JSON: {r[:30]}...")