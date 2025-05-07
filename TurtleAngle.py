# Description: Draws 2 lines using turtle graphics and calculates the acute angle between them.

import turtle
import math

def get_point(prompt):
    """Prompts the user for a coordinate."""
    return float(input(prompt))

print("Welcome to the Turtle Angle Calculator!")
print("This program draws two lines and calculates the acute angle between them.\n")

x1 = get_point("Enter x-coordinate of Point 1: ")
y1 = get_point("Enter y-coordinate of Point 1: ")
x2 = get_point("Enter x-coordinate of Point 2: ")
y2 = get_point("Enter y-coordinate of Point 2: ")



try:
    m1 = y1 / x1
except ZeroDivisionError:
    m1 = float('inf')

try:
    m2 = (y2 - y1) / (x2 - x1)
except ZeroDivisionError:
    m2 = float('inf')

if m1 == m2:
    angle_radians = 0.0
elif math.isinf(m1) and math.isinf(m2):
    angle_radians = 0.0
elif math.isinf(m1) or math.isinf(m2):
    angle_radians = math.pi / 2 
else:
    angle_radians = math.atan(abs((m2 - m1) / (1 + m1 * m2)))

angle_degrees = angle_radians * 180 / math.pi
print(f"The acute angle between the two lines is: {angle_degrees:.2f} degrees")

turtle.goto(x1, y1)           
turtle.goto(x2, y2)           
turtle.write(f"{angle_degrees:.2f}°")  
turtle.done()                 
