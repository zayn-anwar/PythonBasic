import time
import sys
sys.set_int_max_str_digits(0)

print("Calculator made by Zion")
time.sleep(5)
print("Operations are: ADDITION,SUBTRACTION,MULTIPLICATION,DIVISION,RAISED TO")
time.sleep(5)
first = int(input("Enter your first number: "))
operation = input("Enter your requested operation in full capital letters: ")
second = int(input("Enter your second number: "))
if operation == 'ADDITION':
    ans = (first+second)
    print(f"Your answer is {ans}")
if operation == 'SUBTRACTION':
    ans = (first-second)
    print(f"Your answer is {ans}")
if operation == 'MULTIPLICATION':
    ans = (first*second)
    print(f"Your answer is {ans}")
if operation == 'DIVISION':
    ans = (first/second)
    print(f"Your answer is {ans}")
if operation == 'RAISED TO':
    ans = (first**second)
    print(f"Your answer is {ans}")