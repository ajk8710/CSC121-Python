"""
This program asks customer info for 4 customers and writes to text file.
"""

# Creates text file to write
output_file = open('water_usage.txt', 'w')

# Running for 4 customers
for customer_count in range(4):
    acc_number = int(input('Enter account number: '))

    customer_type = input('Enter R for residential, B for business: ')
    customer_type = customer_type.upper()

    # Re-prompts for customer type if neither R or B is entered
    while customer_type != 'R' and customer_type != 'B':
        print('Wrong customer type')
        customer_type = input('Enter R for residential, B for business: ')
        customer_type = customer_type.upper()

    water = int(input('Enter number of gallons used: '))

    # Writes to text file
    output_file.write(str(acc_number) + ' ' + customer_type + ' ' + str(water) + '\n')

output_file.close()
