#Temperature Converter
def celsius_to_fahrenheit(celsius):
  
  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit

temp_celsius = float(input("Enter temperature in Celsius: "))

converted_fahrenheit = celsius_to_fahrenheit(temp_celsius)

print(f"{temp_celsius} degrees Celsius is equal to {converted_fahrenheit:.2f} degrees Fahrenheit")