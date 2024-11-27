def calculate_grade(marks):
    """Calculate the grade based on marks."""
    if marks >= 75:
        return 'A'
    elif marks >= 65:
        return 'B'
    elif marks >= 55:
        return 'C'
    elif marks >= 45:
        return 'D'
    else:
        return 'F'

def main():
    num_students = int(input("Enter the number of students: "))
    students_grades = {}

    for _ in range(num_students):
        student_name = input("Enter the name of the student: ")
        marks = []

        num_subjects = int(input(f"Enter the number of subjects for {student_name}: "))
        
        for j in range(num_subjects):
            mark = float(input(f"Enter marks for subject {j + 1}: "))
            marks.append(mark)

        # Calculate average marks
        average_marks = sum(marks) / num_subjects
        grade = calculate_grade(average_marks)

        # Store result
        students_grades[student_name] = {
            'average_marks': average_marks,
            'grade': grade
        }

    # Display results
    print("\nStudent Grades:")
    for student, info in students_grades.items():
        print(f"{student}: Average Marks = {info['average_marks']:.2f}, Grade = {info['grade']}")

if __name__ == "__main__":
    main()