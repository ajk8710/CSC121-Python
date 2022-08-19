"""
Create a Python project manage_course.  Add a Python file course.py to this project.  Define a class Course in this file.
This class has three publicly accessible instance variables to store course code, quota and enrollment.
Define the following methods:
(a)	An __init__ method that accepts the course code and quota as arguments.
Write statements in __init__ to store them in instance variables.
Also create an instance variable to store enrollment and initialize it to 0.
(b)	An add_student method to increase enrollment by one and display “One student added” if the course is not full.
If the course is already full, make no change to enrollment and display “Course already full”.
This method has no argument other than self and has no return value.
(c)	A drop_student method to decrease enrollment by one and display “One student dropped” if the course is not empty.
If the course is empty, make no change to enrollment and display “Course is empty”.
This method has no argument other than self and has no return value.
"""


class Course:
    def __init__(self, course_code, quota):
        self.course_code = course_code
        self.quota = quota
        self.enrollment = 0

    def add_student(self):
        if self.enrollment < self.quota:
            self.enrollment += 1
            print('One student added.')
        else:
            print('Course already full.')

    def drop_student(self):
        if self.enrollment > 0:
            self.enrollment -= 1
            print('One student dropped')
        else:
            print('Course is empty')
