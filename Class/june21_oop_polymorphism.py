# Polymorphism - 
#  ability of functions, operators etc. to perform different functions

# name = "John" + "James"
# # name = 1 + 4

# print(name)

# def add_numbers(a, b, c=10):
#     return a + b + c
# print(add_numbers(2, 6))
# print(add_numbers(2, 9, 20))

# Method overriding

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def display_work(self):
#         print("Engineering")

# class Organization:
#     def __init__(self, org_name):
#         self.org_name = org_name

# class Employee1(Organization):
#     def __init__(self, ename, org_name):
#         Organization.__init__(self, org_name)
#         self.employee = ename

# class Employee2(Organization):
#     def __init__(self, ename, org_name):
#         super().__init__(org_name)


# class Manager(Employee1, Employee2):
#     def __init__(self, ename1, ename2, org_name):
#         Employee1.__init__(self, ename1, org_name)
#         Employee2.__init__(self, ename2, "FIRS")

# james = Manager("Jay", "John", "NNPC")
# print(james.org_name)


class Manager:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def profile(self):
        return f"{self.name} gets paid ${self.salary} monthly."

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def profile(self):
        return f"{self.name} gets paid ${self.salary} monthly."
        
# both classes have the same atributes
    
john = Manager("John", 20000)
mary = Employee("Mary", 25000)

management = [john, mary]

for i in management:
    print(i.profile())



