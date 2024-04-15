# !/usr/bin/env python3
from Rectangle import Rectangle
from math import sqrt


class Hexagon(Rectangle):
    def __init__(self, side1):
        super().__init__(side1, side1)  # Call the superclass constructor
    def get_area(self):
        return (3 * sqrt(3) * self.side1 ** 2) / 2

    # Override the get area method
    def __str__(self):
        return f"The Hexagon area is: {self.get_area()}"
