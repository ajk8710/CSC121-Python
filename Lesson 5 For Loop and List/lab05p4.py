"""
Write a Python program to do the following:
(a)	Use a for loop and a random integer generator to generate 5 random integers in 1 to 9.
Store the random integers in a list.  Display the list.
(b)	Use a for loop and a random integer generator to generate 5 random integers in 2 to 8.
Store the random integers in a second list.  Display the second list.
(c)	Use a for loop to compare elements in the two lists in pairs,
i.e., compare the first elements in both lists, compare the second elements in the both lists, etc.
Display the larger number in each comparison.
"""

import random

lst1 = []
for i in range(5):
    lst1.append(random.randint(1, 9))
print(lst1)

lst2 = []
for i in range(5):
    lst2.append(random.randint(2, 8))
print(lst2)

lst3 = []
for i in range(5):
    if lst1[i] >= lst2[i]:
        lst3.append(lst1[i])
    else:
        lst3.append(lst2[i])
print(lst3)
