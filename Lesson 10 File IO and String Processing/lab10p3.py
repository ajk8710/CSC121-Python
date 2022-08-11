"""
This program prompts user time in format of Hr:Min:Sec and displays time without ':' or error message if input is incorrect.
"""

time = input('Enter time [hh:mm:ss]: ')

if time.count(':') != 2:
    print('Must separate hour, minute and second with two colons.')
else:
    # Splits each item by ':' and save as list
    time_list = time.split(':')

    # If length of an element is not 2 or not digit, print error message
    if len(time_list[0]) != 2 or not time_list[0].isdigit():
        print('Hour must be a 2-digit number.')
    elif len(time_list[1]) != 2 or not time_list[1].isdigit():
        print('Minute must be a 2-digit number.')
    elif len(time_list[2]) != 2 or not time_list[2].isdigit():
        print('Second must be a 2-digit number.')

    # If hour, minute, second are out of boundary, prints error message
    elif int(time_list[0]) < 0 or int(time_list[0]) > 23:
        print('Hour must be a 2-digit number between 0 and 23.')
    elif int(time_list[1]) < 0 or int(time_list[1]) > 59:
        print('Minute must be a 2-digit number between 0 and 59.')
    elif int(time_list[2]) < 0 or int(time_list[2]) > 59:
        print('Second must be a 2-digit number between 0 and 59.')

    # Otherwise (no errors) prints times with ':' removed
    else:
        print('Time with colons removed:', time.replace(':', ''))
