"""
Write a program to do the following.
Ask the customer to enter “S” for standard shipping or “E” for express shipping.
Also ask the user to enter the weight of the package in pounds.
Calculate and display shipping charge.

Weight ------------------ Standard rate per pound
4 pounds or less -------------------------- $1.05
Over 4 pounds but no more than 8 pounds --- $0.95
Over 8 pounds but no more than 15 pounds -- $0.85
Over 15 pounds ---------------------------- $0.80

Weight ------------------- Express rate per pound
2 pounds or less -------------------------- $3.25
Over 2 pounds but no more than 5 pounds --- $2.95
Over 5 pounds but no more than 10 pounds -- $2.75
Over 10 pounds ---------------------------- $2.55
"""

ship_type = input('Enter S for standard shipping, E for express [S/E]: ')
wt = float(input('Enter weight (lbs): '))

if ship_type in ('S', 's'):
    if wt <= 0:
        print('Please enter weight > 0')
    elif wt <= 4:
        charge = 1.05 * wt
    elif wt <= 8:
        charge = 0.95 * wt
    elif wt <= 15:
        charge = 0.85 * wt
    else:
        charge = 0.80 * wt
    if wt > 0:
        print(f'Shipping charge: ${charge:,.2f}')
elif ship_type in ('E', 'e'):
    if wt <= 0:
        print('Please enter weight > 0')
    elif wt <= 2:
        charge = 3.25 * wt
    elif wt <= 5:
        charge = 2.95 * wt
    elif wt <= 10:
        charge = 2.75 * wt
    else:
        charge = 2.55 * wt
    if wt > 0:
        print(f'Shipping charge: ${charge:,.2f}')
else:
    print('Please enter valid shipping type, S or E')
