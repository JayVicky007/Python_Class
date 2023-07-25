name = "Hello World"

print(name.upper())

number = [1,2,3,4,5]

number.append(7)

print(number)

class Dog:
    bread = "Bull dog"
    age = 5

    def bark(self):   # first parameter must be self
        print("Barking")

dog = Dog()
print(dog.bread)

dog = Dog()
dog.bark()   # no need to input an argument for self



class Animal:
    
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.sex = gender
    
    # def sound(self):
    #     if self.name == "cat":
    #         print("Meow")
    #     elif self.name == "dog":
    #         print("bark")
    #     else:
    #         print("Don't know sound")

    def get_profile(self):
        print(f"The {self.name} is a {self.sex.lower()} and it is {self.age} years old")

    def profile(self):
        self.get_profile()

dog = Animal("dog", 12, "Male")
dog.age = 24 # reinitializing the attribute
dog.name = "lion"
dog.sex = "FEMALE"

dog.get_profile()
dog.profile()


# class Dog:
#     animal = "dog"

#     def __init__(self, breed, color):

#         self.breed = breed
#         self.color = color


class Animal:

    def sound(self):
        print("animal sound")

class Dog(Animal):  # Dog inherits attributes from Animal class
    def eat(self):
        print("eating")

bull_dog = Dog()
bull_dog.eat()
bull_dog.sound()

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("animal sound")

class Dog(Animal):  # Dog inherits attributes from Animal class
    def __init__(self, name):
        Animal.__init__(self, name)

    def eat(self):
        print("eating")

bull_dog = Dog("Bull Dog")
bull_dog.eat()
bull_dog.sound()
print(bull_dog.name)


# Inheriting multiple classes

class Father:
    def __init__(self, fname):
        self.father_name = fname

    def father_occupation(self):
        print("Engineering")

class Mother:
    def __init__(self, mname):
        self.mother_name = mname

    def mother_occupation(self):
        print("Nursing")

class Child(Father, Mother):
    def __init__(self, cname, fname, mname):
        Father.__init__(self, fname)
        Mother.__init__(self, mname)

        self.child_name = cname

john = Child("John", "James", "Jane")

john.father_occupation()
print(john.mother_name)    

'''

Create a class called MyList that has an attribute called data, which is a list of integers.
The class should have the following methods:

__init__(self, data): Initializes the MyList object with the provided list of integers.
get_item(self, index): Returns the integer at the specified index of the data list.
get_slice(self, start, end): Returns a new My_List object that contains a slice of the data list
from the specified start index (inclusive) to the specified end index (exclusive).

Your task is to write a program that does the following:
Creates an instance of the MyList class with the list [1, 2, 3, 4, 5]
Prints the value at index 2 of the data attribute using the get_item method
Creates a new MyList object that contains a slice of the data list from index 1 (inclusive)
to index 4 (exclusive) using the get_slice method.
Prints the data attribute of the new MyList object.

'''

class MyList:

    def __init__(self, *data):
        self.data = data

    def get_item(self, index):
        return self.data[index]
    
    def get_slice(self, start, end):
        slice = self.data[start:end]
        return slice

My_List = MyList(1,2,3,4,5)
print(My_List.data)
print(My_List.get_item(2))

