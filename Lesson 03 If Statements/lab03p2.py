"""
Write a program to do the opposite of Program 1.
Ask the user to enter the number of seconds since midnight.
Calculate and display the time, including hour, minute, second and AM/PM.
[Hint: Review truncating division and modulus operator in Lesson 02.
You probably need to use them.]
[Example: 3725 sec is 1:2:5am, 86339 sec is 11:58:59pm]
[440 sec is 12:7:20am, 44097 sec is 12:14:57pm]
"""

sec_since_mid = int(input('Enter number of seconds since midnight: '))
hour = 0
minute = 0
second = 0

if sec_since_mid >= 43200:
    ampm = 'PM'
else:
    ampm = 'AM'

hour = sec_since_mid // 3600
minute = sec_since_mid % 3600 // 60
second = sec_since_mid % 3600 % 60

if hour > 12:
    hour -= 12

print(f'{hour:02d}:{minute:02d}:{second:02d} {ampm}')
