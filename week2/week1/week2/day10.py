
contacts = [
    {"name": "James Omondi",  "phone": "0712345678", "skill": "welding",      "city": "Nairobi"},
    {"name": "Sandra Weru",   "phone": "0723456789", "skill": "tiling",       "city": "Mombasa"},
    {"name": "Patrick Njiru", "phone": "0734567890", "skill": "phone repair", "city": "Nairobi"},
    {"name": "Grace Achieng", "phone": "0745678901", "skill": "copywriting",  "city": "Kisumu"},
    {"name": "Brian Kamau",   "phone": "0756789012", "skill": "upholstery",   "city": "Nairobi"},
]

# Add two more contact
contacts.append({
    "name": "Kevin Mwangi",
    "phone": "0767890123",
    "skill": "beekeeping",
    "city": "Nakuru"
})
contacts.append({
    "name" : "Mary Jane",
    "phone" : "0713302043",
    "skill" : 'Farming',
    "city" : "Nairobi"
})


# Display all contacts
print("===== CONTACT BOOK PROJECT =====")
for i, contact in enumerate(contacts):
    print(f"\n{i+1}. {contact['name']}")
    print(f"   Phone : {contact['phone']}")
    print(f"   Skill : {contact['skill']}")
    print(f"   City  : {contact['city']}")

# Search by city
print("\n===== NAIROBI CONTACTS =====")
for contact in contacts:
    if contact["city"] == "Nairobi":
        print(f"  {contact['name']} | {contact['skill']}")

# Summary
print(f"\nTotal contacts: {len(contacts)}")

#EXERCISE1 : LIST OPERATIONS
# Create a list of 5 fruits
# Sort it, reverse it, then add one more item
fruits = ["mango", "banana", "apple", "orange", "grape"]
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)
fruits.append("pawpaw")
print(fruits)
fruits.insert(1, "pawpaw")
print(fruits)
fruits.pop(6)
print(fruits)

#EXERCISE2 : DICTIONARY WORK
# Create a dictionary for a student with name, age, and grade
# Print each value using the key
student = {"name": "Daniel", "age": 25, "grade": "A"}
print("=== Daniel results ===")
for key, value in student.items():
    print(f"{key}: {value}")

#EXERCISE3 : NESTED DATA
# Create a list of 3 student dictionaries
# Loop through and print each student's name and grade
print("=== Best students ===")
students = [
    {"name": "Daniel", "grade": "A"},
    {"name": "James", "grade": "B"},
    {"name": "Amina", "grade": "A"}
]
for s in students:
    print(f"{s['name']}: {s['grade']}")

# Build a simple phonebook
# Store 3 contacts as a dictionary of name: number
# Print a formatted contact list 
phonebook = {"Daniel": "0712345678", "James": "0798765432", "Amina": "0756123456"}
print("--- CONTACTS ---")
for name, number in phonebook.items():
    print(f"{name}: {number}")

#Create a calendar for the year 2027
months = ["January", "February", "March", "April", "May","June", "July", "August","September","October","November","December"]
dates_of_month = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
days_of_weeek = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
months_many_days = "January","March","May","July","August","October","December"
short_month = "February"

if max(dates_of_month) >= 31:
    print("months with many days:", months_many_days)

if min(dates_of_month) <= 29:
    print(short_month)
    print("days of the week", days_of_weeek)

# create month1 2027
month1 = {
    "month": "January",
    "days_of_the_week": days_of_weeek,
    "dates_of_month": dates_of_month[:31],
}

print("January:", month1)