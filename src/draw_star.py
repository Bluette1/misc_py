# see https://brilliant.org/courses/programming-python/#chapter-introduction-28

from turtle import *
speed(5)
width(5)

color('red', 'yellow')

begin_fill()
for i in range(5):  # change to range(7)
    right(180 - 36) # adjust this angle
    forward(200)
end_fill()