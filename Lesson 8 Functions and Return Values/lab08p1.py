"""
In Lab 07 we wrote a program to calculate energy bill for households.
We are going to rewrite that program with value returning functions.
Energy consumption is measured in kilowatt hours (kWh).
The more kWh a household use in a month, the higher the energy bill.
A power company charges customers $0.12 per kWh for the first 500 kWh.
After the first 500 kWh, the rate is $0.15 per kWh.  Write a program to calculate energy charge.
You must write and use the following functions.
(a)	A main function: Call the value returning function get_kWh_used.
Pass the return value to the value returning function bill_calculator as an argument.
Display the return value of bill_calculator.
(b)	A get_kWh_used function: This function has no parameter. It asks the user to enter number of kWh used.
Use an input validation loop to ensure that kWh used is not negative. Return kWh used.
(c)	A bill_calculator function: This function has a parameter to receive number of kWh used.
Calculate and return the energy charge.

Example:
Enter kilowatt hours used: 510
Please pay this amount: 61.5
"""


def main():
    kwh = get_kwh_used()
    bill = bill_calculator(kwh)
    print(f'Please pay this amount: ${bill:,.2f}')


def get_kwh_used():
    kwh = float(input('Enter the kwh used: '))
    while kwh < 0:
        print('kwh cannot be negative.')
        kwh = float(input('Enter the kwh used: '))
    return kwh


def bill_calculator(kwh):
    if kwh <= 500:
        return 0.12 * kwh
    else:
        return 60 + 0.15 * (kwh - 500)


main()
