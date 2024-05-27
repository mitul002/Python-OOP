from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    @abstractmethod
    def area(self):
        pass  # Abstract method doesn't have a body
                # we cant create object of abstract  class

class Triangle(Shape):
    def area(self):  # Area is overridden
        area = 0.5 * self.dim1 * self.dim2
        print(f"Area of triangle: {area}")

class Rectangle(Shape):
    def area(self):  # Area is overridden
        area = self.dim1 * self.dim2
        print(f"Area of rectangle: {area}")

t1 = Triangle(20, 30)
t1.area()

r1 = Rectangle(20, 30)
r1.area()
