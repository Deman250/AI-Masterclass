services = [
    {
        "name":    "Automated Data Reports",
        "client":  "small business owners who export data manually",
        "problem": "spending 2-4 hours per week copying data between spreadsheets and writing summaries",
        "outcome": "a Python script that reads their data source and produces a formatted weekly report in under 30 seconds",
        "tools":   "Python, pandas, CSV/Excel/JSON",
        "example": "28-day fitness log analysis with weekly breakdown and protocol comparison"
    },
    {
        "name":    "API Integration Scripts",
        "client":  "operations teams using two or more disconnected tools",
        "problem": "manually copying data between platforms with no automation between them",
        "outcome": "a Python script that pulls from one API and pushes to another automatically on a schedule",
        "tools":   "Python, requests, FastAPI, JSON",
        "example": "Multi-endpoint dashboard pulling from three simulated SMP data sources"
    },
    {
        "name":    "AI Writing Automation",
        "client":  "business owners who write the same types of responses repeatedly",
        "problem": "spending hours writing first drafts of emails, summaries, or customer responses",
        "outcome": "a Python tool that generates structured drafts using the OpenAI API in the required voice and format",
        "tools":   "Python, OpenAI API, python-dotenv",
        "example": "SMP coaching message generator that mirrors the Chat API response structure"
    },
    {
        "name":    "Financial Reconciliation Scripts",
        "client":  "Sacco treasurers and shop owners in Nairobi who reconcile M-Pesa statements by hand",
        "problem": "manually matching M-Pesa transaction messages against sales records every week, often taking a full afternoon",
        "outcome": "a script that automatically matches transaction records against sales logs and flags mismatches within minutes",
        "tools":   "Python, pandas, regex",
        "example": "data-analysis-report's cleaning and merging pipeline adapted to parse financial exports"
    }, 
]

for i, s in enumerate(services, 1):
    print(f"SERVICE {i}: {s['name'].upper()}")
    print()
    print(f"  Who I help:    {s['client']}")
    print(f"  Their problem: {s['problem']}")
    print(f"  What I deliver:{s['outcome']}")
    print(f"  Tools used:    {s['tools']}")
    print(f"  Proof of work: {s['example']}")
    print()

    # Generate a one-line pitch
    pitch = (f"I help {s['client']} by building {s['outcome'].split('a ')[1] if 'a ' in s['outcome'] else s['outcome']}.")
    print(f"  One-line pitch: \"{pitch}\"")
    print("-" * 60)
