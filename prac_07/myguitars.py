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
    """Main function to load, sort, and display guitars."""
    guitars = load_guitars()
    print("\nOriginal list of guitars:")
    display_guitars(guitars)

    # Sort guitars by year
    guitars.sort()

    print("\nSorted guitars (oldest to newest):")
    display_guitars(guitars)

def add_guitars(guitars):
    """Allow user to add new guitars."""
    print("\nAdd new guitars (leave name empty to finish):")
    while True:
        name = input("Guitar name: ")
        if not name:
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))

def save_guitars(guitars):
    """Save all guitars to the CSV file."""
    with open(FILENAME, "w") as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")
    print("\nGuitars saved to file.")


if __name__ == "__main__":
    main()
