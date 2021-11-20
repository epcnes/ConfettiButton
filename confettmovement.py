from random import randint
from turtle import forward, left, right, penup
import time
from makewindow import Confett, winheight, winwidth

width = winwidth/2

def sideways(temp0):
    leftright = randint(1,5)
    penup()
    if leftright == 1:
        temp0.left(90)
        temp0.speed(0)
        temp0.forward(randint(2,10))
        temp0.right(90)
        temp0.forward(randint(1,25))
    elif leftright == 2:
        temp0.right(90)
        temp0.speed(0)
        temp0.forward(randint(2,10))
        temp0.left(90)
        temp0.forward(randint(1,25))
    else:
        forward(randint(1,25))

def movement(temp1):
    penup()
    while (temp1.pos()[1] > -(winheight/2)):
        time.sleep(0.01)
        sideways(temp1)

def fall():
    for i in range(0, len(Confett)-1):
        Confett[i].goto(randint(-width+100, width-100), winheight/2)
        Confett[i].showturtle()
        movement(Confett[i])

fall()