# My week's steps count report
# Daily step counts for a week
week_steps = [9200, 7400, 105000, 8800, 6900, 11000, 9600]
for steps in week_steps:
    if steps >= 8000:
        print(steps, "- Goal hit!")
    else:
        print(steps, "-Below goal.")

 
print("Days tracked:", len(week_steps)) 

week_steps = [9200, 7400, 105000, 8800, 6900, 11000, 9600]
for steps in week_steps:
    if steps >= 8000:
        print(steps, "- Goal hit!")
    elif steps < 8000:
        print(steps, "- Work harder!Try to reach your step goal tomorrow.")    
    else:
        print(steps, "- Below goal.")