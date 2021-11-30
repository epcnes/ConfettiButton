from random import randint
import turtle
import os
from PIL import Image, ImageTk
import tkinter as tk
from win32api import GetSystemMetrics

gifs = []
winwidth = GetSystemMetrics(0)
winheight = GetSystemMetrics(1)

root = tk.Tk()
root.title("Confetti")
root.config(highlightbackground='black')
root.wm_attributes('-transparentcolor', 'black')
root.overrideredirect(True)

canvas = tk.Canvas(master=root, width=winwidth, height=winheight, highlightthickness=0)

canvas.pack()

wn = turtle.TurtleScreen(canvas)
wn.screensize(winwidth, winheight)
Confett = turtle.RawTurtle(wn)
Confett.hideturtle()
Confett.penup()

#getting gifs#
path = os.getcwd() + "\\Coloured Confett"
directlist = os.listdir(path)
for i in range(0, len(directlist)):
    gifs.append(f"{path}\\{directlist[i]}")
    wn.addshape(gifs[i])
 
Confett.shape(gifs[randint(0, len(gifs)-1)])