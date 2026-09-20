#API configuration
print("=== Loading API configuration... ====")
import os

# Configuration
BASE_URL = "https://api.smptracker.com/v1"
API_KEY = os.environ.get("SMP_API_KEY", "demo_key_123")
DEFAULT_CITY = "Nairobi"
STEP_GOAL = 10000
MAX_RESULTS = 50

print("Configuration loaded:")
print(f"  Base URL:   {BASE_URL}")
print(f"  API Key:    {API_KEY[:8]}...")
print(f"  City:       {DEFAULT_CITY}")
print(f"  Step Goal:  {STEP_GOAL:,}")
print(f"  Max Results:{MAX_RESULTS}")

#Fetching data from the API
print("=== Fetching data from the API... ====")
# Simulates what a fetch function does in a script

def fetch_members(city="Nairobi", limit=50):
    """
    Fetches member data from the SMP API.
    Returns a list of member dicts or raises RuntimeError.
    In production: uses requests.get() with headers and params.
    """
    # Simulate the API response
    mock_response_status = 200
    mock_data = [
        {"id": 1, "name": "James Omondi",  "city": "Nairobi",  "steps": 9200,  "protocol": "OMAD"},
        {"id": 2, "name": "Sandra Weru",   "city": "Nairobi",  "steps": 10500, "protocol": "2MAD"},
        {"id": 3, "name": "Patrick Njiru", "city": "Mombasa",  "steps": 8100,  "protocol": "OMAD"},
        {"id": 4, "name": "Grace Achieng", "city": "Nairobi",  "steps": 11000, "protocol": "OMAD"},
        {"id": 5, "name": "Brian Kamau",   "city": "Kisumu",   "steps": 7400,  "protocol": "2MAD"},
        {"id": 6, "name": "Kevin Mwangi",  "city": "Nairobi",  "steps": 10800, "protocol": "OMAD"},
    ]

    if mock_response_status != 200:
        raise RuntimeError(f"API error: status {mock_response_status}")

    # Filter by city
    filtered = [m for m in mock_data if m["city"] == city]
    return filtered[:limit]


# Call the function
members = fetch_members(city="Nairobi")
print(f"Fetched {len(members)} members from Nairobi")
for m in members:
    print(f"  {m['name']}: {m['steps']} steps")
#processing the data
print("=== Processing data... ====")
def process_members(members, step_goal=10000):
    """
    Takes a list of raw member records.
    Returns a summary dict with stats and categorized members.
    """
    if not members:
        return {"error": "No members to process"}

    total = len(members)
    goal_met = [m for m in members if m["steps"] >= step_goal]
    goal_missed = [m for m in members if m["steps"] < step_goal]
    avg_steps = round(sum(m["steps"] for m in members) / total)
    top_performer = max(members, key=lambda m: m["steps"])

    return {
        "total_members": total,
        "goal_met_count": len(goal_met),
        "goal_missed_count": len(goal_missed),
        "average_steps": avg_steps,
        "top_performer": top_performer["name"],
        "top_steps": top_performer["steps"],
        "goal_met": [m["name"] for m in goal_met],
    }


# Test with sample data
raw_members = [
    {"name": "James Omondi",  "steps": 9200,  "protocol": "OMAD"},
    {"name": "Sandra Weru",   "steps": 10500, "protocol": "2MAD"},
    {"name": "Grace Achieng", "steps": 11000, "protocol": "OMAD"},
    {"name": "Brian Kamau",   "steps": 7400,  "protocol": "2MAD"},
    {"name": "Kevin Mwangi",  "steps": 10800, "protocol": "OMAD"},
]

summary = process_members(raw_members, step_goal=10000)
print("Processed summary:")
for key, value in summary.items():
    print(f"  {key}: {value}")

#outputting the results
print("=== Outputting results... ====")
import json

def print_report(summary, city="Nairobi"):
    print("=" * 48)
    print(f"  SMP MEMBER REPORT: {city.upper()}")
    print("=" * 48)
    print(f"  Total members:    {summary['total_members']}")
    print(f"  Hit step goal:    {summary['goal_met_count']}")
    print(f"  Missed goal:      {summary['goal_missed_count']}")
    print(f"  Average steps:    {summary['average_steps']:,}")
    print(f"  Top performer:    {summary['top_performer']} ({summary['top_steps']:,} steps)")
    print("-" * 48)
    print("  Members who hit goal:")
    for name in summary["goal_met"]:
        print(f"    {name}")
    print("=" * 48)


summary = {
    "total_members": 5,
    "goal_met_count": 3,
    "goal_missed_count": 2,
    "average_steps": 9780,
    "top_performer": "Grace Achieng",
    "top_steps": 11000,
    "goal_met": ["Sandra Weru", "Grace Achieng", "Kevin Mwangi"]
}

print_report(summary, city="Nairobi")

# Save to JSON
output = json.dumps(summary, indent=2)
print("\nJSON output saved:")
print(output)

#putting it all together
print("=== Putting it all together... ====")
import json
import os

# --- Configuration ---
BASE_URL = "https://api.smptracker.com/v1"
API_KEY = os.environ.get("SMP_API_KEY", "demo_key_123")
TARGET_CITY = "Mombasa"
STEP_GOAL = 10000

# --- Fetch ---
def fetch_members(city, limit=50):
    # Simulated API response
    all_members = [
        {"name": "James Omondi",  "city": "Nairobi",  "steps": 9200,  "protocol": "OMAD", "sleep": 7.5},
        {"name": "Sandra Weru",   "city": "Nairobi",  "steps": 10500, "protocol": "2MAD", "sleep": 8.0},
        {"name": "Patrick Njiru", "city": "Mombasa",  "steps": 8100,  "protocol": "OMAD", "sleep": 6.5},
        {"name": "Grace Achieng", "city": "Nairobi",  "steps": 11000, "protocol": "OMAD", "sleep": 7.0},
        {"name": "Brian Kamau",   "city": "Kisumu",   "steps": 7400,  "protocol": "2MAD", "sleep": 9.0},
        {"name": "David Kiptoo", "city": "Mombasa", "steps": 15000, "protocol": "2MAD", "sleep": 7.0},
        {"name": "Kevin Mwangi",  "city": "Nairobi",  "steps": 10800, "protocol": "OMAD", "sleep": 7.5}
    ]
    return [m for m in all_members if m["city"] == city][:limit]

# --- Process ---
def process_members(members, step_goal):
    goal_met = [m for m in members if m["steps"] >= step_goal]
    avg_steps = round(sum(m["steps"] for m in members) / len(members)) if members else 0
    avg_sleep = round(sum(m["sleep"] for m in members) / len(members), 1) if members else 0
    top = max(members, key=lambda m: m["steps"]) if members else {}
    return {
        "total": len(members),
        "goal_met": len(goal_met),
        "avg_steps": avg_steps,
        "avg_sleep": avg_sleep,
        "top_name": top.get("name", "N/A"),
        "top_steps": top.get("steps", 0),
        "achievers": [m["name"] for m in goal_met]
    }

# --- Output ---
def print_report(city, summary):
    print(f"\n{'='*48}")
    print(f"  SMP DAILY REPORT: {city.upper()}")
    print(f"{'='*48}")
    print(f"  Members:       {summary['total']}")
    print(f"  Hit {STEP_GOAL:,} steps: {summary['goal_met']}")
    print(f"  Avg steps:     {summary['avg_steps']:,}")
    print(f"  Avg sleep:     {summary['avg_sleep']} hrs")
    print(f"  Top:           {summary['top_name']} ({summary['top_steps']:,})")
    print(f"\n  Achievers: {', '.join(summary['achievers'])}")
    print(f"{'='*48}\n")

# --- Main ---
members = fetch_members(TARGET_CITY)
summary = process_members(members, STEP_GOAL)
print_report(TARGET_CITY, summary)

#Example 2; Data for Dairy Farmers
import json

# --- Configuration ---
COOPERATIVE = "Githunguri Dairy Cooperative"
MIN_LITRES = 10.0   # flag farms below this daily target

# --- Fetch ---
def fetch_farm_readings():
    # Simulated readings from morning collection
    return [
        {"farm": "Kamau wa Njoroge",  "location": "Githunguri", "litres": 22.5, "cows": 3},
        {"farm": "Wanjiku Farm",      "location": "Limuru",     "litres": 18.0, "cows": 2},
        {"farm": "Mwangi Dairy",      "location": "Githunguri", "litres": 31.5, "cows": 4},
        {"farm": "Achieng Holdings",  "location": "Thika",      "litres": 11.0, "cows": 2},
        {"farm": "Kariuki Homestead", "location": "Limuru",     "litres": 26.0, "cows": 3},
        {"farm": "Calpha Dairy", "location": "Limuru", "litres": 50.8, "cows": 7}
    ]

# --- Process ---
def process_readings(readings, min_litres):
    total = sum(r["litres"] for r in readings)
    avg = round(total / len(readings), 1) if readings else 0
    below_target = [r for r in readings if r["litres"] < min_litres]
    top = max(readings, key=lambda r: r["litres"])
    return {
        "farms_collected": len(readings),
        "total_litres": total,
        "average_litres": avg,
        "below_target": [r["farm"] for r in below_target],
        "top_farm": top["farm"],
        "top_litres": top["litres"]
    }

# --- Output ---
def print_farm_report(cooperative, summary):
    print(f"\n{'='*50}")
    print(f"  DAILY REPORT: {cooperative.upper()}")
    print(f"{'='*50}")
    print(f"  Farms collected:   {summary['farms_collected']}")
    print(f"  Total litres:      {summary['total_litres']:.1f} L")
    print(f"  Average per farm:  {summary['average_litres']} L")
    print(f"  Top farm:          {summary['top_farm']} ({summary['top_litres']} L)")
    if summary["below_target"]:
        print(f"  Below target:      {', '.join(summary['below_target'])}")
    else:
        print("  All farms met target today.")
    print(f"{'='*50}\n")

# --- Main ---
readings = fetch_farm_readings()
summary  = process_readings(readings, MIN_LITRES)
print_farm_report(COOPERATIVE, summary)
