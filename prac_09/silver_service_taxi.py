from prac_09.taxi import Taxi  # Importing Taxi class from your module

class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes a 'fanciness' multiplier and flagfall."""
    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= self.fanciness
        self.flagfall = 4.50
    def get_fare(self):
        """Return the fare for the SilverServiceTaxi trip, including flagfall."""
        fare = super().get_fare()
        return fare + self.flagfall

    def __str__(self):
        """Return a string representation of the SilverServiceTaxi with flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
