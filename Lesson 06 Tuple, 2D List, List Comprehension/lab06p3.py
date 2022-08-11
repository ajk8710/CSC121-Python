"""
Three figure skaters, Jean, Kayla and Connie, compete in a meet.  Each skater receives 4 scores.
Write a program to do the following.
(a)	Ask the user to enter 4 scores for Jean. Store the scores in a list. Display the list.
(b)	Ask the user to enter 4 scores for Kayla. Store the scores in a list. Display the list.
(c)	Ask the user to enter 4 scores for Connie. Store the scores in a list. Display the list.
(d)	Create a list to store the three score lists.
This is a list of lists that contains three elements: Jean’s score list, Kayla’s score list, Connie’s score list.
Display this list of lists.
(e)	Use a set of nested for loops to add 1 extra point to every score of every skater in the list of lists created in part (d).
(f)	Display the modified list of lists. Each score should be 1 point higher than before.
(g)	For each skater in the list of lists, sort her 4 scores in ascending order.
(h)	Display the modified list of lists. Each skater’s 4 scores should be in ascending order.
"""

jean = []
kayla = []
connie = []

print("Please enter Jean's scores one by one.")
for i in range(1, 5):
    score = float(input(f'Enter Score #{i}: '))
    jean.append(score)
print("Jean's scores:", jean)
print()

print("Please enter Kayla's scores one by one.")
for i in range(1, 5):
    score = float(input(f'Enter Score #{i}: '))
    kayla.append(score)
print("Kayla's scores:", kayla)
print()

print("Please enter Connie's scores one by one.")
for i in range(1, 5):
    score = float(input(f'Enter Score #{i}: '))
    connie.append(score)
print("Connie's scores:", connie)
print()

all_scores = [jean, kayla, connie]
print('All scores:', all_scores)

for i in range(3):
    for j in range(4):
        all_scores[i][j] += 1
print('All scores after extra point:', all_scores)

for i in range(3):
    all_scores[i].sort()
print('All scores after sorting:', all_scores)
