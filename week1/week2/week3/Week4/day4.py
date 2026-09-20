#EXERCISE
print("==== WORKING WITH CSV FILES ===")
import csv
import io

csv_data = """day,steps,protocol
Monday,9200,OMAD
Tuesday,7500,2MAD
Wednesday,10500,OMAD
Thursday,4200,OMAD
Friday,8800,Autophagy Marathon
Saturday,11000,2MAD
Sunday,9600,OMAD"""

f = io.StringIO(csv_data)
reader = csv.DictReader(f)

valid_steps = []
for row in reader:
    steps = int(row["steps"])
    if steps >= 7000:
        valid_steps.append(steps)
        print(f"{row['day']}: {steps} steps ({row['protocol']})")
    else:
        print(f"{row['day']}: {steps} steps - flagged as invalid")

avg = sum(valid_steps) / len(valid_steps)
print(f"\nAverage (valid days): {round(avg)} steps")

#Applied Example: Crop Harvest Tracker
print("A crop farmer tracks harvest yield per field using a CSV. The same DictReader pattern reads each field's output and flags underperforming plots.")
import csv, io

harvest_csv = """field,crop,bags_harvested,target_bags
North Plot,Maize,48,50
South Plot,Beans,22,30
East Plot,Wheat,61,55
West Plot,Maize,35,50
Centre Plot,Sorghum,44,40
"""

reader = csv.DictReader(io.StringIO(harvest_csv))

print(f"{'Field':<15} {'Crop':<10} {'Harvested':>10} {'Target':>8} {'Status':>12}")
print("-" * 58)

for row in reader:
    harvested = int(row["bags_harvested"])
    target = int(row["target_bags"])
    pct = (harvested / target) * 100
    status = "On target" if harvested >= target else f"Short by {target - harvested} bags"
    print(f"{row['field']:<15} {row['crop']:<10} {harvested:>10} {target:>8} {status:>12}")


print("==== Reading CSV file csv.readee ====")
import csv
import io

# Simulated CSV content
csv_data = """name,phone,skill,city
James Omondi,0712345678,welding,Nairobi
Sandra Weru,0723456789,tiling,Mombasa
Patrick Njiru,0734567890,phone repair,Nairobi
Grace Achieng,0745678901,copywriting,Kisumu
Brian Kamau,0756789012,upholstery,Nairobi"""

f = io.StringIO(csv_data)
reader = csv.reader(f)

for row in reader:
    print(row)

#skipping the header
print("=== skip header ===")
import csv
import io

csv_data = """name,phone,skill,city
James Omondi,0712345678,welding,Nairobi
Sandra Weru,0723456789,tiling,Mombasa
Patrick Njiru,0734567890,phone repair,Nairobi"""

f = io.StringIO(csv_data)
reader = csv.reader(f)
next(reader)  # Skip header row

for row in reader:
    name, phone, skill, city = row
    print(f"{name} | {skill} | {city}")

print("=== Reading with Dictreader ====")
import csv
import io

csv_data = """name,steps,water,protocol,cold_shower
James Omondi,9200,8,OMAD,True
Sandra Weru,10500,9,2MAD,True
Patrick Njiru,7600,6,OMAD,False
Grace Achieng,11000,8,Autophagy Marathon,True"""

f = io.StringIO(csv_data)
reader = csv.DictReader(f)

for row in reader:
    steps = int(row["steps"])
    status = "Goal hit" if steps >= 8000 else "Below goal"
    print(f"{row['name']}: {steps} steps | {row['protocol']} | {status}")

print("=== writing CSV with csv.writer ====")
import csv
import io

output = io.StringIO()
writer = csv.writer(output)

# Write header
writer.writerow(["name", "steps", "protocol", "goal_hit"])

# Write data rows
data = [
    ["James",   9200,  "OMAD",              True],
    ["Sandra",  10500, "2MAD",              True],
    ["Patrick", 7600,  "OMAD",              False],
    ["Grace",   11000, "Autophagy Marathon", True],
]

for row in data:
    writer.writerow(row)

print("Generated CSV:")
print(output.getvalue())
print("=== Writing the Dictwriter")
import csv
import io

clients = [
    {"name": "James",   "skill": "welding",      "city": "Nairobi",  "sessions": 4},
    {"name": "Sandra",  "skill": "tiling",        "city": "Mombasa",  "sessions": 3},
    {"name": "Patrick", "skill": "phone repair",  "city": "Nairobi",  "sessions": 4},
    {"name": "Grace",   "skill": "copywriting",   "city": "Kisumu",   "sessions": 2},
]

output = io.StringIO()
fieldnames = ["name", "skill", "city", "sessions"]
writer = csv.DictWriter(output, fieldnames=fieldnames)

writer.writeheader()
writer.writerows(clients)

print(output.getvalue())
