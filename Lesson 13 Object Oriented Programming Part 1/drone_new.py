"""
This is new drone with instance variables being private
"""


class Drone:
    def __init__(self):
        self.__speed = 0.0
        self.__height = 0.0

    def accelerate(self):
        self.__speed += 10

    def decelerate(self):
        self.__speed -= 10
        if self.__speed < 0:
            self.__speed = 0

    def ascent(self):
        self.__height += 10

    def descent(self):
        self.__height -= 10
        if self.__height < 0:
            self.__height = 0

    def __str__(self):
        return f'Speed: {self.__speed}, Height: {self.__height}'
