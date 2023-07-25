# class NegativeNumError(Exception):
#     pass

# def get_valid_num():
#     user_input = input("Enter a number: ")
#     while not user_input.isdigit() or float(user_input) < 0:
#         if not user_input.isdigit():
#             print("Input a valid number")
#         else:
#             print("Input must be a positive number")
#         user_input = input("Enter a number: ")
#     return float(user_input) ** 2

# valid_num = get_valid_num()
# print(valid_num)



# def get_valid_num():
#     user_input = input("Enter a number: ")
#     while True:
#         if user_input.isdigit():
#             if float(user_input) >= 0:
#                 return float(user_input) ** 2
#             else:
#                 print("Input must be a positive number")
#         else:
#             print("Input a valid number")
#         user_input = input("Enter a number: ")

# valid_num = get_valid_num()
# print(valid_num)

while True:
    number = input("Enter a number: ")

    if not number.isdigit():
        print("That is not a digit")
    elif number.isdigit():
        print(int(number) **2)
        break
    else:
        print("The number should be positive")





















# class NegativeNumError(Exception):
#     pass

# def get_valid_num():
    
#     while True:
#         try:
#             user_input = float(input("Enter a number: "))
#             if user_input < 0:
#                 raise NegativeNumError
#             return user_input ** 2
#         except ValueError:
#             print("Input a valid number")
#         except NegativeNumError:
#             print("Input must be a positive number")

# valid_num = get_valid_num()
# print(valid_num)

# do it without using the try and except method

    
