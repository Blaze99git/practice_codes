"""
3. Grade Calculator
Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).
"""
def grade_calculator(score):
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
score = int(input("Enter the student's score: "))
grade = grade_calculator(score)
print(f'Score: {score}, Grade: {grade}')