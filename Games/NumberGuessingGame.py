import random as rm

print("Welcome to Number Guessing!")

dgcount1 = int(input("What should be the lowest number?: "))
dgcount2 = int(input ("What should be the highest number?: "))
noToGuess = rm.randint(dgcount1,dgcount2)
print ("The number has been generated.")

guess = int()
guesscount = 0
while guess != noToGuess:
    guess = int(input("What is the number?: "))
    guesscount+=1
    print (f"You have used {guesscount} guess/es")
    if guesscount>1:
        if guess>noToGuess:
            print ("You have guessed higher than the number!")
        elif guess<noToGuess:
            print ("You have guessed lower than the number!")
        else:
            break
    else:
        continue
if guess == noToGuess:
    print (f"You have won in {guesscount} tries!")
    print (f"The correct number was {noToGuess}!")
