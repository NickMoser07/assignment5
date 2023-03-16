import random

print("welcome to the guessing game\nThe computer has picked a number from 1 - 10. try to match it.")
computer = random.randint(1,10)
choice = int(input("what is your guess (1-10):   "))
if choice == computer:
    msg = "you picked " + str(choice) + ", the computer also chose 3" + str(computer)

else:
    msg = "you picked " + str(choice) + ", the computer picked " + str(computer) + "\nYoungling, your time will come."
print(msg)