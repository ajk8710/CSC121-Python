"""
This problem is about Python modules.
Crate a module currency, which includes the following three functions that do currency conversions:
to_euro(dollar): This function receives US Dollar as an argument and converts it to Euro.  1 US Dollar = 0.81 Euro.  Return Euro.
to_yen(dollar): This function receives US Dollar as an argument and converts it to Japanese Yen.  1 US Dollar = 106.45 Yen.  Return Yen.
to_peso(dollar): This function receives US Dollar as an argument and converts it to Mexican Peso.  1 US Dollar = 18.58 Peso.  Return Peso.
Store these three functions in a file named currency.py.
Create a file for the main module.  Name the file lab12P2.py.

Define a main function in the main module to do the following:
(1)	Ask the user to choose a foreign currency: Euro, Japanese Yen or Mexican Peso. Write a loop to validate user input.
If an invalid choice is made, display an error message and ask the user to choose a foreign currency again until the choice is valid.
(2)	Ask the user to enter US dollar amount. Write a loop to validate user input.
If the US dollar amount is negative, display an error message and ask the user to reenter it until it is non-negative.
(3)	Call one of the three functions in the currency module to convert US dollar to the foreign currency chosen by the user
(4)	Receive and display the converted foreign currency
"""

import currency

print('Converting US Dollar to a foreign currency.')
choice = input('Enter 1 for Euro, 2 for Japanese Yen, 3 for Mexican Peso: ')
while choice not in {'1', '2', '3'}:
    print('Invalid input')
    choice = input('Enter 1 for Euro, 2 for Japanese Yen, 3 for Mexican Peso: ')

redo = True
while redo:
    try:
        dollar = float(input('Enter US dollar amount: $'))
        while dollar < 0:
            print('US Dollar cannot be negative.')
            dollar = float(input('Enter US dollar amount'))
        redo = False
    except ValueError:
        print('Please enter numbers for US dollar amount.')

if choice == '1':
    converted = currency.to_euro(dollar)
    unit = 'euro'
elif choice == '2':
    converted = currency.to_yen(dollar)
    unit = 'yen'
else:  # currency == '3'
    converted = currency.to_peso(dollar)
    unit = 'peso'

print(f'US ${dollar:,.2f} converted to {converted:,.2f} {unit}.')
