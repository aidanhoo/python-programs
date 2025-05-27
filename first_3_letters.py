"""
Create a project that asks for the user’s full name, 
store it and display only the first letter of the full name. 
Ask for the year of birth as well and calculate the age. 
Display the name and age in a window. At the same time, 
write the result of the execution to the Output Panel.
"""

import tkinter as tk
import time
from datetime import datetime

def askUser():
    userName = input("What is your name?\n")
    userBirth = int(input("What year were you born?\n"))
    return userName, userBirth

def getFirst3Letters(string:str) -> str:
    return string[:3].title()

def calcUserAge(birth):
    # return datetime.now().year - userBirth
    pass

def openWindow():
    root = tk.Tk()
    root.title("Heyo")
    root.geometry("500x300")
    root.mainloop()
    label = tk.Label(root, text="Hello, Tkinter!")
    label.pack()

def main():
    openWindow()

if __name__ == "__main__":
    main()