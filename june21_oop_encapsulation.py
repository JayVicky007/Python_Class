# Encapsulation

# public: accessible anyywhere in the class
# protected: repped by _
#private: repped by __

class Employee:
    def __init__(self, name, salary):
        self.name = name
        # self._salary = salary
        self.__salary = salary  # private method

    # def show_salary(self):
    #     return self.__salary # private method
    def show_salary(self):
        print(self.__salary)

class Work(Employee):
    def __init__(self, ename, esalary, work):
        super().__init__(ename, esalary)

        self.work = work

# john = Work("John", 20000, "Taxi Driver")
# print(john.name)
# print(john.show_salary()) # printing private method
john = Employee("John", 20000)
print(john._Employee__salary)   # printing




    