"""
This program is about list comprehension.  We are going to use list comprehension to generate sequences of powers.

(a)	Use list comprehension to generate the first, second, third and fourth powers of 2.
Store the results in a list.  The first power of 2 is 21 = 2. The second power of 2 is 22 = 4.
The third power of 2 is 23 = 8. The fourth power of 2 is 24 = 16.  Our goal is to generate the following list:

[2^1, 2^2, 2^3, 2^4]

which equals

[2, 4, 8, 16]

In Python, we use n**p to calculate the pth power of n. For example, 2**1 is 2^1, 2**2, is 2^2, 2**3 is 2^3, and 2**4 is 2^4.

You need an input sequence when you use list comprehension to generate the list of powers of 2.
You are required to use a range function to create the input sequence. Display the list of powers of 2 after it is generated.

(b)	Use list comprehension to generate the first, second, third and fourth power of 3.
Store the result in a list.  The first power of 3 is 31 = 3. The second power of 3 is 32 = 9.
The third power of 3 is 33 = 27. The fourth power of 3 is 34 = 81.  Our goal is to generate the following list:

[3^1, 3^2, 3^3, 3^4]

which equals

[3, 9, 27, 81]

You need an input sequence when you use list comprehension to generate the list of powers of 3.
You are required to use a range function to create the input sequence. Display the list of powers of 3 after it is generated.

(c)	In mathematics, a matrix is a rectangular array of values arranged in rows and columns.
In Python, we can store a matrix in a list of lists.  Each list in the list of lists is a row of the matrix.
For example, the list of lists [ [2, 4, 8, 16], [3, 9, 27, 81] ] represents a matrix of two rows and four columns.
The list [2, 4, 8, 16] is the first row, while the list [3, 9, 27, 81] is the second row.

Use nested list comprehension to generate the following list of lists:

[ [2, 4, 8, 16],
  [3, 9, 27, 81],
  [4, 16, 64, 256],
  [5, 25, 125, 625],
  [6, 36, 216, 1296] ]

The first row is a list of powers of 2. The second row is a list of powers of 3. The third row is a list of powers of 4.
The fourth row is a list of powers of 5. The fifth row is a list of powers of 6.

You need two input sequences when you use nested list comprehension to generate the lists of powers shown above.
You are required to use two range functions to create the two input sequences. Display the list of lists after it is generated.
There is no need to display each row in a separate line.  Just use one print statement to display everything.

The following is the expected output.

Powers of 2: [2, 4, 8, 16]
Powers of 3: [3, 9, 27, 81]
Matrix: [[2, 4, 8, 16], [3, 9, 27, 81], [4, 16, 64, 256], [5, 25, 125, 625], [6, 36, 216, 1296]]
"""

powers_of_2 = [2**i for i in range(1, 5)]
print('Powers of 2:', powers_of_2)

powers_of_3 = [3**i for i in range(1, 5)]
print('Powers of 3:', powers_of_3)

matrix = [[x**i for i in range(1, 5)] for x in range(2, 7)]
print('Matrix:', matrix)
