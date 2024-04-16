# !/usr/bin/env python3
from Square import Square
from math import sqrt


class Hexagon(Square):
    def __init__(self, side1):
        if side1 <= 0 :
            raise ValueError("Side lengths of Hexagon must be positive.")
        super().__init__(side1)  # Call the superclass constructor
    
    # Override the get_area method
    def get_area(self):
        return (3 * sqrt(3) * (super().get_area())) / 2
    
    # Override the get_perimeter method
    def get_perimeter(self):
        return (6 * self.side1)

    # Override the str  method
    def __str__(self):
        return f"The Hexagon area is: {self.get_area()},The Hexagon perimeter is: {self.get_perimeter()}"
