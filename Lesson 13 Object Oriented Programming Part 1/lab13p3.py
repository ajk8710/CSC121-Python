"""
Write a new version of the fly_drone project you wrote in Problem 1.
Make a copy of the fly_drone project folder and rename it to fly_drone_new. Make the following changes to class Drone:
(a)	Change all instance variables to private
(b)	Define a __str__ method to display the drone’s speed and height.
In the main module, you also need to modify the print statement
that displays the speed and height of the drone because those two attributes are private now.
"""

from drone_new import Drone

d = Drone()

choice = '-1'
while choice != '0':
    choice = input('Enter 1 for accelerate, 2 for decelerate, 3 for ascend, 4 for descend, 0 for exit: ')

    if choice == '1':
        d.accelerate()
    elif choice == '2':
        d.decelerate()
    elif choice == '3':
        d.ascent()
    elif choice == '4':
        d.descent()

    print(d)
