import math  # Importing math module for mathematical operations like pi and square root


# Base class: Shape

class Shape:
    # Define a generic method for area, to be overridden in child classes
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")
    
    # Define a generic method for perimeter, to be overridden in child classes
    def perimeter(self):
        raise NotImplementedError("Subclasses must implement this method")

# Derived class: Circle

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius  # Store the radius when creating the object

    # Override area method for Circle
    def area(self):
        return math.pi * self.radius ** 2  # Area formula: πr²

    # Override perimeter method for Circle
    def perimeter(self):
        return 2 * math.pi * self.radius  # Circumference formula: 2πr

# Derived class: Rectangle

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width      # Store width
        self.height = height    # Store height

    # Override area method for Rectangle
    def area(self):
        return self.width * self.height  # Area formula: width × height

    # Override perimeter method for Rectangle
    def perimeter(self):
        return 2 * (self.width + self.height)  # Perimeter formula: 2(w + h)

# Derived class: Triangle

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a  # Side a
        self.b = b  # Side b
        self.c = c  # Side c

    # Override area method for Triangle using Heron's formula
    def area(self):
        s = (self.a + self.b + self.c) / 2  # Semi-perimeter
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        # Heron's formula for area of triangle

    # Override perimeter method for Triangle
    def perimeter(self):
        return self.a + self.b + self.c  # Perimeter = sum of all sides


# Creating a list of different shapes

shapes = [
    Circle(radius=5),              # Circle with radius 5
    Rectangle(width=4, height=6),  # Rectangle with width 4 and height 6
    Triangle(a=3, b=5, c=4)        # Triangle with sides 3, 5, and 4
]

# Loop through each shape and print its area and perimeter

for shape in shapes:
    # __class__.__name__ returns the class name like 'Circle', 'Rectangle'
    print(f"{shape.__class__.__name__} Area: {shape.area(): .2f}, Perimeter: {shape.perimeter(): .2f}")
