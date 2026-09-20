name = input("Enter your name: ")
marks = int(input("Enter your marks (0-100): "))

if marks >= 80 and marks <= 100:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
elif marks >= 0:
    grade = "F"
else:
    grade = "Invalid marks"

print("Student: " + name)
print("Marks: " + str(marks))
print("Grade: " + grade)

if grade == "F":
    print("You failed. Keep practicing 💪")
elif grade != "Invalid marks":
    print("Congratulations! You passed 🎉")

if marks >= 90 and marks <= 100:
    print("Excellent performance! 🔥")

if marks >= 0 and marks < 30:
    print("You need serious improvement 📚")