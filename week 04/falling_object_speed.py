# #https://byui-cse.github.io/cse110-course/lesson04/teach.html
# 04 Teach: Team Activity
# Speed of a Falling Object

import math

mass = float(input("Mass (in kg): "))
gravity = float(input("Gravity in m/s²(9.8 on Earth or 24 on Jupiter): "))
time = float(input("Time (in seconds): "))
density = float(input("Density of the fluid in kg/m³ (1.3  for air or 1000 for water): ")) 
cross_sectional = float(input("Cross sectional area (in m²): "))
drag_constant =  float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))

c = (1/2)*density*cross_sectional*drag_constant

velocity_at_t = math.sqrt((mass *gravity) / c) * (1 - math.exp((-math.sqrt(mass*gravity*c) / mass)*time))
print("\n")
print(f"The inner value of c is: {c:.3f}")
print(f"The velocity after {time} seconds is: {velocity_at_t:.3f} m/s")