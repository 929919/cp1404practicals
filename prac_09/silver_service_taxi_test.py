from silver_service_taxi import SilverServiceTaxi

def test_silver_service_taxi():

    silver_taxi = SilverServiceTaxi("Hummer", 200, 2)  # Hummer with fanciness 2
    fare = silver_taxi.calculate_fare(18)  # 18 km trip
    assert abs(fare - 48.78) < 0.01, f"Expected fare 48.78, but got {fare}"