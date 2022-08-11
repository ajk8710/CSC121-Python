"""
Instructors in a community college are paid on a schedule that provides a salary based on their number of years of teaching experience.
For each year of experience after the first year, up to 10 years, the instructor receives a 2% increase over the preceding value.
Suppose the initial salary of an instructor is $50,000.
In the second year, this instructor’s salary will be $51,000 ($50,000 + $50,000 * 0.02 = $51,000).
In the third year, the salary will be $52,020 ($51,000 + $51,000 * 0.02 = $52,020), and so on.
In addition, the instructor is required to deposit 5% of the salary each year into a retirement fund account.
For example, if the salary is $50,000 in a year, $2500 ($50,000 * 0.05) will be deposited into his/her retirement fund account.
Write a program to do the following.  Ask the user to enter the starting salary.
Calculate and display the salary each year in the first 10 years.
Also calculate and display a running total of the instructor’s retirement fund after each year.

Example:
Enter starting salary: 50000

Year: 1 Salary: 50000.0
Retirement Fund Total So Far: 2500.0

Year: 2 Salary: 51000.0
Retirement Fund Running Total: 5050.0
...
"""

salary = float(input('Enter starting salary: '))

fund = 0
year = 1
while year <= 10:
    fund += salary * 0.05
    print(f'Year {year} Salary: ${salary:,.2f}')
    print(f'Retirement Fund Total So Far: ${fund:,.2f}')
    print()
    salary += salary * 0.02
    year += 1
