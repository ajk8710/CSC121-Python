"""
Write a Python program to do the following:
(a)	Ask the user to enter as many integers from 1 to 10 as he/she wants. Store the integers entered by the user in a list.
Every time after the user has entered an integer, use a yes/no type question to ask whether he/she wants to enter another one.
(b)	Display the list.
(c)	Calculate and display the average of the integers in the list.
(d)	If the average is higher than 7, subtract 1 from every number in the list.  Display the modified list.
"""

lst = []
again = 'y'

while again == 'y':

    x = 0
    while x not in range(1, 11):
        x = int(input('Enter an integer from 1 to 10: '))
    lst.append(x)

    again = 'i'
    while again not in ('y', 'n'):
        again = input('Enter another integer? [y/n] ')
        again = again.lower()

avg = sum(lst) / len(lst)
print('Number List:', lst)
print('Average:', avg)

if avg > 7:
    for i in range(len(lst)):
        lst[i] -= 1
    print('Modified Number List:', lst)
