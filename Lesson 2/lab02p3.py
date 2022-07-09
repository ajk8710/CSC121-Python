"""
Design a program to calculate sales tax,
tip and the total amount of a meal purchased at a restaurant.
The program asks the user to enter the charge for the food.
It will calculate and display the sales tax and tip.
Sales tax is 7% of the food charge.  Tip is 18% of the food charge.
Also calculate and display the total amount due from the customer.
"""

charge = float(input('Enter the charge for the food: '))

sales_tax = charge * 0.07
tip = charge * 0.18
due = charge + sales_tax + tip

print(f'Total amount due: ${due:.2f}')
# : introduces the format spec
# .2 sets the precision to 2
# f displays the number as a fixed-point notation (opposed to scientific notation)
