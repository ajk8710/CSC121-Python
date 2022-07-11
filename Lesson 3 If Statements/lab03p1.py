"""
Write a program to calculate the number of seconds since midnight.
For example, suppose the time is 1:02:05 AM.
Since there are 3600 seconds per hour and 60 seconds per minutes,
it has been 3725 seconds since midnight (3600 * 1 + 2 * 60 + 5 = 3725).
The program asks the user to enter 4 pieces of information: hour, minute, second, and AM/PM.
The program will calculate and display the number of seconds since midnight.
[Hint: be very careful when the hour is 12].
[Example: 1:2:5am is 3725 sec, 11:58:59pm is 86339 sec]
[12:7:20am is 440 sec, 12:14:57pm is 44097 sec]
"""

hour = int(input('Enter hour: '))
minute = int(input('Enter minute: '))
second = int(input('Enter second: '))
ampm = input('Enter AM or PM: ')

if hour != 12:
    sec_since_midnight = 3600 * hour + 60 * minute + second
else:
    sec_since_midnight = 60 * minute + second

if ampm in ('pm', 'PM'):
    sec_since_midnight += 3600 * 12

print('Seconds since midnight:', sec_since_midnight)
