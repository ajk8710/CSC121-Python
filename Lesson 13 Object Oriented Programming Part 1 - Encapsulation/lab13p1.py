"""
Add a file fly_drone_main.py to this project.  In this main module, create an instance of Drone.
Write a loop to control the speed and height of the drone.
In the loop, ask the user to enter 1 for acceleration, 2 for deceleration, 3 for ascending, 4 for descending, or 0 for exit.
Call the appropriate method of the Drone object to change the speed or height of the drone.
Every time the speed or height of the drone changes, display the speed and height.
"""

from drone import Drone

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
