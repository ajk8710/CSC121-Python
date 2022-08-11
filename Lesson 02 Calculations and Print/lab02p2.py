"""
Each student in a course needs to submit 3 lab assignments and take 2 tests.
Design a program to do the following.
Ask the user to enter 3 lab scores and 2 test scores.
Calculate and display the lab average and the test average.
Also calculate and display the course grade,
which equals 55% of the lab average plus 45% of the test average.
"""

lab1 = float(input('Enter the 1st lab score: '))
lab2 = float(input('Enter the 2nd lab score: '))
lab3 = float(input('Enter the 3rd lab score: '))
test1 = float(input('Enter the 1st test score: '))
test2 = float(input('Enter the 2nd test score: '))

lab_avg = (lab1 + lab2 + lab3) / 3
test_avg = (test1 + test2) / 2
grade = 0.55 * lab_avg + 0.45 * test_avg

print('The lab average is', lab_avg)
print('The test average is', test_avg)
print('The course grade is', grade)
