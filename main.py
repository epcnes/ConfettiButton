from random import randint
from turtle import forward, left, right, penup
import time
import turtle
import os
import tkinter as tk

#defining things#
root = tk.Tk()
gifs = []
winwidth = root.winfo_screenwidth()
winheight = root.winfo_screenwidth()
width = winwidth/2

#make window#
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
#random confetti#
Confett.shape(gifs[randint(0, len(gifs)-1)])

def movement(temp1):
    temp1.right(90)
    temp1.speed(0)
    while (temp1.pos()[1] > -(winheight/2)):
        side = randint(0,5)
        time.sleep(0.01)
        if (side == 3):
            #go right#
            temp1.left(90)
            temp1.forward(randint(1,10))
            temp1.right(90)
            temp1.forward(randint(10, 50))
        elif (side == 5):
            temp1.right(90)
            temp1.forward(randint(1,10))
            temp1.left(90)
            temp1.forward(randint(10, 50))
        else:
            temp1.forward(randint(10, 50))

def fall(confetti):
    confetti.goto(0, 1750)
    confetti.showturtle()
    movement(confetti)

fall(Confett)