import datetime
import mysql.connector as sql
from dotenv import load_dotenv
import os

load_dotenv()

user = os.environ.get('user')
password = os.environ.get('password')
host = os.environ.get('host')


class StudentNotFound(Exception):
    pass

class StudentAlreadyExists(Exception):
    pass

class Student:
    def __init__(self, id, first_name, last_name, phoneNumber):
        
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phoneNumber = phoneNumber
        self.is_present = False

    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class DB:
    def __init__(self):
        self.__db = sql.connect(
            host=host,
            user=user,
            password=password,
            database='attendancemanager'
        )
        self.studentT = 'student'
        self.presentT = 'present'
        self.__cursor = self.__db.cursor()

    # def mark_attendance(self, student: Student):
    #     self.__cursor.execute(f'INSERT INTO {self.presentT} (dates, studentID) VALUES (%s, %s)', (student.dates, student.studentID))
    #     self.__db.commit()

    # def mark_attendance(self, user, date):
    #     user.is_present = True
    #     user.attendance_record.append(date)

    def get_student_by_id(self, id):
        self.__cursor.execute(f'SELECT * FROM {self.studentT} WHERE id = "{id}"')
        student_data = self.__cursor.fetchone() # used to retrieve data from a single row
        if student_data:
            student_id, first_name, last_name, phone_number = student_data
            return Student(student_id, first_name, last_name, phone_number)
        else:
            return None

    def add_new_student(self, student: Student):
        self.__cursor.execute(f'INSERT INTO {self.studentT} (first_name, last_name, phone_number) VALUES (%s, %s, %s)', (student.first_name, student.last_name, student.phoneNumber))      
        self.__db.commit()
    
    def all_student(self):
        self.__cursor.execute(f'SELECT * FROM {self.studentT}')
        return self.__cursor.fetchall()
    
    def update_first_name(self, id, new_fname):
        self.__cursor.execute(f'UPDATE {self.studentT} SET first_name = "{new_fname}" WHERE id = "{id}"')
        self.__db.commit()

    def update_last_name(self, id, new_lname):
        self.__cursor.execute(f'UPDATE {self.studentT} SET last_name = "{new_lname}" WHERE id = "{id}"')
        self.__db.commit()

    def update_phone_number(self, id, new_phone_number):
        self.__cursor.execute(f'UPDATE {self.studentT} SET phone_number = "{new_phone_number}" WHERE id = "{id}"')
        self.__db.commit()



class AttendanceSystem:
    def __init__(self):
        self.db = DB()
        self.attendance_record = {}
        self.student_record = []

    def add_student(self, student: Student):
        for _student in self.db.all_student():
            if _student[1] == student.first_name and _student[2] == student.last_name:
                raise StudentAlreadyExists
        else:
            self.db.add_new_student(student)
            self.student_record.append(student)
            print("Student has been added successfully!")

    def modified_fname(self, student: Student):
        for _student in self.db.all_student():
            if _student[1] == student.first_name and _student[2] == student.last_name:
                raise Exception
        else:
            self.db.update_first_name(student)
            print("Student's first name has been updated successfully!")

    def modified_lname(self, student: Student):
        for _student in self.db.all_student():
            if _student[1] == student.first_name and _student[2] == student.last_name:
                raise Exception
        else:
            self.db.update_last_name(student)
            print("Student's first name has been updated successfully!")
        
    def modified_fname(self, student: Student):
        for _student in self.db.all_student():
            if _student[1] == student.first_name and _student[2] == student.last_name:
                raise Exception
        else:
            self.db.update_first_name(student)
            print("Student's first name has been updated successfully!")


    def mark_attendance(self, id):
        date = datetime.datetime.now().date()
        current_time = datetime.datetime.now().time()
        lesson_start_time = datetime.time(10, 0, 0)  # Lesson starts at 10 am

        student = self.db.get_student_by_id(id)
        if student:
            if current_time < lesson_start_time:
                # If the student arrives before 10 am, mark them as present
                if date in self.attendance_record.keys():
                    self.attendance_record[date].append(student)
                    student.is_present = True
                else:
                    self.attendance_record[date] = [student]
                print("Student marked as present.")
            else:
                # If the student arrives at or after 10 am, mark them as absent
                student.is_present = False
                print("Student marked as absent.")
        else:
            raise StudentNotFound
                
    def display_all(self):
        return self.db.all_student()


manager = AttendanceSystem()

# Add Students
student1 = Student(1, 'Jax', 'Walker', '167825576')
student2 = Student(2, 'Kate', 'Samson', '0606438256')

# Add the students to the database
manager.db.add_new_student(student1)
manager.db.add_new_student(student2)

# Add the students to the student_record list
manager.student_record.append(student1)
manager.student_record.append(student2)

# Update Student Information
studentID = input("Enter student ID to update: ")
newFirstName = input("Enter the new first name: ")
manager.db.update_first_name(studentID, newFirstName)

# Mark Attendance
studentID = input("Enter student ID to mark attendance: ")
try:
    manager.mark_attendance(studentID)

except StudentNotFound:
    print("Student not found.")

else:
    print("Attendance marked successfully.")

all_students = manager.display_all()
for student in all_students:
    print(student)


# studentID = input("Enter student ID: ")
# student = manager.mark_attendance(studentID)

# if student:
#     # Add the student to the student_record list
#     manager.student_record.append(student)

#     # Mark attendance for the student
#     manager.mark_attendance(studentID)
# else:
#     print("Student not found.")

# studentID = input("Enter student ID to mark attendance: ")
# try:
#     manager.mark_attendance(studentID)
# except StudentNotFound:
#     print("Student not found.")
# else:
#     print("Attendance marked successfully.")

# student1 = Student(1, 'John', 'James', '2345667893')
# student2 = Student('James', 'John', '234566')
# student3 = Student("Paul", "Franklin", "690352")
# student4 = Student("Kate", "Helga", "123456")

# studentID = input("Enter student ID: ")

# newFirstName = input("Enter the new first name of the student: ")
# manager.db.update_first_name(studentID, newFirstName)

# newLastName = input("Enter the new last name of the student: ")
# manager.db.update_last_name(studentID, newLastName)

# newPhoneNumber = input("Enter the new phone number of the student: ")
# manager.db.update_phone_number(studentID, newPhoneNumber)

# studentID = input("Enter student ID: ")
# manager.mark_attendance(studentID)




# details = Student(studentID, studentFirstName, studentLastName, studentPhoneNumber))
# manager.add_student(details)
# print(manager.display_all_details())

# manager.add_student(student1)
# manager.add_student(student2)
# manager.add_student(student3)
# manager.add_student(student4)

# manager.modified_fname(student1)