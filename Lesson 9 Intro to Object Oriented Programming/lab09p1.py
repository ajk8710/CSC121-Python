"""
Write a Python program that uses Turtle Graphics to draw the letter “E” with four lines.
Decide the size and the location of the letter yourself.
"""

import turtle

turtle.setup(800, 600)
t = turtle.Turtle()

t.penup()
t.setposition(-100, 100)
t.pendown()
t.forward(200)

t.penup()
t.setposition(-100, -100)
t.pendown()
t.forward(200)

t.penup()
t.setposition(-100, 0)
t.pendown()
t.forward(200)

t.penup()
t.setposition(-100, 100)
t.pendown()
t.right(90)
t.forward(200)

t.hideturtle()
turtle.exitonclick()
