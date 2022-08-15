"""
This problem is about modular design.
We are writing a program to simulate a self-checkout system of a store named Wake-Mart.
This program has four tasks at the top level: input prices of items, process discount, process promotion and process payment.
Processing of payment is further divided into two subtasks.  The customer can choose either to pay by cash or by debit card.
"""


def main():
    print('Welcome to the self-checkout system of Wake-mart')
    num_items, total_price = scan_prices()
    total_price = discount(num_items, total_price)
    num_items, total_price = promotion(num_items, total_price)
    makePayment(total_price)


def scan_prices():

    """ This function gets the price of each item purchased.
    The customer enters the prices one by one with a loop. When there are no more prices to enter, 0 is entered to exit the loop.
    Whenever a negative price is entered, display “Price cannot be negative” and ask the user to enter next price.
    Every time a valid price is entered, display the number of prices entered and the total so far (exclude invalid entries).
    Return the number of prices entered and the total price of all items when the user has finished entering prices. """

    num_items = 0
    price = 0.1
    total_price = 0

    while price != 0:
        try:
            price = float(input(f'Enter price of item #{num_items + 1} [or 0 to stop]: '))
            if price > 0:
                num_items += 1
                total_price += price
                print(f'Number of items: {num_items}, Total: ${total_price:,.2f}')
            elif price < 0:
                print('Price cannot be negative')
        except ValueError:
            print('Please enter valid price')

    return num_items, total_price


def discount(num_items, total_price):

    """ discount(count, total)	This function gives a 10% discount if 10 or more items are purchased.
    It receives items count and total as arguments.
    It checks whether 10 or more items are purchased, and reduces the total by 10% if the 10 or more items requirement is met.
    This function returns the total, either it has been changed or not. """

    if num_items >= 10:
        print("You've got 10% discount for buying 10 items of more.")
        total_price *= .9
        print(f'Number of items: {num_items}, Total: ${total_price:,.2f}')
    return total_price


def promotion(num_items, total_price):

    """ This function allows the user to buy a gift card with discount.
    It receives items count and total as arguments.
    If the total is $50 or higher, the user can choose to buy one $50 gift card for the price of $40.
    Update items count and total if the user chooses to buy gift card.
    This function returns items count and total, either they have been changed or not. """

    if total_price >= 50:
        gift = 'i'
        while gift not in {'Y', 'N'}:
            gift = input('Do you want to buy a $50 gift card for $40? [Y/N]: ')
            gift = gift.upper()
        if gift == 'Y':
            print('Thank you for buying a gift card.')
            num_items += 1
            total_price += 40
            print(f'Number of items: {num_items}, Total: ${total_price:,.2f}')
    return num_items, total_price


def makePayment(balance):

    """ This function allows the user to choose payment type [1 for cash, 2 for debit].
    It receives balance as argument, and pass it to pay_cash and pay_debit. """

    print('Payment options:')
    payment_type = '3'
    while payment_type not in {'1', '2'}:
        payment_type = input('Enter 1 for cash, 2 for debit: ')

    if payment_type == '1':
        pay_cash(balance)
    else:  # payment_type == '2'
        pay_debit(balance)


def pay_cash(balance):

    """ This function receives cash payment.  The self-checkout machine only accepts $10, $5 and $1 bills.
    Ask the user how many $10, $5 and $1 bills he is going to use.  Calculate and display total payment.
    If the total payment is lower than the balance, ask the user to reenter the numbers of $10,
    $5 and $1 bills until the total payment is not lower than the balance.
    If customer has paid more than the balance, calculate and display change. """

    print('This machine only accepts $10, $5 and $1 bills.')
    redo = True
    while redo:
        try:
            tens = int(input('How many $10 bills are you going to pay? '))
            fives = int(input('How many $5 bills are you going to pay? '))
            ones = int(input('How many $1 bills are you going to pay? '))
            payment_amount = tens * 10 + fives * 5 + ones
            if payment_amount < balance:
                print('Total cash payment less than balance. Please re-enter.')
            else:
                redo = False
        except ValueError:
            print('Please enter integers for number of bills.')

    print('Thank you for the payment.')
    print(f'Total cash paid: ${payment_amount:,.2f}')
    print(f'Change: ${(payment_amount - balance):,.2f}')


def pay_debit(balance):

    """ This function receives debit payment. It asks customer to enter a 16-digit card number and a 4-digit PIN.
    It also asks customer to enter payment amount. Use a validation loop to ensure that payment is not lower than the balance.
    If payment is lower than the balance, ask the user to reenter payment amount until it is not lower than the balance.
    If payment is higher than balance, calculate and display cash back amount. """

    card_num = '1'
    pin = '1'
    payment_amount = -1
    while len(card_num) != 16 or not card_num.isdigit():
        card_num = input('Please enter a 16-digit card number: ')
    while len(pin) != 4 or not pin.isdigit():
        pin = input('Please enter 4-digit pin: ')
    while payment_amount < balance:
        try:
            payment_amount = float(input('Please enter payment amount: '))
            if payment_amount < balance:
                print('Payment amount cannot be smaller than balance. Please re-enter.')
        except ValueError:
            print('Please enter numbers only for payment amount.')
    print('Thank you for your payment.')
    print(f'Cash back amount: ${payment_amount - balance:,.2f}')


main()
