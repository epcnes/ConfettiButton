from random import randint
import turtle
import os
import os.path
import tkinter as tk
from win32api import GetSystemMetrics

numofConfett = randint(10,20)
Confett = []
winwidth = GetSystemMetrics(0)
winheight = GetSystemMetrics(1)

wn = tk.Canvas(width=winwidth, height=winheight, highlightthickness=0, bd=0)

def maker():
    gifs = []
    win = []
    #getting gifs#
    path = os.getcwd() + "\\Coloured Confett"
    directlist = os.listdir(path)
    for i in range(0, len(directlist)-1):
        gifs.append(f"{path}//{directlist[i]}")
    for i in range(0, numofConfett-1):
        globals()[f"confetti#{i}"] = tk.PhotoImage(file=gifs[randint(0, len(gifs)-1)])
        win.append(globals()[f"confetti#{i}"])
    window = tk.Tk()
    window.config(highlightbackground='black')
    window.overrideredirect(True)
    window.wm_attributes('-transparent', 'black')

maker()  

# for i in range(0, numofConfett-1):
#     globals()[f"turts{i}"] = turtle.Turtle()
#     Confett.append(globals()[f"turts{i}"])
#     Confett[i].hideturtle()
#     Confett[i].speed(speed=0)
#     globals()[f"turts{i}"].shape(gifs[randint(0, len(gifs)-1)])
#     Confett[i].penup()
#     Confett[i].right(90)