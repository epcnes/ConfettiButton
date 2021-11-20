from random import randint
import turtle
import os
import os.path
import tkinter as tk
from win32api import GetSystemMetrics

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

root.mainloop()