"""CP1404 Practical - Guitar class"""

class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name, year, cost):
        """Initialize a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __lt__(self, other):
        """Compare guitars by year for sorting."""
        return self.year < other.year

    def __str__(self):
        """Return string representation of a Guitar."""
        return f"{self.name} ({self.year}) - ${self.cost:,.2f}"

    def is_vintage(self):
        """Determine if a guitar is vintage (50+ years old)."""
        return 2024 - self.year >= 50
