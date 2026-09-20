#daily discipline report
def day_report(steps,water,protocol):
    
    print("===Daily Report===")
    print(f"steps   : {steps}")
    print(f"water   : {water} glasses")
    print(f"protocol : {protocol}")
    print()

def hit_goal(steps):
    return steps >= 8000

day_report(9200, 8, "OMAD")
day_report(7500, 6, "2MAD")
day_report(11000, 9, "Autophagy Marathon")

print("Goal hit (9200)?", hit_goal(9200))
print("Goal hit (7500)?", hit_goal(7500))

def get_status(steps):
    print("===Steps Report===")
    if steps >= 10000:
        print(steps, "Exceeded")
    elif steps >= 8000:
        print(steps, "Hit")
    else:
        print(steps, "Missed")
    return "Exceeded"

get_status(12000)
