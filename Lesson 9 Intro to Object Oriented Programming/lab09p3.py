"""
Write a Python program that uses Turtle Graphics to draw the letters “XYZ” with straight lines.
Decide the size and the location of the letter yourself.
"""

import turtle

# Creates pane
turtle.setup(800, 600)

# Creates turtle_x and hides turtle_x
turtle_x = turtle.Turtle()
turtle_x.pensize(5)
turtle_x.speed(3)
turtle_x.hideturtle()

# Draws one side of 'X'
turtle_x.penup()
turtle_x.setposition(-250, 50)
turtle_x.pendown()
turtle_x.setposition(-150, -50)

# Draws another side of 'X'
turtle_x.penup()
turtle_x.setposition(-150, 50)
turtle_x.pendown()
turtle_x.setposition(-250, -50)

# Creates turtle_y and hides turtle_y
turtle_y = turtle.Turtle()
turtle_y.pensize(5)
turtle_y.speed(3)
turtle_y.hideturtle()

# Draws the left side of 'Y'
turtle_y.penup()
turtle_y.setposition(-50, 50)
turtle_y.pendown()
turtle_y.setposition(0, 0)

# Draws the right side of 'Y'
turtle_y.penup()
turtle_y.setposition(50, 50)
turtle_y.pendown()
turtle_y.setposition(0, 0)

# Draws the bottom of 'Y'
turtle_y.right(90)
turtle_y.forward(50)

# Creates turtle_z and hides turtle_z
turtle_z = turtle.Turtle()
turtle_z.pensize(5)
turtle_z.speed(3)
turtle_z.hideturtle()

# Draws upper side of 'Z'
turtle_z.penup()
turtle_z.setposition(150, 50)
turtle_z.pendown()
turtle_z.forward(100)

# Draws middle and lower side 'Z'
turtle_z.setposition(150, -50)
turtle_z.forward(100)

turtle.exitonclick()
