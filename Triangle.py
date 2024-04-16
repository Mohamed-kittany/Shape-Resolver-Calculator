# !/usr/bin/env python3
from Rectangle import Rectangle


class Triangle(Rectangle):
    def __init__(self, base,height,side3,side4):
        if base <= 0 or height <= 0 or side3 <= 0 or side4 <= 0:
            raise ValueError("Side lengths of Triangle must be positive.")
        super().__init__(base, height)
        self.side3 = side3
        self.side4 = side4
   
    # Override the get_area method
    def get_area(self):
        return ((super().get_area()) / 2)
    
    # Override the get_perimeter method
    def get_perimeter(self):
        return self.side3 + self.side4 + self.side1
    # Override the str method
    def __str__(self):
        return f"The Triangle area is: {self.get_area()} , The Triangle perimeter is: {self.get_perimeter()}"
