"""
In the following program, a function average is defined to calculate the average of the elements of a list.
This function is called twice to calculate two averages.

def average (my_list) :
    avg = sum(my_list)/len(my_list)
    return avg

list1 = [2, 1, 5, 9, 8]
list1_avg = average(list1)
print("list1 average:", list1_avg)

list2 = [17, 5, 2, 4]
list2_avg = average(list2)
print("list2 average:", list2_avg)

Rewrite the program by replacing the definition of function average with a lambda function.
That means in your program there should be no function definition using the keyword def.

The following is the expected output.
list1 average: 5.0
list2 average: 7.0
"""

avg = lambda lst: sum(lst) / len(lst)

print("list1 average:", avg([2, 1, 5, 9, 8]))
print("list2 average:", avg([17, 5, 2, 4]))
