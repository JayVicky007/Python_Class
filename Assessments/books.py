'''
Create a program that reads a text file containing information about a group of books. 
Each line the file should contain the book's title, author, and ISBN, separated by commas. 
Your program should create a Book class with attributes for title, author, and ISBN, 
and a method for displaying the book's information. 
The program should then read the file, create a Book object for each book, and store the objects in a list. 
Finally, the program should print the list of books to the console.

'''

# import os
# print(os.getcwd())

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def display_info(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"


book_list = []

file_path = r"C:\Users\Jay Vicky\Python_Class\Assessments\books.txt"
with open(file_path, "r") as file:
    for line in file:
        
        book_data = line.strip().split(",")
        title = book_data[0].strip()
        author = book_data[1].strip()
        isbn = book_data[2].strip()
        
        book = Book(title, author, isbn)
        book_list.append(book)

for book in book_list:
    print(book.display_info())
