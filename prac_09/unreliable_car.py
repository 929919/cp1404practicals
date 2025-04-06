"""
CP1404/CP5632 Practical
UnreliableCar class (inherits from Car)
"""

import random
from prac_09.car import Car


class UnreliableCar(Car):
    """A Car that might not drive all the time based on reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance."""
        super().__init__(name, fuel)
        self.reliability = reliability