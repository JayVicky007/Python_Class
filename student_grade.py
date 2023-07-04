'''
1. Define a class Student with the following attribute; 
- name(String)
- age(integer)
- score (integer)
2. Create a file (name.txt) and add 10 names in each line
3. Use the open function to read from the file and get the names
4. Use the names gotten from the file to create a student object, using the names as attribute name, 
use the random package to create random ages from 16 - 19, 
and use the random package to add random scores from 20, 100
5. Create a method in Student to get the grade of the score;
- < 30 = F
- 30 - 40 = E
- 40 - 60 = C
- 60 - 70 = B
- 70  - 100 = A

'''

import random

class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def get_grade(self):

        if self.score <= 30:
            return "F"
        if self.score > 30 and self.score <= 40:
            return "E"
        if self.score > 40 and self.score <= 60:
            return "C"
        if self.score > 60 and self.score <= 70:
            return "B"
        if self.score > 70 and self.score <= 100:
            return "A"
        
names = ["Jack Bauer", "Ragnar Lothbrok", "Michael Scofield", "Walter White", "Jack Sparrow", "Col. Mustang", "Hououin Kyouma", "Kurapika", "Chrollo", "Christina"]

with open("names.txt", "w") as f: 
    for name in names:
        f.write(f"{name} \n")

with open("names.txt", "r") as f:
    read_lines = f.readlines()

students = []
for name in read_lines:
    name = name.strip()
    age = random.randint(16, 19)
    score = random.randint(20, 100)
    student = Student(name, age, score)
    students.append(student)

for student in students:
    print(f"Name: {student.name}, Age: {student.age}, Score: {student.score}, Grade: {student.get_grade()}")
