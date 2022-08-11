"""
Admission to an aquarium is $14 per person.
There is also an IMAX theatre in the building, which charges $8 per ticket for a 3D shark show.
Customers have three choices:
    admission to the aquarium only without watching 3D show,
    watch 3D show only with no admission to the aquarium,
    or do both with a 25% discount.
Design a program for group orders.
Ask the group to enter number of people who want admission only but no 3D show,
number of people who want 3D show only but no admission to the aquarium,
and number of people who want both.
Calculate and display the total amount due from the group.
"""

aquarium_price = 14
imax_price = 8
discount_combo = .25

aquarium_only = int(input('Enter the number of people for aquarium only: '))
imax_only = int(input('Enter the number of people for imax only: '))
both = int(input('Enter the number of people for both aquarium and imax: '))

# backslash to continue to line, or you can use parenthesis
due = aquarium_price * aquarium_only + imax_price * imax_only \
      + (aquarium_price + imax_price) * both * (1 - discount_combo)

print(f'Total amount due is ${due:.2f}.')
