class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    # Sort the student list based on CGPA in descending order
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

# Test the function with different input lists of students
if __name__ == "__main__":
    students1 = [
        Student("Alice", "A101", 3.75),
        Student("mano", "B102", 3.65),
        Student("varsha", "C103", 3.85),
    ]

    students2 = [
        Student("subiskha", "D104", 3.95),
        Student("suraj", "E105", 3.55),
        Student("ananth", "F106", 3.75),
    ]

    sorted_students1 = sort_students(students1)
    sorted_students2 = sort_students(students2)

    print("Sorted Students 1:")
    for student in sorted_students1:
        print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")

    print("\nSorted Students 2:")
    for student in sorted_students2:
        print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")