"""CP1404 Practical - Guitar class.
Estimated time: 15 minutes
Actual time: 20 minutes
"""


class Guitar:
    """Represent a guitar with its properties."""

    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar instance.

        name: str, name of the guitar
        year: int, year the guitar was made
        cost: float, cost of the guitar
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return the age of the guitar in years (as of 2025)."""
        return 2025 - self.year

    def is_vintage(self):
        """Return True if the guitar is 50 or more years old, False otherwise."""
        return self.get_age() >= 50