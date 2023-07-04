# # import math

# # print(math.sqrt(25))

# # if you don't need all the functions inside the math package
# from math import sqrt

# print(sqrt(25))

# # for factorial
# from math import factorial

# print(factorial(5))

# # to get the current directory/path of where we're running our code

# import os

# os.mkdir("tester")
# print(os.chdir("C:\\Users\\Jay Vicky\\Python_Class"))  # use two backslashes insteas of one
# print(os.getcwd())

# import math

# print(math.ceil(4.578)) 
# math.floor(4.578)

# import random

# test_list = list("Hello World")
# random.shuffle(test_list)

# print("".join(test_list))

# import random

# names = ["Kate", "John", "James", "Bob"]

# print(random.choice(names))


import time, random

names = ["Kate", "John", "James", "Bob"]

time.sleep(5) # delays the display of output

print(random.choice(names))

