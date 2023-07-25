import csv

class DuplicateStudentIDError(Exception):
    pass

class StudentNotFoundError(Exception):
    pass

class Student:
    def __init__(self, student_id, name, age):
        self.id = student_id
        self.name = name
        self.age = age

class StudentRecordManager:
    def __init__(self, file_path="student_records.txt"):
        self.file_path = file_path

    def _read_records(self):
        records = {}
        try:
            with open(self.file_path, "r", newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    student_id, name, age = map(str.strip, row)
                    records[int(student_id)] = Student(int(student_id), name, int(age))
        except FileNotFoundError:
            # If the file doesn't exist, return an empty dictionary
            return {}
        return records

    def _write_records(self, records):
        with open(self.file_path, "w", newline="") as file:
            writer = csv.writer(file)
            for student in records.values():
                writer.writerow([student.id, student.name, student.age])

    def add_student(self, student):
        records = self._read_records()
        if student.id in records:
            raise DuplicateStudentIDError(f"Student with ID {student.id} already exists.")
        records[student.id] = student
        self._write_records(records)

    def get_student(self, student_id):
        records = self._read_records()
        if student_id not in records:
            raise StudentNotFoundError(f"Student with ID {student_id} not found.")
        return records[student_id]

    def update_student(self, student):
        records = self._read_records()
        if student.id not in records:
            raise StudentNotFoundError(f"Student with ID {student.id} not found.")
        records[student.id] = student
        self._write_records(records)

if __name__ == "__main__":
    try:
        # Sample usage
        manager = StudentRecordManager()

        # Adding a new student
        student1 = Student(1, "John Doe", 20)
        manager.add_student(student1)

        # Retrieving a student
        student2 = manager.get_student(1)
        print(student2.name)  # Output: "John Doe"

        # Updating a student
        student2.age = 21
        manager.update_student(student2)

        # Retrieving the updated student
        student3 = manager.get_student(1)
        print(student3.age)  # Output: 21

        # Testing StudentNotFoundError
        manager.get_student(10)  # Raises StudentNotFoundError

        # Testing DuplicateStudentIDError
        student4 = Student(1, "Jane Smith", 22)
        manager.add_student(student4)  # Raises DuplicateStudentIDError
    except (StudentNotFoundError, DuplicateStudentIDError) as e:
        print(f"Error: {str(e)}")
