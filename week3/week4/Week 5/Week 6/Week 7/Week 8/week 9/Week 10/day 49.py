from datetime import date

outreach_log = [
    {"date": "2026-07-08", "name": "Kamau Njoroge",   "channel": "LinkedIn",  "status": "replied",     "notes": "Interested in monthly report automation"},
    {"date": "2026-07-09", "name": "Wanjiku Ltd",     "channel": "WhatsApp",  "status": "no_reply",    "notes": "Sent portfolio link"},
    {"date": "2026-07-10", "name": "Aisha Waweru",    "channel": "X (DM)",    "status": "call_booked", "notes": "Call on July 16"},
    {"date": "2026-07-11", "name": "Mombasa Retail",  "channel": "LinkedIn",  "status": "no_reply",    "notes": "Owner active on LinkedIn"},
    {"date": "2026-07-12", "name": "Brian Omondi",    "channel": "Referral",  "status": "replied",     "notes": "Friend's contact, needs API work"},
    {"date": "2026-07-13", "name": "Njeri Kamau",     "channel": "Upwork",    "status": "proposal_sent","notes": "CSV cleanup job"},
    {"date": "2026-07-14", "name": "Eldoret Foods",   "channel": "In person", "status": "no_reply",    "notes": "Left business card"},
    {"date": "2026-07-15", "name": "Techbridge Ltd",  "channel": "LinkedIn",  "status": "replied",     "notes": "Wants scope document"},
]

# Summary stats
total    = len(outreach_log)
replied  = sum(1 for e in outreach_log if e["status"] in ("replied", "call_booked"))
calls    = sum(1 for e in outreach_log if e["status"] == "call_booked")
reply_rate = replied / total * 100

print("OUTREACH TRACKER SUMMARY")
print("=" * 50)
print(f"Total messages sent:  {total}")
print(f"Replies received:     {replied}  ({reply_rate:.0f}% reply rate)")
print(f"Calls booked:         {calls}")
print()

# By channel
channels = {}
for e in outreach_log:
    ch = e["channel"]
    channels[ch] = channels.get(ch, 0) + 1

print("By channel:")
for ch, count in sorted(channels.items(), key=lambda x: -x[1]):
    print(f"  {ch:<14} {count} sent")

print()
print("Calls to follow up:")
for e in outreach_log:
    if e["status"] == "call_booked":
        print(f"  {e['name']} ({e['date']}) -- {e['notes']}")

print()
print("Hot leads (replied):")
for e in outreach_log:
    if e["status"] == "replied":
        print(f"  {e['name']} via {e['channel']} -- {e['notes']}")
