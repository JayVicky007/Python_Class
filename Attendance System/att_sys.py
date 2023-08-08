import datetime
import mysql.connector as sql
from dotenv import load_dotenv
import os

load_dotenv()

user = os.environ.get('user')
password = os.environ.get('password')
host = os.environ.get('host')


class StudentNotFound(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class Student:
    def __init__(self, id, first_name, last_name, phoneNumber):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phoneNumber = phoneNumber
        self.is_present = False
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

class DB:
    def __init__(self) -> None:
        self.__db = sql.connect(
            host=host,
            user=user,
            password=password,
            database='attendancemanager'
        )
        self.studentT = 'student'
        self.presentT = 'present'
        self.__cursor = self.__db.cursor()

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

    def mark_student_present(self, student_id, dates):
        # Convert dates to a datetime object with today's date
        today = datetime.date.today()
        datetime_obj = datetime.datetime.combine(today, dates)

        self.__cursor.execute(f'INSERT INTO {self.presentT} (dates, studentID) VALUES (%s, %s)', (datetime_obj, student_id))
        self.__db.commit()


class AttendanceSystem:
    def __init__(self) -> None:
        self.db = DB()
        self.attendance_record = {}
        self.student_record = []

    def add_student(self, student: Student):
        for _student in self.db.all_student():
            if _student[1] == student.first_name and _student[2] == student.last_name:
                raise Exception
        else:
            self.db.add_new_student(student)
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

  
    def mark_attendance(self):
        studentID = input("Enter student ID: ")
        student = self.fetch_student_by_id(studentID)
        if student is not None:
            arrival_time = input(f"Enter the arrival time for {student.first_name} {student.last_name} (HH:MM): ")
            dates = datetime.datetime.strptime(arrival_time, "%H:%M").time()
            preset_time = datetime.time(10, 0)

            if dates < preset_time:
                self.db.mark_student_present(studentID, arrival_time)
                if dates in self.attendance_record.keys():
                    self.attendance_record[dates].append(student)
                else:
                    self.attendance_record[dates] = [student]
                print(f"{student.first_name} {student.last_name} is marked present.")
            else:
                print(f"{student.first_name} {student.last_name} is marked absent.")
        else:
            print("Student not found.")

    def fetch_student_by_id(self, studentID):
        self.db.__cursor.execute(f'SELECT * FROM {self.db.studentT} WHERE id = %s', (studentID,))
        student_data = self.db.__cursor.fetchone()
        if student_data:
            id, first_name, last_name, phone_number = student_data
            return Student(id=id, first_name=first_name, last_name=last_name, phoneNumber=phone_number)
        return None    
        
    def display_all(self):
        return self.db.all_student()
        
    
manager = AttendanceSystem()

all_students = manager.display_all()
for student in all_students:
    print(student)

studentID = input("Enter student ID: ")
manager.mark_attendance(studentID)

# studentID = 2

# # Set the student_record list to contain the students you want to mark attendance for
# # For testing purposes, let's create a Student object with ID 2
# student = Student(id=2, first_name='Jane', last_name='Smith', phoneNumber='987654321')
# manager.student_record = [student]

# try:
#     manager.mark_attendance(studentID)
# except StudentNotFound:
#     print("Student not found.")
  
# studentID = input("Enter student ID: ")

# newFirstName = input("Enter the new first name of the student: ")
# manager.db.update_first_name(studentID, newFirstName)

# newLastName = input("Enter the new last name of the student: ")
# manager.db.update_last_name(studentID, newLastName)

# newPhoneNumber = input("Enter the new phone number of the student: ")
# manager.db.update_phone_number(studentID, newPhoneNumber)

all_students = manager.display_all()
for student in all_students:
    print(f"{student.first_name} {student.last_name} - Present: {student.is_present}")
# student1 = Student(1, 'John', 'James', '234566')
# student2 = Student(2, 'James', 'John', '234566')

# manager.add_student(student1)

