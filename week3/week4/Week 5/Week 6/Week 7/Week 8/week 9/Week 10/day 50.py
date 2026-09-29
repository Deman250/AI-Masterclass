# Service offer
print("===== SERVICE OFFER =====")

def service_offer(skill, price, delivery):
    return f"Service: {skill} | Price: KES {price} | Delivery: {delivery} days"

print(service_offer("Python Automation", 15000, 3))
print(service_offer("Data Report", 8000, 2))

print("\n===== MY FULL AI MASTERCLASS CURRICULUM =====")
weeks = [
    {
        "week": 1, "title": "Python Foundations",
        "skills": ["Variables & types", "Conditionals", "Loops", "Functions"],
        "mini_project": "SMP stats calculator"
    },
    {
        "week": 2, "title": "Lists and Dictionaries",
        "skills": ["List methods", "Nested structures", "Dict operations", "JSON"],
        "mini_project": "Training log data processor"
    },
    {
        "week": 3, "title": "Functions and Modules",
        "skills": ["Parameters", "Return values", "Imports", "Lambda"],
        "mini_project": "Habit analysis module"
    },
    {
        "week": 4, "title": "Files, Errors, and Data",
        "skills": ["CSV/JSON I/O", "Error handling", "Data cleaning", "Pipelines"],
        "mini_project": "Health data pipeline"
    },
    {
        "week": 5, "title": "APIs and Automation",
        "skills": ["GET/POST requests", "Auth headers", "OpenAI API", "Prompts"],
        "mini_project": "AI coaching report generator"
    },
    {
        "week": 6, "title": "Pandas and NumPy",
        "skills": ["DataFrames", "Filtering", "Groupby", "Matplotlib"],
        "mini_project": "SMP analytics dashboard"
    },
    {
        "week": 7, "title": "Machine Learning",
        "skills": ["scikit-learn", "Train/test split", "Classifiers", "Prediction"],
        "mini_project": "AI-powered health app"
    },
    {
        "week": 8, "title": "JavaScript and Web",
        "skills": ["DOM manipulation", "Fetch API", "Async/await", "Full-stack"],
        "mini_project": "Browser-based AI coaching tool"
    },
    {
        "week": 9, "title": "Git and GitHub",
        "skills": ["Commits", "Branches", "GitHub", "Pull requests"],
        "mini_project": "Public GitHub portfolio"
    },
    {
        "week": 10, "title": "Portfolio and Freelance",
        "skills": ["Portfolio structure", "Service offer", "Pricing", "Outreach"],
        "mini_project": "First client acquisition pipeline"
    },
]

total_skills = sum(len(w["skills"]) for w in weeks)
total_days   = len(weeks) * 5

print("AI MASTERCLASS COURSE SUMMARY")
print("=" * 60)
print(f"Total days completed:   {total_days}")
print(f"Total weeks completed:  {len(weeks)}")
print(f"Distinct skills built:  {total_skills}+")
print()

print(f"{'WK':<4} {'TITLE':<26} {'MINI PROJECT'}")
print("-" * 60)
for w in weeks:
    print(f"W{w['week']:<3} {w['title']:<26} {w['mini_project']}")

print()
print("SKILLS ACQUIRED BY DOMAIN")
print("-" * 60)
domains = {
    "Backend / Python":    ["Variables & types","Conditionals","Loops","Functions","CSV/JSON I/O","Error handling","DataFrames","Filtering","Groupby","scikit-learn","Train/test split"],
    "APIs / Automation":   ["GET/POST requests","Auth headers","OpenAI API","Prompts","Async/await"],
    "Frontend / Web":      ["DOM manipulation","Fetch API","Full-stack"],
    "Data / ML":           ["Classifiers","Prediction","Matplotlib","Pipelines"],
    "Tools / Workflow":    ["Commits","Branches","GitHub","Pull requests","Portfolio structure","Pricing","Outreach"],
}
for domain, skills in domains.items():
    print(f"  {domain:<24} {len(skills)} skills")

print()
print("Status: GRADUATED. What comes next is your call.")
