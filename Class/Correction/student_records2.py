class Student:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
    
    def format_data(self):
        return f'{self.id},{self.name},{self.age}\n'
    
    @classmethod
    def reformat_data(cls, data : str):
        data = data.strip('\n').split(',')
        id = int(data[0])
        name = data[1]
        age = int(data[2])
        return Student(id, name, age)

    def __str__(self):
        return f"Student ID: {self.id}, Name: {self.name}, Age: {self.age}"


class StudentRecordManager:
    def add_student(self, student: Student):
        with open('student_data.txt', 'a') as f:
            f.write(student.format_data())

    def get_student(self, id):
        with open('student_data.txt', 'r') as f:
            for student_data in f:
                student = Student.reformat_data(student_data)
                if student.id == id:
                    return student
        return None

    def update_student(self, data: Student):
        found = False
        updated_students = []
        
        with open('student_data.txt', 'r') as f:
            for student_data in f:
                student = Student.reformat_data(student_data)
                if student.id == data.id:
                    updated_students.append(data.format_data())
                    found = True
                else:
                    updated_students.append(student_data)
        
        if not found:
            return "Could not find student"
        
        with open('student_data.txt', 'w') as f: 
            f.writelines(updated_students)

        return "Student record updated successfully"


# Test the implementation
def main():
    
    manager = StudentRecordManager()
    
    # Adding students
    student1 = Student(1, 'John Mark', 20)
    manager.add_student(student1)
    
    student2 = Student(2, 'James Philip', 23)
    manager.add_student(student2)

    student3 = Student(3, "Paul Frank", 19)
    manager.add_student(student3)

    # Retrieving student records
    student_id = 3
    retrieved_student = manager.get_student(student_id)
    if retrieved_student:
        print("Retrieved student record:")
        print(retrieved_student)
    else:
        print("Could not find student with ID:", student_id)

    print()

    # Updating a student record
    updated_student = Student(2, 'James Smith', 24)
    result = manager.update_student(updated_student)
    print(result)

    print()

    # Retrieving the updated student record
    student_id = 2
    retrieved_student = manager.get_student(student_id)
    if retrieved_student:
        print("Retrieved updated student record:")
        print(retrieved_student)
    else:
        print("Could not find student with ID:", student_id)

main()