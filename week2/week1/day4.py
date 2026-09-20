#Daily discipline grader
steps = 12000
sleep_hours = 9
water_glasses = 10
cold_shower = True
page_read = 10
if steps >= 10000:
    print("Excellentjob! You met your step goal for the day.")
elif steps >= 7500:
    print("Good job! You made progress on your step goal for the day.")
else:
    print("Keep going! You can reach your step goal tomorrow.")
    
if sleep_hours >= 7:
    print("Great! You got enough sleep for the day.")
    

elif sleep_hours >= 5:
    print("You got some sleep, but try to get more for better health and productivity.")


if cold_shower:
    print("Good job! You took a cold shower today.")


if page_read >= 10 and page_read >= 15:
    print("Well done! You read enough pages today.")
    
elif page_read >= 5:
    print("Try to read more pages tomorrow for personal growth.")

#Summary of the day
print(f"Today's step count: {steps}")
print(f"Hours of sleep: {sleep_hours}")
print(f"Water glasses consumed: {water_glasses}")
print(f"Cold shower taken: {cold_shower}")
print(f"Pages read: {page_read}")

print(f"Today I walked {steps} steps, slept for {sleep_hours} hours, drank {water_glasses} glasses of water, took a cold shower: {cold_shower}, and read {page_read} pages.")