from random import randint
import turtle
import os
from PIL import Image, ImageTk
import tkinter as tk
from win32api import GetSystemMetrics

numofConfett = randint(5,10)
Confett = []
gifs = []
winwidth = GetSystemMetrics(0)
winheight = GetSystemMetrics(1)

root = tk.Tk()
root.configure(width=winwidth, height=winheight)
root.overrideredirect(True)
wn = tk.Canvas(root, width=20, height=20, bg='black')

#getting gifs#
path = os.getcwd() + "\\Coloured Confett"
directlist = os.listdir(path)
for i in range(0, len(directlist)):
    gifs.append(f"{path}//{directlist[i]}")

for i in range(0, numofConfett):
    img = ImageTk.PhotoImage(Image.open(gifs[randint(0, len(gifs)-1)]))
    globals()[f"confetts{i}"] = wn.create_image(x=randint(-winwidth+100, winwidth-100), y=winheight/2)
    Confett.append(globals()[f"confetts{i}"])