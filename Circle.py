# !/usr/bin/env python3
from Shape import Shape
import math


class Circle(Shape):
    def __init__(self, side):
        super().__init__(side, side)  # Call the superclass constructor

    def get_area(self):
        return math.pi * (self.side1 ** 2)

    # Override the get area method
    def __str__(self):
        return f"The Circle area is: {self.get_area()}"
