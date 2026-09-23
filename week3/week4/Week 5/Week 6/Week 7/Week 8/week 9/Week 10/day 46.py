#Generate a portfolio summary for a developer with multiple projects.
print("\n ===== Generating developer portfolio summary =====")
projects = [
    {
        "title":   "SMP Performance Coach",
        "problem": "Manually tracking fitness data and writing coaching notes took 30+ minutes per day.",
        "solution":"Automated pipeline that trains a classifier on 28 days of data, predicts daily goal achievement, and generates a coaching message.",
        "tools":   ["Python", "scikit-learn", "pandas", "FastAPI"],
        "result":  "Prediction + coaching in under 2 seconds. Exports weekly JSON report.",
        "github":  "github.com/Deman250/smp-tracker",
        "type":    "ML + API"
    },
    {
        "title":   "Multi-Endpoint API Dashboard",
        "problem": "Three separate data sources with no unified view. Reporting was manual and inconsistent.",
        "solution":"Dashboard that fetches from three endpoints, processes each independently, and outputs a combined summary with protocol comparison.",
        "tools":   ["Python", "requests", "pandas"],
        "result":  "Single command produces a full multi-source report. Reduced prep time by 90%.",
        "github":  "github.com/Deman250/api-dashboard",
        "type":    "Data Pipeline"
    },
    {
        "title":   "Browser-Based AI Coach",
        "problem": "Clients needed a way to get coaching feedback without installing software.",
        "solution":"Client-side JavaScript tool. Prediction engine and coaching generator run entirely in the browser. No server required.",
        "tools":   ["JavaScript", "DOM API", "Fetch API"],
        "result":  "Zero setup for end users. Works on any device with a browser.",
        "github":  "github.com/Deman250/browser-coach",
        "type":    "Web Tool"
    },
    {
        "title": "Data-analysis Pipeline",
        "problem": "Data from multiple sources needed to be cleaned, merged, and analyzed.",
        "solution": "Automated pipeline that cleans, merges, and analyzes data from multiple sources, producing a comprehensive report.",
        "tools": ["Python", "pandas", "NumPy", "Matplotlib"],
        "result": "Produces a comprehensive report from cleaned and merged data.",
        "github": "github.com/Deman250/data-analysis-pipeline",
        "type": "Data Analysis"
    },
]

SEPARATOR = "=" * 64

print(SEPARATOR)
print("  DEVELOPER PORTFOLIO SUMMARY")
print(SEPARATOR)

for i, p in enumerate(sorted(projects, key=lambda p: p["type"]), 1):
    print(f"\nProject {i}: {p['title']}  [{p['type']}]")
    print(f"  Problem:  {p['problem']}")
    print(f"  Solution: {p['solution']}")
    print(f"  Tools:    {', '.join(p['tools'])}")
    print(f"  Result:   {p['result']}")
    print(f"  Code:     {p['github']}")

print()
print(SEPARATOR)
print(f"  Total projects: {len(projects)}")
all_tools = set(t for p in projects for t in p["tools"])
print(f"  Tech stack:     {', '.join(sorted(all_tools))}")
print(SEPARATOR)
