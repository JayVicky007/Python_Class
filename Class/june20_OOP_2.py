# class Company:
#     def __init__(self, company_name):   #constructor
#         self.company = company_name  # instance attribute

#     def profile(self):  # method
#         print(self.company)


# class Work(Company):
#     def __init__(self, occupation, company):
#         super().__init__(company)
#         self.occupation = occupation

#     def work_profile(self):
#         print(f"The company {self.company} has {self.occupation}")


# class Employee(Work):
#     def __init__(self, salary, name, company, work):
#         super().__init__(work, company)
#         self.name = name
#         self.salary = salary

#     def staff_profile(self):
#         print(f"{self.name} works in {self.company} as {self.occupation}")


# john = Employee(100000, "John", "FIRS", "Tech Engineer")
# print(john.name, john.company, john.occupation, john.salary)

#little exercise
# class Vehicle:
#     def __init__(self, maxspeed, mileage):
#         self.maxspeed = maxspeed
#         self.mileage = mileage

# model = Vehicle(240, 30000)
# print(model.maxspeed, model.mileage)


# Hierachical inheritance

class Company:
    def __init__(self, company_name):
        self.company_name = company_name

    def company_profile(self):
        print(self.company_name)

class Employee(Company):
    def __init__(self, name, company_name):
        super().__init__(company_name)
        self.name = name
        self.salary = 50000

class Manager(Company):
    def __init__(self, name, company_name):
        super().__init__()









'''

create a class that takes a dictionary of names of people as the key and their score as the values. e.g

{"John": 72, "James": 84} 

assign them grades based on their scores

get the total number of people that submitted their score. 

output should be something John: A, James: B
2

'''

class Grade:
    def __init__(self, scores):
        self.scores = scores

    def assign_grades(self):
        grades = {}
        for name, score in self.scores.items():
            if score >= 70:
                grade = "A"
            elif score >= 60:
                grade = "B"
            elif score >= 50:
                grade = "C"
            elif score >= 45:
                grade = "D"
            elif score >= 40:
                grade = "E"
            else:
                grade = "F"
            grades[name] = grade
        return grades

    def submit(self):
        return len(self.scores)

scores = {"Johnbull": 75, "Phoenix": 64, "Mary": 53, "Django": 46, "Peacock": 41, "Rooster": 30}
result = Grade(scores)
grades = result.assign_grades()

for name, grade in grades.items():
    print(f"{name}: {grade}")

print(f"Number of students who submitted: {result.submit()}")


    
# class Grades:
#     def __init__(self, dict):
#         self.dict = dict
#         count = 0
#         for i in dict:


        

    



