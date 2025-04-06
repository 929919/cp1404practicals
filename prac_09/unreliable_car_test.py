from prac_09.unreliable_car import UnreliableCar


def main():
    # Create two UnreliableCars: one highly reliable, one unreliable
    reliable_car = UnreliableCar("Reliable", 100, 90.0)
    unreliable_car = UnreliableCar("Unreliable", 100, 10.0)

    print("Testing Reliable Car (90% reliability)")
    reliable_total_driven = 0
    for _ in range(10):
        driven = reliable_car.drive(10)
        reliable_total_driven += driven
        print(f"Attempted to drive 10km, actually drove {driven}km")
    print(f"Total driven by Reliable Car: {reliable_total_driven}km")

    print("\nTesting Unreliable Car (10% reliability)")
    unreliable_total_driven = 0
    for _ in range(10):
        driven = unreliable_car.drive(10)
        unreliable_total_driven += driven
        print(f"Attempted to drive 10km, actually drove {driven}km")
    print(f"Total driven by Unreliable Car: {unreliable_total_driven}km")


if __name__ == '__main__':
    main()
