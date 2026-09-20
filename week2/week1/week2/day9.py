week_log = [
    {"day": "Monday", "steps": 9200, "fasting_protocol": "OMAD"},
    {"day": "Tuesday", "steps": 10500, "fasting_protocol": "2MAD"},
    {"day": "Wednesday", "steps": 8800, "fasting_protocol": "OMAD"},
    {"day": "Thursday", "steps": 11000, "fasting_protocol": "Autophagy marathon"},
    {"day": "Friday", "steps": 7600, "fasting_protocol": "OMAD"}
]

total = 0
for log in week_log:
    total += log["steps"]
    print(f"{log['day']}: {log['steps']} steps, Fasting Protocol: {log['fasting_protocol']}")

average_steps = total / len(week_log)
print(f"\nAverage steps for the week: {average_steps:.2f}")

for log in week_log:
    print(f"{log['day']}: {log['steps']} steps, Fasting Protocol: {log['fasting_protocol']}, Cold Showers: {log.get('cold_showers', True)}")
    print(f"Cold showers: {log.get('cold_showers', True)}")
week_log.insert(2, {"day": "Wednesday", "steps": 8800, "fasting_protocol": "OMAD", "cold_showers": False})
for log in week_log:
    print(f"{log['day']}: {log['steps']} steps, Fasting Protocol: {log['fasting_protocol']}, Cold Showers: {log.get('cold_showers', True)}")
    week_log[4]["cold_showers"] = False
    for log in week_log:
        print(f"{log['day']}: {log['steps']} steps, Fasting Protocol: {log['fasting_protocol']}, Cold Showers: {log.get('cold_showers', True)}")    
        week_log[0]["cold_showers"] = False