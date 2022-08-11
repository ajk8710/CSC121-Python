"""
Write a Python program that shows a turtle walking back and forth between two vertical walls.  Please do the following:
(a)	Create a 800 X 600 Turtle Graphics window
(b)	Draw a vertical line at x-coordinate = -300.  The y-coordinates of the two end points are 200 and -200, respectively.
(c)	Draw another vertical line at x-coordinate = 300.  The y-coordinates of the two end points are 200 and -200, respectively.
(d)	Create a turtle object and change the shape from arrowhead to turtle.
(e)	Use a loop to make the turtle walk 2000 steps.  Whenever the turtle hits a wall, it turns 180 degree and continues to walk.
"""

import turtle

# Creates pane
turtle.setup(800, 600)

# Creates wall object
wall = turtle.Turtle()
wall.pensize(5)
wall.speed(8)
wall.hideturtle()

# Draws the left side of wall
wall.penup()
wall.setposition(-300, 200)
wall.pendown()
wall.setposition(-300, -200)

# Draws the right side of wall
wall.penup()
wall.setposition(300, 200)
wall.pendown()
wall.setposition(300, -200)

# Creates turtle object
t = turtle.Turtle()
t.shape('turtle')
t.pensize(5)
t.penup()
t.speed(0)

# Makes turtle walk between walls
# Turtle turns when its head is about to hit the wall
for step in range(2000):
    t.forward(10)    # t.forward(1) will bottleneck turtle speed
    if t.xcor() == 280 or t.xcor() == -280:
        t.right(180)

turtle.exitonclick()
