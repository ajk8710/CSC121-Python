"""
Residential and business customers are paying different rates for water usage.
Residential customers pay $0.005 per gallon for the first 6000 gallons.
If the usage is more than 6000 gallons, the rate will be $0.007 per gallon after the first 6000 gallons.
Business customers pay $0.006 per gallon for the first 8000 gallons.
If the usage is more than 8000 gallons, the rate will be $0.008 per gallon after the first 8000 gallons.
For example, a residential customer who has used 9000 gallons will pay $30 for the first 6000 gallons ($0.005 * 6000),
plus $21 for the other 3000 gallons ($0.007 * 3000). The total bill will be $51.
A business customer who has used 9000 gallons will pay $48 for the first 8000 gallons ($0.006 * 8000),
plus $8 for the other 1000 gallons ($0.008 * 1000). The total bill will be $56.
Write a program to do the following.
Ask the user which type the customer it is and how many gallons of water have been used.
Calculate and display the bill.
"""

customer_type = input('Enter R for residential customer or B for business customer [R/B]: ')

if customer_type not in ('R', 'r', 'B', 'b'):
    print('Please enter valid customer type [R/B]')
elif customer_type in ('R', 'r'):
    usage = float(input('How many gallons of water were used? '))
    if usage < 0:
        print('Please enter water usage >= 0')
    elif usage <= 6000:
        charge = 0.005 * usage
        print(f'Please pay this amount ${charge:,.2f}')
    else:
        charge = 0.005 * 6000 + 0.007 * (usage - 6000)
        print(f'Please pay this amount ${charge:,.2f}')
elif customer_type in ('B', 'b'):
    usage = float(input('How many gallons of water were used? '))
    if usage < 0:
        print('Please enter water usage >= 0')
    elif usage <= 8000:
        charge = 0.006 * usage
        print(f'Please pay this amount: ${charge:,.2f}')
    else:
        charge = 0.006 * 8000 + 0.008 * (usage - 8000)
        print(f'Please pay this amount: ${charge:,.2f}')
