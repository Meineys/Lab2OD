import turtle
import random


def draw_mountain(t, x1, y1, x2, y2, depth):
    if depth == 0:
        t.up()
        t.goto(x1, y1)
        t.down()
        t.goto(x2, y2)
        return

    xm = (x1 + x2) / 2
    ym = (y1 + y2) / 2 + random.randint(-20, 20) * depth

    draw_mountain(t, x1, y1, xm, ym, depth - 1)
    draw_mountain(t, xm, ym, x2, y2, depth - 1)


t = turtle.Turtle()
t.speed(0)
screen = turtle.Screen()
draw_mountain(t, -300, 0, 300, 0, 5)
screen.exitonclick()