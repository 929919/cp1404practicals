from silver_service_taxi import SilverServiceTaxi

def test_silver_service_taxi():

    silver_taxi = SilverServiceTaxi("Hummer", 200, 2)  # Hummer with fanciness 2
    fare = silver_taxi.calculate_fare(18)  # 18 km trip
    assert abs(fare - 48.78) < 0.01, f"Expected fare 48.78, but got {fare}"

    expected_str = "Hummer, fuel=200, odo=0, 0km on current fare, $4.92/km plus flagfall of $4.50"
    assert silver_taxi.__str__() == expected_str, f"Expected '{expected_str}', but got {silver_taxi.__str__()}"


# Run the test
test_silver_service_taxi()