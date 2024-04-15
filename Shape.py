# !/usr/bin/env python3
from abc import ABC, abstractmethod

class Shape(ABC):
    @staticmethod
    def validate_positive_number(value: float, name: str = "Value") -> float:
        """
        Validates that a number is non-negative.

        Args:
        value (float): The value to validate.
        name (str): The name of the parameter, used in the error message.

        Returns:
        float: The validated value if it's non-negative.

        Raises:
        ValueError: If the value is negative.
        """
        if value < 0:
            raise ValueError(f"{name} must be non-negative")
        return value

    @abstractmethod
    def get_area(self) -> float:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass




