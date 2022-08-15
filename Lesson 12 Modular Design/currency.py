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


def to_euro(dollar):
    dollar = float(dollar)
    return 0.81 * dollar


def to_yen(dollar):
    return 106.45 * dollar


def to_peso(dollar):
    return 18.58 * dollar
