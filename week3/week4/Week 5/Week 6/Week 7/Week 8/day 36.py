# Python and JavaScript 

print("\n ===== VARIABLES AND DATA TYPES IN JAVASCRIPT =======")
# Fixed values
# We use const to declare variables that do not change in JavaScript
#const athleteName = "Wanjiku";
athleteName = "Wanjiku"
protocol = "SMP Phase 1"
targetSteps = 10000

# variables that change we use let in JavaScript
#let dayNumber = 1;
#let stepCount = 0;
dayNumber = 1
stepCount = 0

#we use console.log() in JavaScript to print to the console
#console.log("Athlete:", athleteName);
print("Athlete:", athleteName)
print("Protocol:", protocol)
print("Target steps:", targetSteps)

# Reassign variable
dayNumber = 7
stepCount = 11240

print("\nDay:", dayNumber)
print("Steps logged:", stepCount)
print("Hit goal:", stepCount >= targetSteps)

# type() checks the data type
print("\nTypes:")
print("athleteName:", type(athleteName).__name__)   # str
print("targetSteps:", type(targetSteps).__name__)   # int
print("hit goal:", type(True).__name__)             # bool


