
# def find_common_elements(*args):
#     common_elements = []
#     for i in args[0]:
#         if i in list(set(args[0]) & set((args[1]))):
#             common_elements.append(i)

#     return common_elements
# result = find_common_elements([1,2,3 ,"John", "James", "Frank"], [2, "Frank", 3, "John"])
# print(result)

list1 = [1,"John",3,4,5]
list2 = [2,4,5,"John",9]

def find_common_element(list1, list2):
    common_element = []
    for i in list1:
        for j in list2:
            if i == j:
                common_element.append(i)
    return common_element

result = find_common_element(list1, list2)
print(result)