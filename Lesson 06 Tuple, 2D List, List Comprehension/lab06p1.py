"""
A teacher wants a program to give extra points to students who fail a test. Write a Python program to do the following:
(a)	Ask the user to enter 5 test scores.  Store the scores in a list. Display the list.
(b)	Copy all 5 test scores to another list.  Use a loop to examine each test score in the new list.
If the score is below 60, add 10 extra points to the score. Display the list.
(c)	Compare the old score and new score of each student.  If the old score and new score are different, display the two scores.

Example:
Enter a test score: 45
Enter a test score: 77
Enter a test score: 88
Enter a test score: 52
Enter a test score: 90
All scores: [45.0, 77.0, 88.0, 52.0, 90.0]
Students who scored below 60 get 10 extra points.
All scores: [55.0, 77.0, 88.0, 62.0, 90.0]
Students whose scores have changed:
Old score: 45.0 New score: 55.0
Old score: 52.0 New score: 62.0
"""

scores = []
for i in range(5):
    score = float(input('Enter a test score: '))
    scores.append(score)

print('All scores:', scores)

scores_modified = scores[:]
for i in range(5):
    if scores_modified[i] < 60:
        scores_modified[i] += 10

print('Students who scored below 60 get 10 extra points.')
print('All scores:', scores_modified)

for i in range(5):
    if scores[i] != scores_modified[i]:
        print('Old score:', scores[i], 'New score:', scores_modified[i])
