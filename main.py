import math
import turtle


# Functions for basic shapes
def drawSquare(length, direction, color):
    _direction = str(direction)
    turtle.pendown()
    turtle.fillcolor(str(color))
    turtle.begin_fill()

    if _direction.lower() == "left":
        for i in range(4):
            turtle.left(90)
            turtle.forward(length)
    elif _direction.lower() == "right":
        for i in range(4):
            turtle.right(90)
            turtle.forward(length)
    else:
        print("Not a valid direction! Pick left or right. (" + color + " square")
        turtle.end_fill()
        turtle.penup()
        return

    turtle.end_fill()
    turtle.penup()
    print("Drew a square!")


def drawRectangle(length, height, direction, color):
    _direction = str(direction)
    turtle.pendown()
    turtle.fillcolor(str(color))
    turtle.begin_fill()

    if _direction.lower() == "left":
        for i in range(2):
            turtle.left(90)
            turtle.forward(length)
            turtle.left(90)
            turtle.forward(height)
    elif _direction.lower() == "right":
        for i in range(2):
            turtle.right(90)
            turtle.forward(length)
            turtle.right(90)
            turtle.forward(height)
    else:
        print("Not a valid direction! Pick left or right. (" + color + "rectangle)")
        turtle.end_fill()
        turtle.penup()
        return

    turtle.end_fill()
    turtle.penup()
    print("Drew a rectangle!")


def drawTriangleSQ(length, direction, color):
    _direction = str(direction)
    turtle.pendown()
    turtle.fillcolor(str(color))
    turtle.begin_fill()

    if _direction.lower() == "left":
        for i in range(2):
            turtle.left(90)
            turtle.forward(length)
        turtle.left(135)
        turtle.forward(length * math.sqrt(2))
    elif _direction.lower() == "right":
        for i in range(2):
            turtle.right(90)
            turtle.forward(length)
        turtle.right(135)
        turtle.forward(length * math.sqrt(2))
    else:
        print(
            "Not a valid direction! Pick left or right (" + color + " square triangle)"
        )
        turtle.end_fill()
        turtle.penup()
        return

    turtle.end_fill()
    turtle.penup()
    print("Drew a square triangle!")


def drawCircle(radius, direction, color):
    _direction = str(direction)
    turtle.pendown()
    turtle.fillcolor(str(color))
    turtle.begin_fill()

    steps = 120
    stepLength = 2 * math.pi * abs(radius) / steps
    turnAngle = 360 / steps

    if _direction.lower() == "left":
        for i in range(steps):
            turtle.forward(stepLength)
            turtle.left(turnAngle)
    elif _direction.lower() == "right":
        for i in range(steps):
            turtle.forward(stepLength)
            turtle.right(turnAngle)
    else:
        print("Not a valid direction! Pick left or right (" + color + " circle)")
        turtle.end_fill()
        turtle.penup()
        return

    turtle.end_fill()
    turtle.penup()
    print("Drew a circle!")


def drawLine(x1, y1, x2, y2):
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)
    turtle.penup()
