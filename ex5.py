import turtle
import random


def tree(branchLen, t):
    if branchLen > 5:
        t.pensize(branchLen / 10)

        if branchLen < 20:
            t.color("green")
        else:
            t.color("brown")

        t.forward(branchLen)

        angle = random.randint(15, 45)
        sub_len = random.randint(5, 15)

        t.right(angle)
        tree(branchLen - sub_len, t)

        t.left(angle * 2)
        tree(branchLen - sub_len, t)

        t.right(angle)

        t.up()
        t.backward(branchLen)
        t.down()


def main():
    t = turtle.Turtle()
    t.speed(0)
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(200)
    t.down()
    tree(75, t)
    myWin.exitonclick()


main()