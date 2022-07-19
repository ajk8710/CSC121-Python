"""
(a)	Use the range function to generate this sequence of integers: 5, 9, 13, 17 and 21. Save the numbers in a list. Display the list.
(b)	Use a for loop to display each element in a separate line.
(c)	Use the range function to generate this sequence of integers: 26, 19, 12 and 5. Save the numbers in a list. Display the list.
(d)	Use a for loop to calculate the total of the elements in the second list.  Display the total.
"""

lst1 = list(range(5, 22, 4))
print('First list:', lst1)

print('Elements in the first list:')
for i in range(len(lst1)):
    print(lst1[i])

lst2 = list(range(26, 4, -7))
print('Second list:', lst2)
print('Total of the elements in the second list:', sum(lst2))
