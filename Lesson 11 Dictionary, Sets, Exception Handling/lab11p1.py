"""
This program is about dictionaries.  We want to use a dictionary to store frequency count of each letter in a string.
Write a Python program to do the following:
(a)	Ask the user to enter a string.  Convert all letters to uppercase.
Count the frequency of each letter in the string. Store the frequency counts in a dictionary.
You should count letters only.  Do not count any other characters such as digits and space.  Display the dictionary.
(b)	Ask the user to enter a letter.  Convert it to uppercase.  Check whether the letter is in the dictionary.
If it is not, display the message “Letter not in dictionary”. Otherwise, display the frequency count of that letter,
remove the letter from the dictionary and display the dictionary after that letter has been removed.
(c) Create a list to store the letters that are in the dictionary.  Sort and display the list.
"""

diction = {}

string = input('Enter a String: ')
string = string.upper()

for char in string:
    if char.isalpha():
        if char in diction:
            diction[char] += 1
        else:
            diction[char] = 1

print(diction)

letter = input('Enter a letter: ')
letter = letter.upper()

if letter in diction:
    print(f'Frequency of letter {letter}: {diction[letter]}')
    del diction[letter]
    print('Letter removed')
    print(diction)
else:
    print('Letter not in dictionary')

lst = list(diction.keys())
lst.sort()
print('Letters sorted:', lst)
