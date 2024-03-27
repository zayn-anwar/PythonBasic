import time
import random

print("Welcome to High or Low!")
time.sleep(1)
print("In this game, we will give you a random number and you have to guess if the answer is higher or lower than the random number.")
time.sleep(3)
max_num = int(input("Enter the maximum number of the range out of which the random number will be selected: "))

number = random.randint(0, max_num)  # This is the number they have to guess
givennumber = random.randint(0, max_num)  # This is the number from which they have to find if the 'number' variable if higher or lower
print("Working...")
time.sleep(2)
higherorlower = input(f"Is the number higher or lower than {givennumber}? ")

if higherorlower.lower() == "higher":
    if givennumber < number:
        print("YOU'VE GUESSED THE ANSWER!")
        print(f"The number was {number}!")
    elif givennumber > number:
        print("It was actually lower!")
        print(f"The number was {number}")
elif higherorlower.lower() == "lower":
    if givennumber > number:
        print("YOU'VE GUESSED THE ANSWER!")
        print(f"The number was {number}!")
    elif givennumber < number:
        print("It was actually higher!")
        print(f"The number was {number}")