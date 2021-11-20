from random import randint
import turtle
import os
import os.path
import tkinter as tk
from win32api import GetSystemMetrics

gifs = []
winwidth = GetSystemMetrics(0)
winheight = GetSystemMetrics(1)

root = tk.Tk()
root.overrideredirect(True)
wn = tk.Canvas(master = root, width=winwidth, height=winheight, highlightthickness=0, bd=0)
wn.pack()
window = turtle.TurtleScreen(wn)

#getting gifs#
path = os.getcwd() + "\\Coloured Confett"
directlist = os.listdir(path)
for i in range(0, len(directlist)):
    gifs.append(f"{path}\\{directlist[i]}")
    window.addshape(gifs[i])