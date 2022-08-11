"""
A simple physics experiment is to drop a ball and see how high it bounces.
Once the “bounciness” of the ball has been determined, the ratio gives a bounciness index.
For example, if a ball dropped from a height of 10 feet bounces 6 feet high, the index is 0.6.
If the ball were to continue bouncing, the height it reaches in the second bounce would be 3.6 feet (6 feet * 0.6 = 3.6 feet).
Write a program that asks the user to enter the initial height of the ball,
the bounciness index and the number of times the ball is allowed to continue bouncing.
Display the height the ball reaches in each bounce.

Example:
Enter initial height: 8
Enter bounciness index: 0.5
Enter number of times the ball is allowed to bounce: 6
Number of bounces: 1 Height: 4.0
Number of bounces: 2 Height: 2.0
Number of bounces: 3 Height: 1.0
Number of bounces: 4 Height: 0.5
Number of bounces: 5 Height: 0.25
Number of bounces: 6 Height: 0.125
"""

height = float(input('Enter initial height: '))
bounce_index = float(input('Enter bounciness index: '))
bounce_limit = int(input('Enter number of times the ball is allowed to bounce: '))

count = 1
while count <= bounce_limit:
    height *= bounce_index
    print('Number of bounces:', count, 'Height:', height)
    count += 1
