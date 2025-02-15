import time as tm
import random as rm

def fighting():
    enemyoptions = ["Attack", "Defend"]
    enemyhealth = int(100)
    health = int(100)
    while health>(0) and enemyhealth>(0):
     option = input("Attack or Defend?: ")
     enemyoption = rm.choice(enemyoptions)
     if option == "Attack" and enemyoption == "Attack":
        enemyhealth = (enemyhealth-10)
        health = (health-10)
        print ("You and your enemy lost 10 health!")
     if option == "Defend" and enemyoption == "Attack":
        enemyhealth = (enemyhealth-20)
        print ("Your enemy lost 20 health!")
     if option == "Defend" and enemyoption == "Defend":
        enemyhealth = (enemyhealth-5)
        health = (health-5)
        print ("You and your enemy lost 5 health!")
     if option == "Attack" and enemyoption == "Defend":
        health = (health-20)
        print ("You lost 20 health!")
     print (f"Your health is {health}")
     print (f"Enemy health is {enemyhealth}")
    if health<=(0):
       print ("You have lost!")
    if enemyhealth<=(0) and health<=(0):
       print ("You have lost!")
    if enemyhealth<=(0) and health>(0):
       print ("You have won! Contact Zayn for your prize!!!!")

print ("IMMORTAL PEACE")
tm.sleep(2)
print ("A remake of Mortal Kombat but worse!")
tm.sleep(4)
ready = input("Ready to fight? (TYPE OK)")
if ready == "OK":
    print ('FIGHT!')
    fighting()
else:
    print('Play when ready!')
