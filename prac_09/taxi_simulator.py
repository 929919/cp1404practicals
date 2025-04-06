from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi



def main():
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]

    current_taxi = None
    total_bill = 0

    program_running = True  # Control variable for the loop

    while program_running:
        print(f"\nBill to date: ${total_bill:.2f}")
        print("q)uit, c)hoose taxi, d)rive")
        choice = input(">>> ").strip().lower()

        if choice == "q":
            # Quit the program and show total trip cost
            print(f"Total trip cost: ${total_bill:.2f}")
            print("Taxis are now:")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")
            program_running = False  # Exit the loop

        elif choice == "c":
            # Choose a taxi from the list
            print("Taxis available:")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")

            try:
                taxi_choice = int(input("Choose taxi: "))
                if 0 <= taxi_choice < len(taxis):
                    current_taxi = taxis[taxi_choice]
                    print(f"You chose: {current_taxi}")
                else:
                    print("Invalid taxi choice")
            except ValueError:
                print("Invalid option")

        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                try:
                    # Drive the chosen taxi
                    distance = float(input("Drive how far? "))
                    current_taxi.start_fare()
                    current_taxi.drive(distance)
                    fare = current_taxi.get_fare()
                    total_bill += fare
                    print(f"Your {current_taxi.name} trip cost you ${fare:.2f}")
                except ValueError:
                    print("Invalid distance")
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
