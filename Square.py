# !/usr/bin/env python3
from Rectangle import Rectangle

# Define a subclass Square inheriting from Rectangle
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)  # Call the superclass constructor

    # Override the get area method
    def __str__(self):
        return f"The square area is: {self.get_area()}"
