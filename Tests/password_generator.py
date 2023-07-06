# import random

# print(random.randrange(10000000, 90000000))

# import random
# char = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
# print(random.choice(char))

# add a feature to put the program into a file. Name of file should be secret key.

import random
def generatePassword(length):
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = lower_case.upper()
    special_characters = '!"$%^&*()_-+=[]\|,.<>?@#~:;¬`'

    password = []

    for _ in range(length):     # we're using _ because we are neither returning nor printing the value
        our_choice = [str(random.randrange(0, 9)), random.choice(lower_case), random.choice(upper_case), random.choice(special_characters)]
        password.append(random.choice(our_choice))

    return "".join(password)

your_password = generatePassword(14)
print(f"Your password: {your_password}")

with open("Secret_Key.txt", "w") as f:
    f.write(your_password)


