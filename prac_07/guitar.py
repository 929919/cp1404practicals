"""CP1404 Practical - Guitars program.
Estimated time: 20 minutes
Actual time: 20 minutes
"""
from guitar import Guitar

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


def main():
    print("My guitars!")
    guitars = []

    # print("My guitars!")
    # guitars = []
    #
    # # Simulação de entrada
    # name = "Fender Stratocaster"
    # year = 2014
    # cost = 765.4
    # guitar = Guitar(name, year, cost)
    # guitars.append(guitar)
    # print(f"{guitar} added.\n")
    #
    # name = ""  # Encerra o loop
    #
    # print("\nThese are my guitars:")
    # for i, guitar in enumerate(guitars, 1):
    #     vintage_string = " (vintage)" if guitar.is_vintage() else ""
    #     print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")



    guitars.append(Guitar("Fender Stratocaster", 2014, 765.40))
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.90))

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")



if __name__ == "__main__":
    main()