# !/usr/bin/env python3
from Shape import Shape
import math

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = self.validate_positive_number(radius, "Radius")

    def get_area(self) -> float:
        return math.pi * (self.radius ** 2)

    def __str__(self) -> str:
        return f"The Circle area is: {self.get_area():.2f}"

