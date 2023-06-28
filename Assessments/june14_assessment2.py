def my_list(lst):
    # new_list = []
    # for item in lst:
    #     if len(item) > 4:
    #         new_list.append(item)
    # return new_list
    return [item for item in lst if len(item) > 4]
    
new_list = my_list(["King", "Queen", "Prince", "Princess", "Chief"])
print(new_list)


# my_list = ["King", "Queen", "Prince", "Princess", "Chief"]

# new_list = []

# new_list = [item for item in my_list if len(item) > 4]

# print(new_list)