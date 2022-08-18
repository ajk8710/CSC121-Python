"""
Create a Python project fly_drone.  Add a Python file drone.py to this project.  Define a class Drone in this file.
This class has the following five methods:
(a)	__init__ : Create two public instance variables to store the speed and the height of the drone.
Initialize them to 0.0. This method has no parameters other than self and no return value.
(b)	accelerate : Increase the speed of the drone by 10.  The new speed cannot be negative.
This method has no parameters other than self and no return value.
(c)	decelerate : Decrease the speed of the drone by 10.  This method has no parameters other than self and no return value.
(d)	ascend : Increase the height of the drone by 10.  This method has no parameters other than self and no return value.
(e)	descend : Decrease the height of the drone by 10.  The new height cannot be negative.
This method has no parameters other than self and no return value.
"""


class Drone:
    def __init__(self):
        self.speed = 0.0
        self.height = 0.0

    def accelerate(self):
        self.speed += 10

    def decelerate(self):
        self.speed -= 10
        if self.speed < 0:
            self.speed = 0

    def ascent(self):
        self.height += 10

    def descent(self):
        self.height -= 10
        if self.height < 0:
            self.height = 0

    def __str__(self):
        return f'Speed: {self.speed}, Height: {self.height}'
