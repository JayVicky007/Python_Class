# How to open/read a file 

# result = open("text.txt", "r")
# output = result.read()
# print(output)

with open("text.txt", "r") as f:
    result = f.read()

print(result)

# How to write

# result = open("text.txt", "w")
# result.writelines(["Hello \n", "World \n", "This is fun"])
