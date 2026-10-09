# 1 вариант
import turtle

def koch_curve(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        koch_curve(t, length / 3, depth - 1)
        t.left(60)
        koch_curve(t, length / 3, depth - 1)
        t.right(120)
        koch_curve(t, length / 3, depth - 1)
        t.left(60)
        koch_curve(t, length / 3, depth - 1)

t = turtle.Turtle()
t.speed(0)
screen = turtle.Screen()
t.up()
t.goto(-200, 0)
t.down()
koch_curve(t, 400, 4)
screen.exitonclick()