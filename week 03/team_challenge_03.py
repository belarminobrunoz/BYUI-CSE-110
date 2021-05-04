# Import math Library
import math

sqr_length = float(input("What is the length of a side of the square? "))
sqr_area = sqr_length*sqr_length
print(f"The area of the square is: {sqr_area}")

print("\n***************************************************************\n")

rec_length  = float(input("What is the length of rectangle? "))
rec_width = float(input("What is the width of the rectangle? "))
rec_area = rec_length*rec_width
print(f"The area of the rectangle is: {rec_area}")

print("\n***************************************************************\n")

rad_circle = float(input("5 What is the radius of the circle? "))
cir_area = math.pi * (rad_circle**2)
print(f"The area of the circle is: {cir_area}")


# The stretch challenges for this activity are:
# https://byui-cse.github.io/cse110-course/lesson03/teach.html
# OOOOOK! -  Instead of using 3.14 for your value of Pi, see if you can find and use the built-in value of Pi included in the python "math" module. Hint, you might try searching on the internet for something like, "python how to get the value of pi."

# Prompt the user for a single length value, then compute and display the areas of a square with that length of side, a circle with that radius, and then the volumes of a cube with that side and a sphere with that radius, all from the same value from the user.

# For each of the three areas in the core requirements, change the prompt for the user to ask for the value in centimeters. Then, display the resulting area in both square centimeters and square meters. Keep in mind that a centimeter is 1/100 of a meter, and a square centimeter is 1/10,000 of a square meter.