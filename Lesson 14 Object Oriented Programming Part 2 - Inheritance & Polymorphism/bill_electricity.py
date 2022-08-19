"""
Write a program to create two types of utility bills: water bill and electricity bill.
Both types of bills have customer’s name and address. They calculate charge differently.
Your project must follow these requirements.
(a)	Create a Utility_bill class. This class has two protected instance variables: name and address.
The __init__ method takes customer’s name and address as two arguments and stores them in the instance variables.
Add another protected instance variable total and initialized it to 0.
Define two abstract methods calculate_charge and display_bill.
These abstract methods have no real code. There is only one statement to raise a NotImplementedError exception.
(b)	Create a Water_bill class. This class is a derived class of the Utility_bill class.
It has an additional protected instance variable to store number of gallons of water used.
Define a calculate_charge method, which asks the user to enter number of gallons of water used and uses it to calculate total charge.
Customers pay $0.005 per gallon for the first 6000 gallons, and $0.007 per gallon after the first 6000 gallons.
Define a display_bill method to display customer’s name, address, number of gallons of water used and total charge.
(c)	Create a Electricity_bill class. This class is a derived class of the Utility_bill class.
It has an additional protected instance variable to store kilowatt hours used.
Define a calculate_charge method, which asks the user to enter kilowatt hours used and uses it to calculate total charge.
Customers pay $0.12 per kWh for the first 500 kWh, and $0.15 per kwh after the first 500 kWh.
Define a display_bill method to display customer’s name, address, number of kWh used and total charge.
(d)	In the main module, ask user to enter name and address. Ask the user to choose either water bill or electricity bill.
Create an object and call its calculate_charge method to calculate total charge. Call the display_bill method to display the bill.
"""

from bill_utility import BillUtility


class BillElectricity(BillUtility):
    def __init__(self, name, address):
        super().__init__(name, address)
        self._kwh = 0

    def calculate_charge(self):
        redo = True
        while redo:
            try:
                kwh = float(input('How many kwh of electricity were used? '))
                if kwh < 0:
                    print('Kwh cannot be less than 0.')
                else:
                    if kwh <= 500:
                        self._total = 0.12 * kwh
                    else:
                        self._total = 60 + 0.15 * (kwh - 500)
                    self._kwh = kwh
                    redo = False
            except ValueError:
                print('Please enter numbers for kwh of electricity.')

    def display_bill(self):
        print(f'Electricity Bill\nName: {self._name}\nAddress: {self._address}\n' +
              f'Kwh Used: {self._kwh}\nPlease pay this amount: ${self._total:,.2f}')
