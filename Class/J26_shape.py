'''
Create a Python cass called Rectangle that represents a rectangle. The
class should have the following properties:

width: the width of the rectangle (a float or integer)
height: the height of the rectangle (a float or integer)

The class should also have the following methods:

area(): calculates the area of the rectangle and returns it as a float.
perimeter(): calculates the perimeter of the rectangle and returns it as a
float

scale(n): scales the rectangle by a factor of n. The width and the height of the rectangle should be multiplied by n 

'''

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return float(self.width * self.height)

    def perimeter(self):
        return float(2 * (self.width + self.height))

    def scale(self, n):
        self.width *= n
        self.height *= n

# Create a rectangle object with width 5 and height 3
rect = Rectangle(5, 3)

# Calculate and print the area of the rectangle
print("Area:", rect.area())

# Calculate and print the perimeter of the rectangle
print("Perimeter:", rect.perimeter())

# Scale the rectangle by a factor of 2
rect.scale(2)

# Print the updated width and height of the rectangle
print("Scaled width:", rect.width)
print("Scaled height:", rect.height)

