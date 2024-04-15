# !/usr/bin/env python3
from Rectangle import Rectangle


class Triangle(Rectangle):
    def __init__(self, base, height):
        super().__init__(base, height)

    def get_area(self):
        return super().get_area() / 2

    def __str__(self):
        return f"The Triangle area is: {self.get_area()}"
