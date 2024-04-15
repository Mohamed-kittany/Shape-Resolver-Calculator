# !/usr/bin/env python3
from Shape import Shape


class Rectangle(Shape):
    def __init__(self, side1, side2):
        super().__init__(side1, side2)  # Call the superclass constructor

    def get_area(self):
        return self.side1 * self.side2

    # Override the get area method
    def __str__(self):
        return f"The Rectangle area is: {self.get_area()}"
