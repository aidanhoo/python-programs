"""
Create a project that asks for the user’s full name, 
store it and display only the first letter of the full name. 
Ask for the year of birth as well and calculate the age. 
Display the name and age in a window. At the same time, 
write the result of the execution to the Output Panel.
"""

import tkinter as tk
from datetime import datetime

def askUser():
    global userName, userBirth
    userName = input("What is your name?\n")
    userBirth = int(input("What year were you born?\n"))

def getFirst3Letters(string:str) -> str:
    return string[:3].title()

def calcUserAge(birth):
    return datetime.now().year - userBirth

def openWindow():
    root = tk.Tk()
    root.geometry("400x300")

if __name__ == "__main__":
    openWindow()
    # askUser()
    # print(calcUserAge(userBirth))