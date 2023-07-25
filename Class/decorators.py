# class Person:
#     @classmethod
#     def age(cls):
#         print("staff")

# # you can't use attribute method such as self inside class methods

# Person.age()

# def hello(test):
#     print(test)

# def say_something():
#     return "Hello World"

# def say_somethingelse():
#     return "Greet"

# a = hello(say_somethingelse)
# print(a)

def hello(test):
    if test() > 9:
        print("Hello WOrld")
        return test
    else:
        print("You're not welcome")
        return test

@hello
def say_somethingelse():
    return 20

a = say_somethingelse()

print(a)