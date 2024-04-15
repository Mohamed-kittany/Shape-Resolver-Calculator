# !/usr/bin/env python3
from Shape import Shape

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = self.validate_positive_number(width, "Width")
        self.height = self.validate_positive_number(height, "Height")

    def get_area(self) -> float:
        return self.width * self.height

    def __str__(self) -> str:
        return f"The Rectangle area is: {self.get_area():.2f}"
