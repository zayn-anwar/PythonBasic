## Made by Zion Coding Incorporated

import time as tm
import random as rm

print("IMMORTAL PEACE")
tm.sleep(2)
print("u better like this bro")
tm.sleep(4)

print("Choose your character!: ")
characterlist = ["The Smiling Jinn", "Yo Thendi"]
character = input("The Smiling Jinn or Yo Thendi?: ")
while character not in characterlist:
    print("Invalid option.")
    character = input("The Smiling Jinn or Yo Thendi?: ")

ready = input("Ready to fight? (TYPE OK): ").strip().upper()
if ready != "OK":
    print("You must type 'OK' to fight")
    exit()

usedoptionslist = []
enemyoptions = ["Attack", "Defend"]
enemyhealth = 200
health = 100

powerused = False

while health > 0 and enemyhealth > 0:
    defendcount = usedoptionslist.count("Defend")
    powercount = usedoptionslist.count("Power")

    if powercount >= 1:
        print("(Power is unavailable)")
    
    if defendcount >= 3:
        option = input("Attack? Defend and Power have temporarily been removed: ").strip().capitalize()
        while option in ["Defend", "Power"]:
            print("Defend and Power have been temporarily disabled")
            option = input("Attack? Defend and Power have been temporarily removed: ").strip().capitalize()
        usedoptionslist.clear()

    else:
        option = input("Attack, Defend, or Power?: ").strip().capitalize()
        while option not in ["Attack", "Defend", "Power"]:
            print("Invalid option! Please type 'Attack', 'Defend', or 'Power'.")
            option = input("Attack, Defend, or Power?: ").strip().capitalize()

    usedoptionslist.append(option)
    enemyoption = rm.choice(enemyoptions)

    # Game mechanics
    if option == "Attack" and enemyoption == "Attack":
        enemyhealth -= 10
        health -= 10
        print("You and your enemy lost 10 health!")
    elif option == "Defend" and enemyoption == "Attack":
        enemyhealth -= 20
        print("Your enemy lost 20 health!")
    elif option == "Defend" and enemyoption == "Defend":
        enemyhealth -= 5
        health -= 5
        print("You and your enemy lost 5 health!")
    elif option == "Attack" and enemyoption == "Defend":
        health -= 20
        print("You lost 20 health!")

    if option == "Power" and not powerused:
        powerused = True
        if character == "The Smiling Jinn":
            enemyhealth -= 40
            print("You have used 'Invincible Hit'! Your enemy has lost 40 health!")
            option = input("Attack? You have lost the ability to use Defend and Power: ")
            while option != "Attack":
                print("Invalid option. Attack is only available.")
                option = input("Attack? You have lost the ability to use Defend and Power: ")
        elif character == "Yo Thendi":
            print("You have used 'Malayalam insults'! Your enemy has lost 30 health!")
            enemyhealth -= 30
            option = input("Attack or Defend?: ")
            if option == "Attack" and enemyoption == "Attack":
                health -= 5
                enemyhealth -= 5
                print("You and your enemy have lost 5 health!")
            elif option == "Defend" and enemyoption == "Attack":
                enemyhealth -= 20
                print("Your enemy has lost 20 health!")
    print(f"Your health is {health}")
    print(f"Your enemy's health is {enemyhealth}")

if health <= 0:
    print("You have lost!")
elif enemyhealth <= 0:
    print("You have won! Contact me for your prize!!!!")
