#creating a file called day1.py in the week4 folder
with open("day1.py", "w") as f:
    f.write("# This is day 1 of week 4\n")
    f.write("print('Hello, this is day 1 of week 4!')\n")
    f.write("print('This file is located in the week4 folder.')\n")
    f.write("print('This is a simple Python script.')\n")
with open("day1.py", "r") as f:
    content = f.read()
    print("File read. Contents:")
    print(content)
    with open("day1.py", "w") as f:
        f.write("print('This line was added to the file.')\n")

items = ["apple", "banana", "cherry", "date", "elderberry"]
with open("day1.py", "w") as f:
    f.write("print('This line was added to the file.')\n")


