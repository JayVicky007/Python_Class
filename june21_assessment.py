'''
Define a class called Employee with a constructor that takes a name and a salary.
#The class should have a method called get_salary that returns the salary of the employee.

#Define two subclasses of Employee called Manager and Engineer, that inherit from Employee
and have their own attributes.
#The Manager class should have a bonus of 10% of the salary and the Engineer class should
have a bonus of 5% of the salary.
#The subclasses should override the get_salary method to return the salary plus the bonus.

Write a function called payroll that takes a list of employees and prints their name and salary.

#Create a list of employees with different names and salaries and pass it to the payroll function.

'''

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary


class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def get_salary(self):
        bonus = self.salary * 0.1  # 10% bonus i.e 10/100
        return round(self.salary + bonus)


class Engineer(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def get_salary(self):
        bonus = self.salary * 0.05  # 5% bonus i.e 5/100
        return round(self.salary + bonus)


def payroll(employees):
    for i in employees:
        print(f"Name: {i.name} \nSalary: ${i.get_salary()}\n")


employees = [Manager("Jay", 200000), Engineer("Mary", 100000)]

payroll(employees)
    
