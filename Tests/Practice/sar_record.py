class DuplicateStudentIDError(Exception):
    pass

class StudentNotFoundError(Exception):
    pass

class Student:
    def __init__(self, id: int, name: str, age: int) -> any:
        self.id = id
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.id, self.name, self.age}"


class StudentRecordManager:
    def add_student(self, student: Student) -> None:
        student_info = {}
        with open("student_record.txt", "w") as file:
            file.write(student + "\n")

    def get_student(id: int) -> str:
        with open("student_record.txt", "r") as file:
            if str(id) in file.read():
                return f"ID: {id}"
            else:
                return "none"
        

manager = StudentRecordManager()

student1 = Student(3, "david", 20)

manager.add_student(str(student1))


print(StudentRecordManager.get_student(2))