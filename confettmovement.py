from random import randint
import turtle
from turtle import forward, left, right, penup
import time
from makewindow import Confett, winheight, winwidth, wn, gifs

numofConfett = randint(2,5)
width = int(winwidth/2)

def sideways(temp0):
    leftright = randint(1,5)
    penup()
    if leftright == 1:
        temp0.left(90)
        temp0.speed(0)
        temp0.forward(randint(2,10))
        temp0.right(90)
        temp0.forward(randint(5,50))
    elif leftright == 2:
        temp0.right(90)
        temp0.speed(0)
        temp0.forward(randint(2,10))
        temp0.left(90)
        temp0.forward(randint(5,50))

def movement(temp1):
    penup()
    while (temp1.pos()[1] > -(winheight/2)):
        time.sleep(0.01)
        sideways(temp1)

def genConfett():    
    for i in range(0, numofConfett-1):
        globals()[f"turts{i}"] = turtle.Turtle(wn)
        Confett.append(globals()[f"turts{i}"])
        Confett[i].hideturtle()
        Confett[i].speed(speed=0)
        globals()[f"turts{i}"].shape(gifs[randint(0, len(gifs)-1)])
        Confett[i].penup()
        Confett[i].right(90)

def fall():
    for i in range(0, len(Confett)-1):
        wn.create_window(randint(-width+100, width-100), winheight/2)
        Confett[i].showturtle()
        movement(Confett[i])

fall()