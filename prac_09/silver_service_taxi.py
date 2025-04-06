from taxi import Taxi  # Assuming the Taxi class is in taxi.py

class SilverServiceTaxi(Taxi):
    flagfall = 4.50  

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel, 1)  # Assume base price_per_km for Taxi is 1
        self.fanciness = fanciness
        self.price_per_km *= self.fanciness  # Adjust the price_per_km based on fanciness

    def calculate_fare(self, distance):
        fare = super().calculate_fare(distance)  # Call Taxi's fare calculation
        return fare + self.flagfall

    def __str__(self):
        return f"{self.name}, fuel={self.fuel}, odo={self.odo}, {self.distance}km on current fare, ${self.price_per_km}/km plus flagfall of ${self.flagfall}"

