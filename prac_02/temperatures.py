def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

temperature = float(input("Enter the temperature: "))
conversion_type = input("Convert to (C)elsius or (F)ahrenheit? ").strip().upper()

if conversion_type == "F":
    print(f"{temperature}°C is {celsius_to_fahrenheit(temperature):.2f}°F")
elif conversion_type == "C":
    print(f"{temperature}°F is {fahrenheit_to_celsius(temperature):.2f}°C")
else:
    print("Invalid choice.")
