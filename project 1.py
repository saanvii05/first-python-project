
print("WELCOME TO THE PYTHON QUIZ!")

score = 0

print("\nQuestion 1")
answer = input("Which language are we learning? ")

if answer.lower() == "python":
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")

print("\nQuestion 2")
answer = input("What is 5 + 5? ")

if answer == "10":
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")

print("\nQuestion 3")
answer = input("Which keyword is used for conditions? ")

if answer.lower() == "if":
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")

print("\nQuestion 4")
answer = input("What is the output of 2 * 3? ")

if answer == "6":
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")

print("\nQuestion 5")
answer = input("Which function takes user input? ")

if answer.lower() == "input":
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")

print("\nQUIZ COMPLETED!")
print("Your score is:", score, "/5")

if score == 5:
    print("Excellent!")
elif score >= 3:
    print("Good job!")
else:
    print("Keep practising!")
