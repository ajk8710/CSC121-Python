"""
The jackpot of a lottery is paid in 20 annual installments.
There is also a cash option, which pays the winner 65% of the jackpot instantly.
In either case 30% of the winnings will be withheld for tax.
Design a program to do the following.
Ask the user to enter the jackpot amount.
Calculate and display how much money the winner will receive annually before tax
and after tax if annual installments is chosen.
Also calculate and display how much money the winner will receive instantly
before and after tax if cash option is chosen.
"""

num_annual = 20
instant_percent = .65
tax_rate = .30

amount = float(input('Enter the jackpot amount: '))

annual_amount = amount / 20
instant_amount = amount * instant_percent

annual_amount_after_tax = annual_amount * (1 - tax_rate)
instant_amount_after_tax = instant_amount * (1 - tax_rate)

print(f'Annual amount before tax is ${annual_amount:,.2f}, '
      f'and after tax is ${annual_amount_after_tax:,.2f} for 20 years.')

print(f'Instant amount before tax is ${instant_amount:,.2f}, '
      f'' f'and after tax is ${instant_amount_after_tax:,.2f}.')
