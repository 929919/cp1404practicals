from prac_09.silver_service_taxi import SilverServiceTaxi


def test_silver_service_taxi():

    silver_taxi = SilverServiceTaxi("Hummer", 200, 2)
    silver_taxi.start_fare()
    silver_taxi.drive(18)

    fare = silver_taxi.get_fare()
    print(f"Fare for 18 km: ${fare:.2f}")

    expected_str = "Hummer, fuel=200, odo=18, 18km on current fare, $4.92/km plus flagfall of $4.50"
    assert silver_taxi.__str__() == expected_str, f"Expected: {expected_str}, but got: {silver_taxi.__str__()}"


test_silver_service_taxi()
