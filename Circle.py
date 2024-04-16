# !/usr/bin/env python3
from Shape import Shape
import math


class Circle(Shape):
    def __init__(self, side):
        if side <= 0:
            raise ValueError("Side lengths of Circle must be positive.")
        super().__init__(side, side)  # Call the   superclass constructor
    
    # Override the get_area method
    def get_area(self):
        return math.pi * (self.side1 ** 2)
    
    # Override the get_perimeter method
    def get_perimeter(self):
        return (math.pi * self.side1 * 2)

    # Override the str area method
    def __str__(self):
        return f"The Circle area is: {self.get_area()},The Circle perimeter is: {self.get_perimeter()}"
