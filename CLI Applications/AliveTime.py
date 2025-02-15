## Made by ZIon Coding Incorporated

import datetime as dt

y = int(input("Which year were you born in?: "))
m = int(input("Which month were you born in? (Enter number): "))
d = int(input("Which day were you born on? (Enter number): "))

birth = dt.datetime(y, m, d)
current = dt.datetime.now()
answer = (current-birth)
print(f"You have been alive for {answer}")
