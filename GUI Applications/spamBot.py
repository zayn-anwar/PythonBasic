# Developed by Zion Coding Incorporated

import tkinter as tk
from threading import Thread
import pyautogui
import keyboard
import time

stop_spam = False

def spam(message, amount):
    global stop_spam
    stop_spam = False
    time.sleep(3) 
    for i in range(amount):
        if stop_spam:
            print("Stopped by user.")
            break
        pyautogui.write(message)
        pyautogui.press("enter")
        time.sleep(1)
    start_button.config(state="normal")
    stop_button.config(state="disabled")
    status_label.config(text="Spamming stopped.")

def start_spam():
    message = message_entry.get()
    try:
        amount = int(amount_entry.get())
    except ValueError:
        status_label.config(text="Amount must be a number")
        return
    if not message:
        status_label.config(text="Message cannot be empty")
        return

    status_label.config(text="Starting in 3 seconds... Switch to your target window.")
    start_button.config(state="disabled")
    stop_button.config(state="normal")

    Thread(target=spam, args=(message, amount), daemon=True).start()

def stop_spam_func():
    global stop_spam
    stop_spam = True
    status_label.config(text="Stopping...")

keyboard.add_hotkey('esc', stop_spam_func)

root = tk.Tk()
root.title("Mad Spamming")
root.geometry("400x300")

tk.Label(root, text="Message to spam:").pack(pady=5)
message_entry = tk.Entry(root, width=50)
message_entry.pack()

tk.Label(root, text="Amount of times:").pack(pady=5)
amount_entry = tk.Entry(root, width=20)
amount_entry.pack()

start_button = tk.Button(root, text="Start Spamming", command=start_spam)
start_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop Spamming", command=stop_spam_func, state="disabled")
stop_button.pack()

status_label = tk.Label(root, text="")
status_label.pack(pady=10)

print("Press ESC anytime to stop spamming.")

def run_keyboard():
    keyboard.wait()

Thread(target=run_keyboard, daemon=True).start()

root.mainloop()
