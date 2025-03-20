"""CP1404 Practical - More Guitars!"""

from guitar import Guitar

FILENAME = "guitars.csv"

def load_guitars():
    """Load guitars from a CSV file and return a list of Guitar objects."""
    guitars = []
    with open(FILENAME, "r") as file:
        for line in file:
            name, year, cost = line.strip().split(",")
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars

def display_guitars(guitars):
    """Display all guitars in the list."""
    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")

def main():
    """Main function to load and display guitars."""
    guitars = load_guitars()
    display_guitars(guitars)

if __name__ == "__main__":
    main()
