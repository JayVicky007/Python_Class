def my_function():
    print("Hello World!")
my_function()

def add():
    print(5+5)
add()

# def my_function(*sum) use (* + arg name) if you don't know how many arguments are going to be passed to your function
def sum(a, b, c):
    print(a, b, c)

sum(1, 2, 3)

# sum("John", 2, True)

def name_of_people(*args):
    print(args)
    for name in args:
        print(name)
name_of_people("John", "James", "Frank", 2, 4, 6)

def name_of_person(name, age):
    print(f"Hi, I'm {name}, and I'm {age} years old")

name_of_person(age = 200, name = "Robocop")

# def name_of_goat(kwargs):
#     print(kwargs["name"])
#     print(kwargs["age"])
#     print(kwargs["occupation"])

# name_of_goat(name = "Messi", age = 37, occupation = "Baller")

def profile(name, age, salary=50000):
    print(f"{name} works in the factory with {salary}")

profile("John,", 29, 100000)

# passing a list as an argument

def profile(list_of_names):
    for names in list_of_names:
        print(names)
profile(["james", "mum", "dad"]) #list
profile(("name", "age", "stuff")) #tuple
profile("you are a clonetrooper.") #string

def name_of_age(age):
    if age > 10:
        return("You are old enough.")
    else:
        return("Go home, kid.")
response = name_of_age(12)
print(response)

#return function
def sum(a, b):
    c = a + b
    return c
response = sum(6, 5)
response2 = response * 2
print(response2)

# recursion
def sum(a, b):

    if a > 0:
        print(a, b)
        a -= 1
        sum(a, b)
sum(4, 2)






