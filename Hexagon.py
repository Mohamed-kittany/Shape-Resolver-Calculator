# !/usr/bin/env python3
from Shape import Shape
from math import sqrt

class Hexagon(Shape):
    def __init__(self, side: float):
        self.side = self.validate_positive_number(side, "Side")

    def get_area(self) -> float:
        return (3 * sqrt(3) * (self.side ** 2)) / 2

    def __str__(self) -> str:
        return f"The Hexagon area is: {self.get_area():.2f}"

