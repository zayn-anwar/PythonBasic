## Made by Zion Coding Industries

import requests
import json
import tkinter

root = tkinter.Tk()
root.geometry("500x150")
root.title("Zion's Horrible Jokes")
root.configure(bg="yellow")

joke = tkinter.StringVar()
punchline = tkinter.StringVar()

def givejoke():
    x = requests.get('https://official-joke-api.appspot.com/jokes/random')
    data = x.json()
    joke = data["setup"]
    punchline = data["punchline"]
    jLabel.config(text = (joke))
    pLabel.config(text = (punchline))

jLabel = tkinter.Label(root, text=("Zion Coding Incorporated presents"), bg="white")
jLabel.place(x=120, y=20)
pLabel = tkinter.Label(root, text=("Jokes to ruin your comedy reputation"), bg="white")
pLabel.place(x=120, y=50)

jButton = tkinter.Button(root, text="Give me a joke!", command=givejoke, bg="white")
jButton.place(x=120, y=100)

root.mainloop()
