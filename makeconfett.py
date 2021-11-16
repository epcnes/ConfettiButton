from random import randint
import turtle
import os
import os.path
import tkinter as tk
from win32api import GetSystemMetrics

numofConfett = randint(5,10)
Confett = []
gifs = []
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

wn = turtle.Screen()
wn.screensize(canvheight=height, canvwidth=width)

#getting gifs#
path = os.getcwd() + "\\Coloured Confett"
directlist = os.listdir(path)
for i in range(0, len(directlist)-1):
    gifs.append(f"{path}//{directlist[i]}")
    wn.addshape(gifs[i])

for i in range(0, numofConfett):
    globals()[f"turts{i}"] = turtle.Turtle()
    Confett.append(globals()[f"turts{i}"])
    Confett[i].speed(speed=0)
    globals()[f"turts{i}"].shape(gifs[randint(0, len(gifs)-1)])
    Confett[i].penup()
    Confett[i].right(90)
    Confett[i].speed(5)