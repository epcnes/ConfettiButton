from random import randint
from turtle import forward, left, right, penup
import time
from makeconfett import Confett

def sideways(temp0):
    leftright = randint(1,5)
    penup()
    if leftright == 1:
        temp0.left(90)
        temp0.speed(0)
        temp0.forward(randint(1,5))
        temp0.right(90)
        temp0.forward(randint(1,25))
    elif leftright == 2:
        temp0.right(90)
        temp0.speed(0)
        temp0.forward(randint(1,5))
        temp0.left(90)
        temp0.forward(randint(1,25))
    else:
        forward(randint(1,25))

def movement(temp1):
    penup()
    while True:
        time.sleep(0.01)
        sideways(temp1)
        position = list(temp1.pos())
        print(position[1])

for i in range(0, len(Confett)-1):
    movement(Confett[i])