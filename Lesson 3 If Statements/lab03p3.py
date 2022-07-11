"""
Write a program to find the largest value.
Ask the user to enter three numbers.  Compare them and report the largest one.
[Hint: The user is free to enter any three numbers.  Some or all of them may be the same.
Take this into consideration when you compare the numbers.]
"""

num1 = float(input('Enter 1st number: '))
num2 = float(input('Enter 2nd number: '))
num3 = float(input('Enter 3rd number: '))

largest = num1

if largest < num2:
    largest = num2

if largest < num3:
    largest = num3

print(f'The largest number is {largest}.')
