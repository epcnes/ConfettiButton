from random import randint
from turtle import forward, left, right, penup
import time
from makeconfett import Confett, winheight, winwidth

width = winwidth/2

def movement(temp1):
    temp1.right(90)
    temp1.speed(0)
    while (temp1.pos()[1] > -(winheight/2)-750):
        side = randint(0,5)
        time.sleep(0.01)
        if (side == 3):
            #go right#
            temp1.left(90)
            temp1.forward(randint(1,5))
            temp1.right(90)
            temp1.forward(randint(10, 50))
        elif (side == 5):
            temp1.right(90)
            temp1.forward(randint(1,5))
            temp1.left(90)
            temp1.forward(randint(10, 50))
        else:
            temp1.forward(randint(10, 50))

def fall(confetti):
    confetti.goto(0, winheight/2)
    confetti.showturtle()
    movement(confetti)

fall(Confett)