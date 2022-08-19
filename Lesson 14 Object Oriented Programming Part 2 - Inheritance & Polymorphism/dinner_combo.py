"""
A Chinese restaurant has two types of dinner combos for customers to choose.
A regular dinner combo includes main dish and soup. A deluxe dinner combo includes main dish, soup and appetizer.
There are three main dish choices: sweet and sour pork ($7), sesame chicken ($8) or shrimp fried rice ($9).
There are two soup choices: egg drop soup ($1.25) or wonton soup ($1.50).
There are two appetizer choices: spring roll ($1.25) or chicken wing ($1.50).
They need a program to place orders. Your Python project needs to follow these requirements:
(a)	Create a Dinner_combo class for regular dinner combos.
This class has three protected instance variables: main_dish, soup and total.
Define a choose_dish method to choose a main dish, a choose_soup method to choose a soup,
and a displayOrder method to display items ordered and total amount due.
(b)	Create a Deluxe_dinner_combo class for deluxe dinner combos.  This class is a derived class of the dinner_combo class.
It has one additional protected instance variables: appetizer.
Define a choose_appetizer method to choose an appetizer, and a displayOrder method to display items ordered and total amount due.
(c)	In the main module, ask user to choose either regular or deluxe dinner combo.
Create an object and call its methods to input food items and display information of the order.
"""


class DinnerCombo:
    def __init__(self):
        self._main_dish = None
        self._soup = None
        self._total = 0

    def choose_dish(self):
        choice = '0'
        while choice not in {'1', '2', '3'}:
            choice = input('Enter 1 for Sweet & Sour Pork [$7], 2 for Sesame Chicken [$8] or 3 for Shrimp Fired Rice [$9]: ')
        if choice == '1':
            self._main_dish = 'Sweet & Sour Pork'
            self._total += 7
        elif choice == '2':
            self._main_dish = 'Sesame Chicken'
            self._total += 8
        else:  # choice == '3'
            self._main_dish = 'Shrimp Fired Rice'
            self._total += 9

    def choose_soup(self):
        choice = '0'
        while choice not in {'1', '2'}:
            choice = input('Enter 1 for Egg Drop Soup [$1.25] or 2 for Wonton Soup [$1.50]: ')
        if choice == '1':
            self._soup = 'Egg Drop Soup'
            self._total += 1.25
        else:  # choice == '2'
            self._soup = 'Wonton Soup'
            self._total += 1.5

    def display_order(self):
        print(self)

    def __str__(self):
        return f'Items ordered: {self._main_dish}, {self._soup}\nTotal: ${self._total:,.2f}'
