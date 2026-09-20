#Filtering rows
import pandas as pd

df = pd.DataFrame({
    "day":      ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "steps":    [9200, 10500, 8800, 11000, 7600, 9400, 10200],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0],
    "protocol": ["OMAD", "2MAD", "OMAD", "OMAD", "2MAD", "OMAD", "OMAD"],
})

# Days where step goal was hit
goal_days = df[df["steps"] >= 10000]
print("Days with 10k+ steps:")
print(goal_days[["day", "steps", "protocol"]].to_string())

print()
# Days with less than 7.5 hours sleep
low_sleep = df[df["sleep_hr"] < 7.5]
print("Days with under 7.5 hours sleep:")
print(low_sleep[["day", "sleep_hr"]].to_string())
#Multiple conditions
import pandas as pd

df = pd.DataFrame({
    "day":      ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "steps":    [9200, 10500, 8800, 11000, 7600, 9400, 10200],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0],
    "protocol": ["OMAD", "2MAD", "OMAD", "OMAD", "2MAD", "OMAD", "OMAD"],
    "cold_shower": [True, True, False, True, True, True, True],
})

# OMAD days with 10k+ steps
omad_goal = df[(df["protocol"] == "OMAD") & (df["steps"] >= 10000)]
print("OMAD days with 10k+ steps:")
print(omad_goal[["day", "steps", "protocol"]].to_string())

print()
# Days with either goal steps OR 8+ hours sleep
either = df[(df["steps"] >= 10000) | (df["sleep_hr"] >= 8.0)]
print("Days with 10k+ steps OR 8+ hrs sleep:")
print(either[["day", "steps", "sleep_hr"]].to_string())
#Filtering with .isin()
import pandas as pd

df = pd.DataFrame({
    "name":     ["James Omondi", "Sandra Weru", "Patrick Njiru", "Grace Achieng", "Brian Kamau", "Kevin Mwangi"],
    "city":     ["Nairobi", "Mombasa", "Nairobi", "Kisumu", "Nairobi", "Mombasa"],
    "steps":    [9200, 10500, 8100, 11000, 7400, 10800],
    "protocol": ["OMAD", "2MAD", "OMAD", "OMAD", "2MAD", "OMAD"],
})

# Members from Nairobi or Mombasa
nbi_msa = df[df["city"].isin(["Nairobi", "Mombasa"])]
print("Nairobi and Mombasa members:")
print(nbi_msa[["name", "city", "steps"]].to_string())
#Adding a new column
import pandas as pd

df = pd.DataFrame({
    "day":          ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "steps":        [9200, 10500, 8800, 11000, 7600, 9400, 10200],
    "sleep_hr":     [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0],
    "water_glasses":[7, 8, 6, 9, 8, 7, 8],
    "protocol":     ["OMAD", "2MAD", "OMAD", "OMAD", "2MAD", "OMAD", "OMAD"],
})

# Boolean column: did we hit the step goal?
df["hit_goal"] = df["steps"] >= 10000

# Numeric column: steps deficit or surplus vs 10k goal
df["steps_vs_goal"] = df["steps"] - 10000

# Category column: water rating
df["hydration"] = df["water_glasses"].apply(lambda x: "Good" if x >= 8 else "Low")

print(df[["day", "steps", "hit_goal", "steps_vs_goal", "hydration"]].to_string())
#Renaming and dropping columns
import pandas as pd

df = pd.DataFrame({
    "day":      ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "steps":    [9200, 10500, 8800, 11000, 7600],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0],
    "protocol": ["OMAD", "2MAD", "OMAD", "OMAD", "2MAD"],
    "notes":    ["ok", "great", "tired", "best", "rest"],
})

# Rename column
df = df.rename(columns={"sleep_hr": "sleep_hours"})
print("After rename:")
print(list(df.columns))

# Drop a column
df = df.drop(columns=["notes"])
print("After drop:")
print(df.to_string())
#Sorting
import pandas as pd

df = pd.DataFrame({
    "name":     ["James Omondi", "Sandra Weru", "Patrick Njiru", "Grace Achieng", "Brian Kamau", "Kevin Mwangi"],
    "steps":    [9200, 10500, 8100, 11000, 7400, 10800],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5],
})

# Sort by steps, highest first
ranked = df.sort_values("sleep_hr", ascending=False).reset_index(drop=True)
ranked.index = ranked.index + 1  # 1-based ranking
df["wake_up_score"] = df["sleep_hr"] * df["steps"] / 1000

print("Step leaderboard:")
for i, row in ranked.iterrows():
    print(f"  #{i}  {row['name']:<20} {row['steps']:,} steps")

#Applied example: Goat farm weight checker
import pandas as pd

data = {
    "goat": ["Simba", "Kijana", "Mzee", "Damu", "Furaha", "Pendo", "Jasiri"],
    "breed": ["Boer", "Galla", "Boer", "Galla", "Boer", "Galla", "Boer"],
    "weight_kg": [28, 19, 35, 14, 32, 22, 17],
    "age_months": [18, 12, 36, 8, 24, 15, 10]
}

df = pd.DataFrame(data)

# Flag underweight: Boer target 25kg, Galla target 18kg
def weight_status(row):
    target = 25 if row["breed"] == "Boer" else 18
    return "OK" if row["weight_kg"] >= target else "Needs feeding"

df["status"] = df.apply(weight_status, axis=1)
df["weight_gap_kg"] = df.apply(
    lambda r: max(0, (25 if r["breed"] == "Boer" else 18) - r["weight_kg"]), axis=1
)

# Show underweight animals sorted by gap
priority = df[df["status"] == "Needs feeding"].sort_values("weight_gap_kg", ascending=False)
print("Priority feeding list:")
print(priority[["goat", "breed", "weight_kg", "weight_gap_kg"]].to_string(index=False))