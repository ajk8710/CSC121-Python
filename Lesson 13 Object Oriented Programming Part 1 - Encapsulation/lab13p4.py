"""
Write a new version of the manage_course project you wrote in Problem 2.
Make a copy of the manage_course project folder and rename it to manage_course_new.
Make the following changes to class Course:
(a)	Change all instance variables to private
(b)	Write getter methods for course code, quota and enrollment
(c)	Write setter method for quota.  This method accepts new quota as an argument.
If new quota is negative, display “Quota cannot be negative”.
Otherwise, set quota to new quota and display “Quota changed”.  This method has no return value.
In the main module, you need to call getter methods to retrieve data stored in
instance variables of the course objects because they are private now.
In addition, add a choice of changing quota to the menu.
If this choice is chosen, ask the user to enter new quota and call the setter method of quota to set a new quota.
"""

from course_new import Course

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
        print(f'Enrollment: {c.get_enrollment()}')
    elif choice == '2':
        c.drop_student()
        print(f'Enrollment: {c.get_enrollment()}')
    elif choice == '3':
        print(f'Course Code: {c.get_course_code()}, Quota: {c.get_quota()}, Enrollment: {c.get_enrollment()}')
    elif choice == '4':
        try:
            quota = int(input('Enter new course quota: '))
            c.set_quota(quota)
        except ValueError:
            print('Please enter integer for course quota.')
