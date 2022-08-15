"""
This program is about exception handling.
In Lab 02 we wrote a program for a hotdog stand to calculate total amount due from a customer.
We want to add exception handling to the program.  The hotdog stand sells hotdogs, potato chips and sodas.
Hotdogs are $2.50 each.  Potato chips are $1.50 per bag.  Sodas are $1.25 per can.
The program asks the user to enter number of hotdogs, chips and sodas ordered by the customer.
It calculates and displays the total amount due.  Numbers of hotdogs, chips and sodas entered should be integers.
If the user enters anything that cannot be converted to an integer, display an error message and set the number of that item to 0.
For example, if the user enters 3.5 hotdogs, display “Invalid input. Number of hotdogs must be an integer” and set number of hotdogs to 0.
Do not ask the user to reenter number of hotdogs.
"""

# for i in range(3):
#     wrong_val = True
#     while wrong_val:
#         try:
#             salary = float(input("Enter annual salary: "))
#             print(f'Salary {i + 1}: {salary}')
#             wrong_val = False
#         except ValueError:
#             print("Salary must be a numerical.")

try:
    hotdogs = int(input('Enter the number of hotdogs: '))
except ValueError:
    print('Invalid input: Number of hotdogs set to 0')
    hotdogs = 0

try:
    chips = int(input('Enter the number of potato chips: '))
except ValueError:
    print('Invalid input: Number of potato chips set to 0')
    chips = 0

try:
    sodas = int(input('Enter the number of sodas: '))
except ValueError:
    print('Invalid input: Number of sodas set to 0')
    sodas = 0

due = 2.5 * hotdogs + 1.5 * chips + 1.25 * sodas
print(f'Total amount due is ${due:,.2f}')
