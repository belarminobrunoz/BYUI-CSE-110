#Program created by Bruno Belarmino

# Assignment: Write a program to convert from Fahrenheit to Celsius. Display the result to one decimal place of precision.
# To convert degrees in Fahrenheit to Celsius you need to subtract 32 from the Fahrenheit amount and then multiply it by the fraction 5/9.

#Welcome
print("*" * 30)
print("Welcome to Temperature Unit Conversion Program!")
print("*" * 30)

#Input
temp_fahrenheit = int(input("What's the temperature in Fahrenheit? "))
print("Thank you!")
temp_celsius = (temp_fahrenheit - 32) * (5 / 9)
print(f"Doing the calculations, I found out that {temp_fahrenheit:.1f} fahrenheit is the same as {temp_celsius:.1f} celsius")