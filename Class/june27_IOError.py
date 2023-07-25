try:
    with open("main.txt", "r") as file:
        print(file.read())
except IOError:
    with open("main.txt", "w") as file:
        file.write("Hello World")
    print("File does not exist but it has been created.")
finally:
    print("Let's Proceed")