from turtle import *

hideturtle()
color('black', 'magenta')

def left_turn():
    for i in range(10):
        forward(15)
        left(9)

def petal():
    begin_fill()
    left_turn()    # option A
    left(90)       # option B
    left_turn()
    end_fill()
    left(360/5 + 180 - 18)

for i in range(5): # option C
    petal()
    right(360/5)



bye()