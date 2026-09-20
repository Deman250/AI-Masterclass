#Assignments on pandas and numpy
print("\n ======= EXERCISE 1: DATAFRAMES =====")
import pandas as pd
# Create a DataFrame from a dictionary and inspect it
data = {
    "name": ["Eric", "James", "Amina", "Sara"],
    "score": [85, 72, 91, 68],
    "city": ["Nairobi", "Mombasa", "Nairobi", "Kisumu"]
}
df = pd.DataFrame(data)
print(df)
print("\nShape:", df.shape)
#Exercise 2
print("\n ====== EXERCISE 2:FILTERING =====")
import pandas as pd
data = {"name": ["Eric","James","Amina","Sara"], "score": [85,72,91,68], "city": ["Nairobi","Mombasa","Nairobi","Kisumu"]}
df = pd.DataFrame(data)
# Filter to show only students from Nairobi with score above 80
result = df[(df['city'] == 'Nairobi') & (df['score'] > 80)]
print(result)
#Exercise 3
print("\n ====== EXERCISE 3:GROUPING =====")
import pandas as pd
data = {"name": ["Eric","James","Amina","Sara"], "score": [85,72,91,68], "city": ["Nairobi","Mombasa","Nairobi","Kisumu"]}
df = pd.DataFrame(data)
# Group by city and get the average score per city
print(df.groupby('city')['score'].mean())
#Numpy challenge
print("\n ===== NUMPY CHALLENGE =====")
import numpy as np
# Create an array of 10 random integers between 1 and 100
# Print the mean, max, min, and standard deviation
arr = np.array([23, 67, 45, 89, 12, 56, 78, 34, 90, 41])
print(f"Mean: {arr.mean():.2f}")
print(f"Max: {arr.max()}")
print(f"Min: {arr.min()}")
print(f"Std: {arr.std():.2f}")

#Exercise 5
print("\n ====== EXERCISE 5: TRADE APPLICATION - TILING CONTRACTOR JOB TRACKER ====")
# Tiling contractor job records
jobs = [
    {"client": "Kamau", "location": "Kiambu", "boxes_used": 30, "price_per_box": 1800},
    {"client": "Mutua", "location": "Machakos", "boxes_used": 48, "price_per_box": 2100},
    {"client": "Odhiambo", "location": "Kisumu", "boxes_used": 20, "price_per_box": 1600},
    {"client": "Wanjiru", "location": "Nakuru", "boxes_used": 60, "price_per_box": 2200},
]

print("Job Summary:")
print("-" * 50)
total_boxes = 0
total_revenue = 0

for j in jobs:
    revenue = j["boxes_used"] * j["price_per_box"]
    print(f"{j['client']} ({j['location']}): {j['boxes_used']} boxes | KES {revenue:,}")
    total_boxes += j["boxes_used"]
    total_revenue += revenue

avg_price = total_revenue / total_boxes

print(f"\nTotal boxes laid: {total_boxes}")
print(f"Total revenue: KES {total_revenue:,}")
print(f"Average price per box: KES {avg_price:.0f}")

#Exercise 6
print("\n ===== EXERCISE 6: FARMING APPLICATION - WEEKLY MILK YIELD ANALYSIS =====")
# Weekly milk yield per cow (litres)
herd_data = [
    {"cow": "Daisy", "yields": [72, 68, 74, 70]},
    {"cow": "Bella", "yields": [45, 42, 38, 40]},
    {"cow": "Nala",  "yields": [88, 91, 85, 93]},
    {"cow": "Rosa",  "yields": [55, 58, 52, 50]},
    {"cow": "Lola",  "yields": [78, 80, 76, 82]},
]

MINIMUM_WEEKLY = 60
top_cow = None
top_total = 0

print(f"{'Cow':<8} {'Total':>8} {'Avg/wk':>8} {'Status':>10}")
print("-" * 38)

for cow in herd_data:
    total = sum(cow["yields"])
    avg = total / len(cow["yields"])
    status = "OK" if avg >= MINIMUM_WEEKLY else "NEEDS ATTENTION"
    print(f"{cow['cow']:<8} {total:>8} {avg:>8.1f} {status:>10}")
    if total > top_total:
        top_total = total
        top_cow = cow["cow"]

print(f"\nTop producer: {top_cow} ({top_total} litres over 4 weeks)")

#Code challenge 1
print("\n ==== CODE CHALLENGE 1: TILING CONTRACTOR JOBS ====")

jobs = [
    {"client": "Kamau", "boxes_used": 30, "price_per_box": 1800},
    {"client": "Mutua", "boxes_used": 48, "price_per_box": 2100},
    {"client": "Odhiambo", "boxes_used": 20, "price_per_box": 1600},
    {"client": "Wanjiru", "boxes_used": 60, "price_per_box": 2200},
]

total_boxes = 0
total_revenue = 0

for job in jobs:
    total_boxes += job["boxes_used"]
    total_revenue += job["boxes_used"] * job["price_per_box"]

print(f"Total: {total_boxes}")
print(f"Revenue: KES {total_revenue:}")
#code challenge 2 
print("\n ===== CODE CHALLENGE 2: PATIENT RISK SCREENING ====")
import pandas as pd

patients = [
    {"name": "Alice",  "bp": 155, "glucose": 130, "creatinine": 0.9},
    {"name": "Brian",  "bp": 120, "glucose": 118, "creatinine": 1.5},
    {"name": "Carol",  "bp": 148, "glucose": 142, "creatinine": 1.0},
    {"name": "David",  "bp": 130, "glucose": 110, "creatinine": 0.8},
    {"name": "Eve",    "bp": 160, "glucose": 98,  "creatinine": 1.1},
    {"name": "Frank",  "bp": 125, "glucose": 115, "creatinine": 0.7},
]
df = pd.DataFrame(patients)
Hypertension_risk = df[df['bp'] >= 140]
Diabetes_risk = df[df['glucose'] >= 126]
Kidney_risk = df[df['creatinine'] >= 1.2]
print("Hypertension risk:", len(Hypertension_risk))
print("Diabetes risk:", len(Diabetes_risk))
print("Kidney risk:", len(Kidney_risk))
