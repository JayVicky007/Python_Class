class Student:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def format_data(self):
        return f'{self.id} {self.name} {self.age}'
    
    def reformat_data(self):
        data = data.strip("\n").split(",")
        

class StudentRecordManager:
    def add_student(self, student: Student):
        with open("student_data.txt", "a") as f:
            f.write(student.format_data())

    def get_student(self, id):
        with open("student_data.txt", "r") as f:
            if len(f.readlines) == 0:
                return "No student in file"
            for student in f.readlines():
                if str(id) == student.split(",")[0]:
                    return student
                else:
                    return "Could not find student"

    def update_student(self, id):
        with open("student_data.txt", "r") as f:
            if len(f.readlines) == 0:
                return "No student in file"
            updates = []
            for student in f.readlines():
                if str(student.id) == student.split(",")[0]:
                    updates.append(student.format_data())
                else:
                    updates.append(student)

            f.writelines(updates)

manager = StudentRecordManager()

student1 = Student(1, "John Doe", 20)
student2 = Student(2, "Jane Dow", 18)

# manager.add_student(student2)

