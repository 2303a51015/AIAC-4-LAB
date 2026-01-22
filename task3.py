'''
90 to 100 
display grade as 'A'
80 to 89
display grade as 'B'
70 to 79
display grade as 'C'
60 to 69
display grade as 'D'
Below 60
display grade as 'F'
'''

def determine_grade(score):
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    elif 0 <= score < 60:
        return 'F'
    else:
        return 'Invalid score'
# Example usage
score = 85
grade = determine_grade(score)
print(f"The grade for the score {score} is: {grade}")
# Example usage
score = 43
grade = determine_grade(score)
print(f"The grade for the score {score} is: {grade}")
    