"""
Rewrite Program 2. (Copied below)
This is you must use keyword arguments to pass number of kWh and customer type to the bill_calculator function when it is called.

The energy company in Program 1 now uses different rates for residential and business customers.
Residential customers pay $0.12 per kWh for the first 500 kWh.  After the first 500 kWh, the rate is $0.15 per kWh.
Business customers pay $0.16 per kWh for the first 800 kWh.  After the first 800 kWh, the rate is $0.20 per kWh.
Write a program to calculate energy charge.  You must write and use the following two functions.
(a)	A main function: Ask the user to enter number of kWh used and customer type (enter R for residential or B for business).
Call the bill_calculator function and pass number of kWh used and customer type to it as arguments.
You must use positional arguments to pass kWh used and customer type.
(b)	A bill_calculator function: This function has two parameters to receive number of kWh used and customer type.
Calculate and display the energy charge.

Example:
Enter kilowatt hours used: 810
Enter R for residential customer, B for business customer: R
Please pay this amount: 106.5

Enter kilowatt hours used: 810
Enter R for residential customer, B for business customer: b
Please pay this amount: 130.0
"""


def main():
    kwh = float(input('Enter the kwh used: '))
    customer_type = 'i'
    while customer_type not in {'R', 'B'}:
        customer_type = input('Enter R for residential customer, B for business customer [R/B]: ')
        customer_type = customer_type.upper()
    bill_calculator(kwh=kwh, customer_type=customer_type)


def bill_calculator(customer_type, kwh):
    if customer_type == 'R':
        if kwh <= 500:
            charge = 0.12 * kwh
        else:
            charge = 60 + 0.15 * (kwh - 500)
    else:
        if kwh <= 800:
            charge = 0.16 * kwh
        else:
            charge = 128 + 0.2 * (kwh - 800)
    print(f'Please pay this amount: ${charge:,.2f}')


main()
