def determine_grade(student_mark):
    if student_mark >= 70:
        return 'A'
    elif student_mark >= 60:
        return 'B'
    elif student_mark >= 50:
        return 'C'
    elif student_mark >= 40:
        return 'D'
    elif student_mark >= 30:
        return 'E'
    elif student_mark >= 20:
        return 'F'

student_mark = float(input("Enter the mark you received: "))
print(determine_grade(student_mark))
