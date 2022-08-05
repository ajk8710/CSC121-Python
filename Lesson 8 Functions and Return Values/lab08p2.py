"""
In Lab 07 we wrote a program to calculate energy bill for residential and business customers.
We are going to rewrite that program with value returning functions.
Residential customers pay $0.12 per kWh for the first 500 kWh. After the first 500 kWh, the rate is $0.15 per kWh.
Business customers pay $0.16 per kWh for the first 800 kWh. After the first 800 kWh, the rate is $0.20 per kWh.
Write a program to calculate energy charge.
You must write and use the following functions.

(a)	A main function: Call the value returning function get_user_input, which returns kWh used and customer type.
Pass the return values to the value returning function bill_calculator as two arguments.
Display the return value of bill_calculator.

(b)	A get_user_input function: This function has no parameter.
It asks the user to enter number of kWh used. Use an input validation loop to ensure that kWh used is not negative.
Also ask the user to enter customer type (enter R for residential or B for business).  Convert lowercase letter to uppercase.
Use an input validation loop to ensure that customer is either R or B. Return kWh used and customer type.

(c)	A bill_calculator function: This function has two parameters to receive number of kWh used and customer type.
Calculate and return the energy charge.


Example:
Enter kilowatt hours used: 810
Enter R for residential customer, B for business customer: R
Please pay this amount: 106.5

Enter kilowatt hours used: 810
Enter R for residential customer, B for business customer: b
Please pay this amount: 130.0
"""


def main():
    kwh, customer_type = get_user_input()
    bill = bill_calculator(kwh, customer_type)
    print(f'Please pay this amount: ${bill:,.2f}')


def get_user_input():
    kwh = float(input('Enter the kwh used: '))
    while kwh < 0:
        print('kwh cannot be negative.')
        kwh = float(input('Enter the kwh used: '))

    customer_type = 'i'
    while customer_type not in {'R', 'B'}:
        customer_type = input('Enter R for residential customer, B for business customer [R/B]: ')
        customer_type = customer_type.upper()
    return kwh, customer_type


def bill_calculator(kwh, customer_type):
    if customer_type == 'R':
        if kwh <= 500:
            bill = 0.12 * kwh
        else:
            bill = 60 + 0.15 * (kwh - 500)
    else:
        if kwh <= 800:
            bill = 0.16 * kwh
        else:
            bill = 128 + 0.2 * (kwh - 800)
    return bill


main()
