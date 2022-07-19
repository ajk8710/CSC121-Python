"""
Diabetes is diagnosed by measuring patient’s fasting plasma glucose level (FPG).
If FPG is higher than 125, the patient has diabetes.
If FPG is higher than 100 but not higher than 125, the patient has pre-diabetes.
FPG 100 or lower is considered as a healthy level.
Write a program to do diabetes diagnosis for multiple patients.
For each patient, enter FPG and determine whether the patient has diabetes, pre-diabetes or a healthy FPG level.
Ask the user to answer a yes/no question to indicate whether he/she wants to do diagnosis for another patient.

Example:
Enter fasting plasma glucose level: 126
This patient has diabetes

Checking diabetes for another patient? [y/n] y
Enter fasting plasma glucose level: 97
This patient has healthy fpg level
"""

again = 'y'
while again == 'y':
    level = float(input('Enter fasting plasma glucose level: '))
    if level > 125:
        print('This patient has diabetes.')
    elif level > 100:
        print('This patient has pre-diabetes.')
    else:
        print('This patient has healthy fpg level.')
    again = input('Checking diabetes for another patient? [y/n]: ')
    again = again.lower()
