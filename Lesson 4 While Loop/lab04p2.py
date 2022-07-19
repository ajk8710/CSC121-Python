"""
In Lab 03 we wrote a program to calculate the number of seconds since midnight.
Modify the program by adding error checking loops.  Hour must be a number from 1 to 12.
Minute and second must be numbers from 0 to 59. Also check whether “AM” or “PM” is entered.
Every time an invalid value is entered, display an error message and ask the user to re-enter a valid value immediately.
"""

hour = int(input('Enter hour: '))
while not (1 <= hour <= 12):
    print('Hour must be from 1 to 12.')
    hour = int(input('Enter hour: '))

minute = int(input('Enter minute: '))
while not (0 <= minute <= 59):
    print('Minute must be from 0 to 59.')
    minute = int(input('Enter minute: '))

second = int(input('Enter second: '))
while not (0 <= second <= 59):
    print('Second must be from 0 to 59.')
    second = int(input('Enter second: '))

ampm = input('Enter AM or PM: ')
while ampm not in ('am', 'AM', 'pm', 'PM'):
    print('Please enter AM or PM.')
    ampm = input('Enter AM or PM: ')

if hour != 12:
    sec_since_midnight = 3600 * hour + 60 * minute + second
else:
    sec_since_midnight = 60 * minute + second

if ampm in ('pm', 'PM'):
    sec_since_midnight += 3600 * 12

print('Seconds since midnight:', sec_since_midnight)
