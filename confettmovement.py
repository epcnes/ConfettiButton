from random import randint
from turtle import forward, left, right, penup
import time
from makeconfett import Confett

def sideways():
    leftright = randint(1,5)
    penup()
    if leftright == 1:
        Confett[0].left(180)
        Confett[0].speed(5)
        Confett[0].forward(randint(1,5))
        Confett[0].right(90)
        Confett[0].forward(100)
    elif leftright == 2:
        Confett[0].right(180)
        Confett[0].speed(5)
        Confett[0].forward(randint(1,5))
        Confett[0].left(90)
        Confett[0].forward(100)
    else:
        forward(100)

def movement(Confett):
    penup()
    while True:
        time.sleep(0.1)
        sideways()

movement(Confett[0])