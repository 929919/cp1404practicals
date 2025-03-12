"""CP1404 Intermediate Exercises - Programming Language class.
Estimated time: 30 minutes
Actual time: [To be recorded]
Start time: 10:00 AM, March 11, 2025
"""


class ProgrammingLanguage:
    """Represent a programming language with its properties."""

    def __init__(self, name, typing, reflection, year):
        """Initialize a ProgrammingLanguage instance.

        name: str, name of the programming language
        typing: str, 'Static' or 'Dynamic'
        reflection: bool, whether the language supports reflection
        year: int, year the language first appeared
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if the language is dynamically typed, False otherwise."""
        return self.typing == "Dynamic"