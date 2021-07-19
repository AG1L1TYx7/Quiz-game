print("Welcome to my computer Quiz")

playing = input("Are you playing:  ")

if playing != "yes":
    quit()
print("Okay! let's begin the game😊: ")
score = 0

answer = input("What does GPU stand for?\n")
if answer == "graphical processing unit":
    print("yes😊")
    score += 1
else:
    print("Incorrect😒")

answer = input("What does CPU stand for?\n")
if answer.lower == "Central processing unit":
    print("yes😊")
    score += 1
else:
    print("Incorrect😒")

answer = input("What does OOP stand for?\n")
if answer.lower == "object oriented programming":
    print("yes😊")
    score += 1
else:
    print("Incorrect😒")

print("You got " + str(score) + "question correct " )
print("You got " + str(score/3 * 100) + "%" )
