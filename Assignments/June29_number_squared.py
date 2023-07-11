class NegativeNumError(Exception):
    pass

def get_valid_num():
    
    while True:
        try:
            user_input = float(input("Enter a number: "))
            if user_input < 0:
                raise NegativeNumError
            return user_input ** 2
        except ValueError:
            print("Input a valid number")
        except NegativeNumError:
            print("Input must be a positive number")

valid_num = get_valid_num()
print(valid_num)

    
    