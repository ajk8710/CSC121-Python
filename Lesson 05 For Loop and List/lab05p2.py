"""
Write a program for course registration.  Students can use this program to add and drop courses.
There should be a loop in the program that tells the user to enter A to add course, D to drop course or E to exit.
If A is chosen, ask the user to enter the course to add.
If the user is already registered in that course, display the message “You are already registered in that course”;
otherwise, add the course to the user’s course list, display the message “Course added”, sort the list and display the list.
If the user chooses D, ask the user to enter the course to drop.
If the user is not registered in that course, display the message “You are not registered in that course”;
otherwise, remove the course from the user’s course list, display the message “Course dropped” and display the list.
The loop will stop when the user enters E.
"""

lst = []
options = ['A', 'D', 'E']

option = 'i'
while option != 'E':

    option = 'i'
    while option not in options:
        option = input('Enter A to add course, D to drop course, and E to exit: ')
        option = option.upper()

    if option == 'A':
        course = input('Enter course to add: ')
        if course in lst:
            print('You are already registered in that course')
        else:
            lst.append(course)
            lst.sort()
            print('Course added')
            print('Courses registered:', lst)

    elif option == 'D':
        course = input('Enter course to drop: ')
        if course not in lst:
            print('You are not registered in that course')
        else:
            lst.remove(course)
            print('Course dropped')
            print('Courses registered:', lst)
