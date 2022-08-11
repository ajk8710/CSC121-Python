"""
Rewrite your program in Problem 3.
This time if what is entered by the user cannot be converted to an integer,
display an error message and ask the user to reenter it until an integer is entered.
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
#             wrong_val = True


# Not really needed, but just to practice propagation of raised exceptions
# This function just do the same thing int() function would do
def string_to_int(string):
    try:
        return int(string)
    except ValueError:
        raise ValueError


wrong_val = True
while wrong_val:
    try:
        hotdogs = string_to_int(input('Enter the number of hotdogs: '))
        wrong_val = False
    except ValueError:
        print('Please enter an integer for the number of hotdogs.')

wrong_val = True
while wrong_val:
    try:
        chips = string_to_int(input('Enter the number of potato chips: '))
        wrong_val = False
    except ValueError:
        print('Please enter an integer for the number of potato chips.')

wrong_val = True
while wrong_val:
    try:
        sodas = string_to_int(input('Enter the number of sodas: '))
        wrong_val = False
    except ValueError:
        print('Please enter an integer for the number of sodas.')

due = 2.5 * hotdogs + 1.5 * chips + 1.25 * sodas
print(f'Total amount due is ${due:,.2f}')
