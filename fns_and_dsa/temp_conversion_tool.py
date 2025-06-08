# -*- coding: utf-8 -*- 
# Global conversion factors 
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9 
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5 
 
def convert_to_celsius(fahrenheit): 
    """Convert Fahrenheit to Celsius using global factor""" 
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR 
    return celsius 
 
def convert_to_fahrenheit(celsius): 
    """Convert Celsius to Fahrenheit using global factor""" 
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32 
    return fahrenheit 
 
def main(): 
    """Main function to handle user interaction""" 
    try: 
        temp = float(input("Enter the temperature to convert: ")) 
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper() 
 
        if unit == 'F': 
            converted = convert_to_celsius(temp) 
            print(f"{temp} degrees F is {converted} degrees C") 
        elif unit == 'C': 
            converted = convert_to_fahrenheit(temp) 
            print(f"{temp} degrees C is {converted} degrees F") 
        else: 
            print("Invalid unit. Please enter 'C' or 'F'.") 
    except ValueError: 
        print("Invalid temperature. Please enter a numeric value.") 
 
if __name__ == "__main__": 
    main() 
