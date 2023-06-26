# Wednesday June 14th, 2023

# items = []

# for i in range(10):
#     items.append(i)

# print(items)

# items = [i for i in range(10)]

# print(items)

# items = [i*2 for i in range(10)]

# print(items)

# conversion of celsius to farenheit

# def convert_to_f(value):
#     result = (value * (9/5)) + 32
#     return result

# c_temp = [12.5, 33.3, 7.9, 22.89]

# f_temp = []

# f_temp = [convert_to_f(temp) for temp in c_temp] #List comprehension

# for temp in c_temp:
#     f_temp.append(convert_to_f(temp)) # you can use either for loop or list comprehension

# print(f_temp)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
c = []

# for value in a:
#     if value in b:
#         c.append(value)
    
# print(c)

# c = [value for value in a if value in b] # same as above

# print(c)

# for x in a:
#     for y in b:
#         if x == y:
#             c.append(x*y)
#         else:
#             c.append(1)

# print(c)

# # c = [x*y for x in a for y in b if x == y]

# c = [x*y if x == y else 1 for x in a for y in b] #added an else statement
# # if you have an else statement, you start with the condition.
# print(c)

# for x in b:
#     for y in a:
#         if x%y != 0:
#             c.append(x%y)

# print(c)

# c = [x%y for x in b for y in a if x%y != 0]

# print(c)

# a = [1, 2, 3, 4, 5. 6, 7, 8, 9, 10]

# b = {i:i*2 for i in a}

# print(b)

# nums = [n for n in range(100) if sum([int(j) for j in str(n)]) % 7 == 0]

# print(nums)

# a = [1,2,3,4,5]
# b = [2,4,6,8,10]
# c = [1,3,5,7,9]

# nums = []

# threshold = 10
# x = 9

# if x < threshold:
#     flag = "Under"
# else:
#     flag = "Over"

# print(flag)

# # tenary assignment

# flag = "Under" if x < threshold else "Over"
# print(flag)


age_limit = 18
user_age = 17

# if user_age < age_limit:
#     response = "You're not old enough"
# else:
#     response = "You're old enough"

response = "You're old enough" if user_age < age_limit else "You're old enough"

print(response)

