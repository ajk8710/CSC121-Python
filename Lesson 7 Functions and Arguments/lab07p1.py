"""
Energy consumption is measured in units of kilowatt hours (kWh).
The more kWh a household use in a month, the higher the energy bill.
A power company charges customers $0.12 per kWh for the first 500 kWh.
After the first 500 kWh, the rate is $0.15 per kWh.  Write a program to calculate energy charge.
You must write and use the following two functions.
(a)	A main function: Ask the user to enter number of kWh used.
Call the bill_calculator function and pass number of kWh used to it as an argument.
(b)	A bill_calculator function: This function has a parameter to receive number of kWh used.
Calculate and display the energy charge.

Example:
Enter kilowatt hours used: 510
Please pay this amount: 61.5
"""


def main():
    kwh = float(input('Enter the kwh used: '))
    bill_calculator(kwh)


def bill_calculator(kwh):
    if kwh <= 500:
        charge = 0.12 * kwh
    else:
        charge = 60 + 0.15 * (kwh - 500)
    print(f'Please pay this amount: ${charge:,.2f}')


main()
