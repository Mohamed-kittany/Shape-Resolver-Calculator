# !/usr/bin/env python3
from Shape import Shape


class Rectangle(Shape):
    def __init__(self, side1, side2):
        if side1 <= 0 or side2 <= 0:
            raise ValueError("Side lengths of Rectangle must be positive.")
        super().__init__(side1, side2)  # Call the superclass constructor
    
    # Override the gget_area method
    def get_area(self):
        return self.side1 * self.side2
  
    # Override the get_perimeter method
    def get_perimeter(self):
        return (2 * self.side1 + 2 * self.side2)

    # Override the str method
    def __str__(self):
        return f"The Rectangle area is: {self.get_area()} , The Rectangle perimeter is: {self.get_perimeter()}"
