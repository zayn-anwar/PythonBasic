from colorama import init, Fore, Back, Style
import time
init()

tasks = []
def addTask():
    taskName = input("Enter task name: ")
    tasks.append(taskName)
    print(f"{Back.GREEN}{taskName} added to the list.{Style.RESET_ALL}")
    time.sleep(1)
def removeTask():
    print(tasks)
    taskIndex = int(input("Which task index do you want to remove?"))
    if taskIndex >taskIndex > len(tasks):
        print(f"{Back.RED}#{taskIndex} is not in the list.{Style.RESET_ALL}")
        time.sleep(1)
    else:
        tasks.pop(taskIndex-1)
        print(f"{Back.GREEN}#{taskIndex} removed from the list.{Style.RESET_ALL}")
        time.sleep(1)
def displayTasks():
    if not tasks:
        print(f"{Back.RED}There are no tasks to display.{Style.RESET_ALL}")
        time.sleep(1)
    else:
        print(tasks)
        time.sleep(1)

if __name__ == "__main__":
    print("Welcome!")
    while True:
        print(f"{Back.YELLOW}{Style.BRIGHT}What would you like to do?{Style.RESET_ALL}")
        print(f"{Back.YELLOW}{Style.BRIGHT}--------------------------{Style.RESET_ALL}")
        print(f"{Back.YELLOW}{Style.BRIGHT}1. Add tasks              {Style.RESET_ALL}")
        print(f"{Back.YELLOW}{Style.BRIGHT}2. Remove tasks           {Style.RESET_ALL}")
        print(f"{Back.YELLOW}{Style.BRIGHT}3. Display tasks          {Style.RESET_ALL}")
        print(f"{Back.YELLOW}{Style.BRIGHT}4. Exit                   {Style.RESET_ALL}")
        print(f"{Back.YELLOW}{Style.BRIGHT}--------------------------{Style.RESET_ALL}")

        choice = input("Enter your choice: ")
        if choice == "1":
            addTask()
        elif choice == "2":
            removeTask()
        elif choice == "3":
            displayTasks()
        elif choice == "4":
            print("Goodbye!")
            time.sleep(1)
            break
