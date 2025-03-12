"""CP1404 Practical - Guitars program.
Estimated time: 20 minutes
Actual time: 20 minutes
"""
from guitar import Guitar

def main():
    print("My guitars!")
    guitars = []

    # Entrada do usuário (comentada para teste)
    # while True:
    #     name = input("Name: ")
    #     if name == "":
    #         break
    #     year = int(input("Year: "))
    #     cost = float(input("Cost: $"))
    #     guitar = Guitar(name, year, cost)
    #     guitars.append(guitar)
    #     print(f"{guitar} added.\n")

    # Dados de teste
    guitars.append(Guitar("Fender Stratocaster", 2014, 765.40))
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.90))

    # Exibir guitarras
    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")

if __name__ == "__main__":
    main()