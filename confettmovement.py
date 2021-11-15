from random import randint
from turtle import forward, left
from makeconfett import Confett

def movement():
    while True:
        leftright = randint(1,2)
        if leftright == 1:
            Confett[0].left(180)
            Confett[0].speed(5)
            Confett[0].forward(randint(1,5))
            Confett[0].right(90)
            Confett[0].forward(100)
        else:
            Confett[0].right(180)
            Confett[0].speed(5)
            Confett[0].forward(randint(1,5))
            Confett[0].left(90)
            Confett[0].forward(100)