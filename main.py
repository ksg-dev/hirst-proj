from color import get_palette
from turtle import Turtle, Screen
import random

color_list = get_palette()
t = Turtle()
screen = Screen()
screen.colormode(255)


def paint(rows, dot_size, space_size):
    t.penup()
    t.right(180)
    half = (rows / 2) * (dot_size + space_size)
    t.forward(half)
    t.left(90)
    t.forward(half)
    t.left(90)
    cols = rows
    while cols > 0:
        for i in range(rows):
            t.dot(dot_size, random.choice(color_list))
            t.forward(space_size)
        print(t.heading())
        if t.heading() == 0:
            t.left(90)
            t.forward(space_size)
            t.left(90)
            t.forward(space_size)
        else:
            t.right(90)
            t.forward(space_size)
            t.right(90)
            t.forward(space_size)
        cols -= 1


paint(10,20,50)



screen.exitonclick()
