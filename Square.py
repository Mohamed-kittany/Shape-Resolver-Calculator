# !/usr/bin/env python3
from Rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side: float):
        super().__init__(side, side)

    def __str__(self) -> str:
        return f"The Square area is: {self.get_area():.2f}"

