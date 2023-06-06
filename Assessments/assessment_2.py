def largest_divisible(lst, n):
    myList = []
    for i in lst:
        if i % n == 0:
            myList.append(i)
    if len(myList) == 0:
        return None
    max_num = max(myList)
    return max_num

largest_number = largest_divisible([4, 11, 13, 25, 3, 18, 97, 100], 5)
print(largest_number)





# User Input
# print("Welcome! Enter five numbers.")
# num1 = input("Enter first number: ")
# num2 = input("Enter second number: ")
# num3 = input("Enter third number: ")
# num4 = input("Enter fourth number: ")
# num5 = input("Enter fifth number: ")
# length = len(numbers)
# print(length)