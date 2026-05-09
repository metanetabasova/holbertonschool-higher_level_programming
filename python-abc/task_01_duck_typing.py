#!/usr/bin/python3
from abc import ABC, abstractmethod
import math

# Blueprint
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Konkret sinifler
class Circle(Shape):
    def __init__(self, radius):
        self.radius = abs(radius)

    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

#Duck Typing istifade eden funksiya
def shape_info(obj):
    #tip yoxlanisi aparilmir sadece metodlar cagirilir
    print(f"Area: {obj.area():.2f}")
    print(f"Perimeter: {obj.perimeter():.2f}")

# Test(istifade)
c = Circle(5)
r = Rectangle(4, 6)

shape_info(c)
shape_info(r)
