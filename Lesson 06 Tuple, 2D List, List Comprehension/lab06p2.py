"""
Write a Python program to do the following:
(a)	Use a for loop and a random integer generator to generate 10 random integers in 1 through 15.
Store the random integers in a tuple.  Display the tuple.
[Hint: you may want to store the random integers in a list first and then convert the list to a tuple]
(b)	Create a new tuple.  Copy the first three elements of the tuple in part (a) to this tuple.  Display this tuple.
(c)	Create a new tuple.  Copy the last three elements of the tuple in part (a) to this tuple.  Display this tuple.
(d)	Concatenate the two tuples in part (b) and part (c).  Display the concatenated tuple.
(e)	Sort the concatenated tuple.  Display the sorted tuple.
"""

import random

lst = []
for i in range(10):
    lst.append(random.randint(1, 15))

tup1 = tuple(lst)
print('Tuple of 10 random numbers:', tup1)

tup2 = tup1[:3]
print('Tuple of first 3 numbers:', tup2)

tup3 = tup1[-3:]
print('Tuple of last 3 numbers:', tup3)

tup4 = tup2 + tup3
print('Two tuples concatenated:', tup4)

lst_to_sort = list(tup4)
lst_to_sort.sort()

tup5 = tuple(lst_to_sort)
print('Two tuples concatenated and sorted:', tup5)
