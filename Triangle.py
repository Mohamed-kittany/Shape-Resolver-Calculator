# !/usr/bin/env python3
from Shape import Shape

class Triangle(Shape):
    def __init__(self, base: float, height: float):
        self.base = self.validate_positive_number(base, "Base")
        self.height = self.validate_positive_number(height, "Height")

    def get_area(self) -> float:
        return 0.5 * self.base * self.height

    def __str__(self) -> str:
        return f"The Triangle area is: {self.get_area():.2f}"

