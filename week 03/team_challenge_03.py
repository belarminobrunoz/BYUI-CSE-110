import math
length_square = float(input('What is the length of a side of the square in centimeters? '))
square_centimeters = length_square ** 2
square_meters = square_centimeters / 10000
print(f'The area of the square in square centimeters is : {square_centimeters}')
print(f'The area of square in square meters is: {square_meters}')
length_rectangle = float(input('What is the length of rectangle in centimeters? '))
width_rectangle = float(input('What is the width of rectangle in centimeters? '))
rectangle_centimeters = length_rectangle * width_rectangle
rectangle_meters = rectangle_centimeters / 10000
print(f'The area of the rectangle in square centimeters is: {rectangle_centimeters}')
print(f'The area of rectangle in square meters is: {rectangle_meters}')
radius = float(input('What is the radius of the circle in centimeters? '))
circle_centimeters = math.pi * (radius ** 2)
circle_meters = circle_centimeters / 10000
print(f'The area of the circle in square centimeters is: {circle_centimeters}')
print(f'The area of the circle in square meters is: {circle_meters}')
()
# value = float(input('Enter a value: '))
# sqr_area = value ** 2
# cir_area = math.pi * (value ** 2)
# cube_volume = value ** 3
# sphere_volume = 4/3 * (math.pi * (value ** 3))
# print(f'The area of square is: {sqr_area}')
# print(f'The are of circle is: {cir_area}')
# print(f'The volume of cube is: {cube_volume}')
# print(f'The volume of sphere is: {sphere_volume}')


# The stretch challenges for this activity are:
# https://byui-cse.github.io/cse110-course/lesson03/teach.html
# OOOOOK! -  Instead of using 3.14 for your value of Pi, see if you can find and use the built-in value of Pi included in the python "math" module. Hint, you might try searching on the internet for something like, "python how to get the value of pi."

# Prompt the user for a single length value, then compute and display the areas of a square with that length of side, a circle with that radius, and then the volumes of a cube with that side and a sphere with that radius, all from the same value from the user.

# receives a single length value, then compute and display 
# -> the areas of a square with that length of side, 
# -> a circle with that radius
# -> the volumes of a cube with that side 
# -> a sphere with that radius

# For each of the three areas in the core requirements, change the prompt for the user to ask for the value in centimeters. Then, display the resulting area in both square centimeters and square meters. Keep in mind that a centimeter is 1/100 of a meter, and a square centimeter is 1/10,000 of a square meter.