"""
This is a practice file.
"""

# input_file = open('file0.txt', 'r')
# empty_str = ''
# line = input_file.readline()
# while line != empty_str:
#     print(line)
#     line = input_file.readline()
# input_file.close()

input_file = open('file0.txt', 'r')
for line in input_file:
    print(line.strip())

input_file = open('file0.txt', 'r')
lst = input_file.readlines()
print(lst)

for i in range(len(lst)):
    lst[i] = lst[i].strip()
print(lst)

input_file.close()
