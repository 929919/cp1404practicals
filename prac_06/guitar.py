"""CP1404 Practical - Guitar class.
Estimated time: 15 minutes
Actual time: [To be recorded]
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