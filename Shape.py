# !/usr/bin/env python3
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def __str__(self):
        pass



