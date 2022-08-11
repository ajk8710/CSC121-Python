"""
This program prompts user a string and displays the frequency of each letters in the string
"""

# Solving without using dictionary

# List of alphabet
list_alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
              'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

userString = input('Enter a string: ')
userString = userString.upper()

count = 0
for alphabet in list_alpha:  # for each alphabet
    for character in userString:  # for each char in string
        if alphabet == character:  # increment count if alphabet == char
            count += 1
    if count != 0:  # Prints if count is not 0
        print(alphabet, count)
    count = 0  # Resets count to 0 for next alphabet
