"""
Students in a course need to do lab assignments and take tests.
Course grade is calculated from these scores.  Write a program to calculate course grade.
You must write and use the following two functions.

(a)	A main function: First, ask the user how many labs there are.
Use a loop to enter lab scores and store them in a list. Display the list of lab scores.
Second, ask the user how many tests there are. Use a loop to enter test scores and store them in another list. Display the list of test scores.
Third, tell the user that the default weights for labs and tests are 50 and 50.
If the user wants to use the default weights, enter D. Otherwise, enter C.
If the user chooses to use default weights,
call the grade_calculator function and pass the list of lab scores and the list of test scores as two arguments.
Do not pass any arguments about weights.
If the user chooses not to use default weights, ask the user to enter the weights for labs and tests, respectively.
Then call the grade_calculator function and pass the list of lab scores, the list of test scores,
lab weight and test weight as four arguments. You are free to use positional or keyword arguments.

(b)	A grade_calculator function:
This function has four parameters: lab score list, test score list, lab weight and test weight.
Use default parameter for lab weight and test weight. Default values are 50 and 50.
First, calculate and display average lab score. Second, calculate and display average test score.
Third, use average lab score, average test score, lab weight and test weight to calculate course grade.
Display course grade.

Example:
How many labs? 3
Enter a lab score: 93
Enter a lab score: 87
Enter a lab score: 90
Lab scores: [93.0, 87.0, 90.0]
How many tests? 2
Enter a test score: 85
Enter a test score: 75
Test scores: [85.0, 75.0]
The default weights for course grade are 50% labs and 50% tests.
Enter C to change the weights or D to use default weights: c
Enter lab percentage (without the % sign): 60
Enter test percentage (without the % sign): 40
Lab average: 90.0
Test average: 80.0
Course grade: 86.0
"""


def main():
    scores_lab = []
    num_lab = int(input('How many labs?: '))
    for i in range(1, num_lab + 1):
        scores_lab.append(float(input(f'Enter a lab score {i} of {num_lab}: ')))
    print(scores_lab)

    scores_test = []
    num_test = int(input('How many tests?: '))
    for i in range(1, num_test + 1):
        scores_test.append(float(input(f'Enter a test score {i} of {num_test}: ')))
    print(scores_test)

    print('The default weights for course grade are 50% labs and 50% tests.')
    weight = i
    while weight not in {'C', 'D'}:
        weight = input('Enter C to change the weights or D to use default weights [C/D]: ')
        weight = weight.upper()
    if weight == 'D':
        grade_calculator(scores_lab, scores_test)
    else:
        weight_lab = float(input('Enter lab percentage (without the % sign): '))
        weight_test = float(input('Enter test percentage (without the % sign): '))
        grade_calculator(scores_lab, scores_test, weight_lab, weight_test)


def grade_calculator(scores_lab, scores_test, weight_lab=50, weight_test=50):
    avg_lab = sum(scores_lab) / len(scores_lab)
    avg_test = sum(scores_test) / len(scores_test)
    course_grade = avg_lab * weight_lab / 100 + avg_test * weight_test / 100
    print('Lab Average:', avg_lab)
    print('Test Average:', avg_test)
    print('Course Grade:', course_grade)


main()
