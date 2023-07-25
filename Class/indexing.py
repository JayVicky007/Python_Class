full_name = "John Alex"
names = ["John", "James", "Alex", "Helga"]
print(names[-len(names)]) # len of name = 4: -len(names) = -4 aka index 0 in this case
print(full_name[0])
print(full_name[:6])
print(full_name[1:8:2])
print(full_name[::-1]) # reverse
print(full_name[::2]) #