class DuplicateStudentIDError(Exception):
    pass

class StudentNotFoundError(Exception):
    pass

class Student:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student ID: {self.id}, Name: {self.name}, Age: {self.age}"

class StudentRecordManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def add_student(self, student):
        students = self.retrieve_students()
        for existing_student in students:
            if existing_student.id == student.id:
                raise DuplicateStudentIDError(f"Student ID {student.id} already exists.")
        
        with open(self.file_path, "a") as file:
            file.write(f"{student.id},{student.name},{student.age}\n")

    def retrieve_students(self):
        students = []
        try:
            with open(self.file_path, "r") as file:
                for line in file:
                    student_data = line.strip().split(",")
                    student_id, student_name, student_age = map(int, student_data)
                    students.append(Student(student_id, student_name, student_age))
        except FileNotFoundError:
            # Return an empty list if the file does not exist yet
            pass
        return students

    def update_student(self, student):
        updated_students = []
        with open(self.file_path, "r") as file:
            for line in file:
                student_data = line.strip().split(",")
                student_id = int(student_data[0])
                if student_id == student.id:
                    updated_students.append(f"{student.id},{student.name},{student.age}\n")
                else:
                    updated_students.append(line)
        
        with open(self.file_path, "w") as file:
            file.writelines(updated_students)

    def get_student_by_id(self, student_id):
        students = self.retrieve_students()
        for student in students:
            if student.id == student_id:
                return student
        raise StudentNotFoundError(f"Student ID {student_id} not found.")


# Test the implementation
if __name__ == "__main__":
    # Creating a sample file with student records
    sample_records = [
        "1,John,20\n",
        "2,Jane,22\n",
        "3,Bob,21\n"
    ]

    with open("student_records.txt", "w") as file:
        file.writelines(sample_records)

    # Initializing the StudentRecordManager with the file path
    record_manager = StudentRecordManager("student_records.txt")

    # Adding new students
    new_student1 = Student(4, "Alice", 19)
    record_manager.add_student(new_student1)

    # Retrieving student records
    all_students = record_manager.retrieve_students()
    for student in all_students:
        print(student)

    # Updating existing student record
    existing_student = record_manager.get_student_by_id(3)
    existing_student.name = "Robert"
    record_manager.update_student(existing_student)

    # Retrieving student records after update
    all_students_after_update = record_manager.retrieve_students()
    for student in all_students_after_update:
        print(student)
