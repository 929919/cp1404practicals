"""CP1404/CP5632 Practical - Used cars example."""
from prac_06.car import Car

def main():
    my_car = Car(180, name="My Sedan")
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(f"Car has odometer: {my_car._odometer}")

    limo = Car(100, name="Luxury Limo")
    limo.add_fuel(20)
    print(f"Limo fuel: {limo.fuel}")
    limo.drive(115)

    print(my_car)
    print(limo)

if __name__ == "__main__":
    main()