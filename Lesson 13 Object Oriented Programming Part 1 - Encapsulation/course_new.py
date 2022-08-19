"""
This is new course with instance variables being private
"""


class Course:
    def __init__(self, course_code, quota):
        self.__course_code = course_code
        self.__quota = quota
        self.__enrollment = 0

    def add_student(self):
        if self.__enrollment < self.__quota:
            self.__enrollment += 1
            print('One student added.')
        else:
            print('Course already full.')

    def drop_student(self):
        if self.__enrollment > 0:
            self.__enrollment -= 1
            print('One student dropped')
        else:
            print('Course is empty')

    def get_course_code(self):
        return self.__course_code

    def get_quota(self):
        return self.__quota

    def get_enrollment(self):
        return self.__enrollment

    def set_quota(self, quota):
        if quota < 0:
            print('Course quota cannot be negative.')
        else:
            self.__quota = quota
            print('Quota changed.')
