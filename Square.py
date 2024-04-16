# !/usr/bin/env python3
from Rectangle import Rectangle

# Define a subclass Square inheriting from Rectangle
class Square(Rectangle):
    def __init__(self, side):
        if side <= 0:
            raise ValueError("Side lengths of Square must be positive.")
        super().__init__(side , side)  # Call the superclass constructor

    # Override the str method
    def __str__(self):
        return f"The square area is: {self.get_area()} , The square perimeter is: {self.get_perimeter()}"
   
