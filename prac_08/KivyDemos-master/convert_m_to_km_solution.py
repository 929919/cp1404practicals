"""
CP1404/CP5632 Practical
Kivy GUI program to convert miles to kilometres
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934  # Conversion constant

class ConvertMilesKmApp(App):
    """App to convert miles to kilometres."""
    output_km = StringProperty("0.0")

    def build(self):
        """Build the app interface from the KV file."""
        self.title = "Miles to Kilometres Converter"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_conversion(self, text):
        """Convert miles to kilometres and update the output label."""
        try:
            miles = float(text)
            self.output_km = str(miles * MILES_TO_KM)
        except ValueError:
            self.output_km = "0.0"

    @staticmethod
    def validate_input(text):
        """Validate user input, assuming 0 if invalid."""
        try:
            return float(text)
        except ValueError:
            return 0.0

    def handle_increment(self, text, change):
        """Adjust the input value and recalculate the conversion."""
        miles = self.validate_input(text) + change
        self.root.ids.input_miles.text = str(miles)
        self.handle_conversion(str(miles))


ConvertMilesKmApp().run()

