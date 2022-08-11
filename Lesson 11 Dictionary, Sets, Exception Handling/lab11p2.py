"""
This program is about sets.  Write a Python program to do the following:
(a)	Generate 5 random integers between 1 and 10, inclusive.  Store the random integers in a set named set1.
Display the set. Please note that the set may have less than 5 elements because some of the random integers generated may be redundant.
(b)	Generate 5 random integers between 1 and 10, inclusive.  Store the random integers in another set named set2.
Display the set. Please note that the set may have less than 5 elements because some of the random integers generated may be redundant.
(c) Find and display the union of set1 and set2.
(d) Use set comprehension to select odd numbers from the union and store them in a set.  Display this set.
(e)	Find and display the intersection of set1 and set2.
(f)	Find and display the symmetric difference of set1 and set2.
"""

from random import randint

set1 = set()
set2 = set()

for i in range(5):
    set1.add(randint(1, 10))
    set2.add(randint(1, 10))

print('Set 1:', set1)
print('Set 2:', set2)
print('Union:', set1 | set2)
print('Odd Numbers:', {num for num in set1 | set2 if num % 2 == 1})
print('Intersection:', set1 & set2)
print('Symmetric Difference:', set1 ^ set2)
