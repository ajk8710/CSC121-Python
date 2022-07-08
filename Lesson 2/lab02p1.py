"""
A hotdog stand sells hotdogs, potato chips and sodas.
Hotdogs are $2.50 each.  Potato chips are $1.50 per bag.  Sodas are $1.25 per cans.
Design a program to do the following.
Ask the user to enter number of hotdogs, chips and sodas ordered by the customer.
The program will calculate and display the total amount due.
"""

hotdogs = int(input('Enter the number of hotdogs: '))
chips = int(input('Enter the number of potato chips: '))
sodas = int(input('Enter the number of sodas: '))
due = 2.5 * hotdogs + 1.5 * chips + 1.25 * sodas
print('Total amount due is $', due, sep='')
# print(f'Total amount due is ${due}')
