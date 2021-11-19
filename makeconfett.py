from random import randint
import turtle
import os
import os.path
import tkinter as tk
from win32api import GetSystemMetrics

numofConfett = randint(2,5)
Confett = []
gifs = []
winwidth = GetSystemMetrics(0)
winheight = GetSystemMetrics(1)

root = tk.Tk()
wn = tk.Canvas(master = root, width=winwidth, height=winheight, highlightthickness=0, bd=0)
wn.pack()

#getting gifs#
path = os.getcwd() + "\\Coloured Confett"
directlist = os.listdir(path)
for i in range(0, len(directlist)-1):
    gifs.append(f"{path}//{directlist[i]}")


for i in range(0, numofConfett-1):
    globals()[f"turts{i}"] = turtle.Turtle(wn)
    Confett.append(globals()[f"turts{i}"])
    Confett[i].hideturtle()
    Confett[i].speed(speed=0)
    globals()[f"turts{i}"].shape(gifs[randint(0, len(gifs)-1)])
    Confett[i].penup()
    Confett[i].right(90)

root.mainloop()