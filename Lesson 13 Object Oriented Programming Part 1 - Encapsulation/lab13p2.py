"""
Add a file manage_course_main.py to this project.  This is the main module.
Write code to ask the user to enter course code and quota of a course.
Use the data provided by the user to create an instance of Course.  Write a loop to manage this course.
In the loop, ask the user to enter 1 for adding a student, 2 for dropping a student, 3 for displaying course info, or 0 for exit.
If 1 is chosen, call the add_student method of the Course object and use a print statement to display updated enrollment.
If 2 is chosen, call the drop_student method of the Course object and use a print statement to display updated enrollment.
If 3 is chosen, display values stored in the Course object to show course code, quota and enrollment.
"""

from course import Course

course_code = input('Enter course code: ')

redo = True
while redo:
    try:
        quota = int(input('Enter course quota: '))
        if quota < 0:
            print('Course quota cannot be negative.')
        else:
            redo = False
    except ValueError:
        print('Please enter integer for course quota.')

c = Course(course_code, quota)

choice = '-1'
while choice != '0':
    choice = input('Enter 1 for adding a student, 2 for dropping a student, 3 for displaying course info, or 0 for exit: ')

    if choice == '1':
        c.add_student()
        print(f'Enrollment: {c.enrollment}')  # accessing public variable. May not be good practice. To be changed on next lab.
    elif choice == '2':
        c.drop_student()
        print(f'Enrollment: {c.enrollment}')
    elif choice == '3':
        print(f'Course Code: {c.course_code}, Quota: {c.quota}, Enrollment: {c.enrollment}')
