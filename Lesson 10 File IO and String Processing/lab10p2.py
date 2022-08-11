"""
This program reads customer info from a text file and displays info to console window.
"""

# Creates text file to write
input_file = open('water_usage.txt', 'r')

# For each line, splits by space
for each_line in input_file:
    line_list = each_line.split()
    acc_number = int(line_list[0])
    customer_type = line_list[1]
    water = int(line_list[2])

    # Computes water charge
    if customer_type == 'R':
        if water <= 6000:
            water_charge = 0.005 * water
        else:
            water_charge = (0.005 * 6000) + 0.007 * (water - 6000)
    else:
        if water <= 8000:
            water_charge = 0.006 * water
        else:
            water_charge = (0.006 * 8000) + 0.008 * (water - 8000)

    # Prints to console window
    print(f'Account number: {acc_number} Water charge: ${water_charge:,.2f}')

input_file.close()
