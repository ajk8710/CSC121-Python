"""
The following program uses a loop to create a list of odd integers, whose range depends on user's choice:

start_num = int(input('Enter starting number: '))
end_num = int(input('Enter ending number: '))
my_list = []
for i in range(start_num, end_num + 1)
    if i % 2 == 1:
        my_list.append(i)
print('Odd numbers in the range:', my_list)

We can shorten the program by using generator expression.  Use one single statement to replace the last 5 lines.
You must use generator expression in that statement.
"""

start_num = int(input('Enter starting integer: '))
end_num = int(input('Enter ending integer: '))
print(list(n for n in range(start_num, end_num + 1) if n % 2 == 1))
