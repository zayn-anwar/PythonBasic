import sympy
from sympy import *

def checkForPrime(y):
    if sympy.isprime(y) == True:
        print (f"{y} is a prime.")
    else:
        print(f"{y} is not a prime.")
    
userInputNumber = int(input("Enter a number to check if it is a prime number: "))
checkForPrime(userInputNumber)
