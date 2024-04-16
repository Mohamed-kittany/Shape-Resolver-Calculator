# !/usr/bin/env python3
from abc import ABC, abstractmethod

#base class for 2D shapes.
class Shape(ABC):
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2
    
    #Calculates the area of the shape.
    @abstractmethod
    def get_area(self):
        pass
        
    #Calculates the perimeter of the shape.
    @abstractmethod
    def get_perimeter(self):
        pass

    #Returns a string represent the shape.
    @abstractmethod
    def __str__(self):
        pass



