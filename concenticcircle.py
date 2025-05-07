# Drawing colorful concentric circles using Turtle Graphics

import turtle
import random
import time
import os

def is_valid_positive_integer(s):
    return s.isdigit() and int(s) > 0

def draw_colored_circles(num_circles, max_radius):
    step = max_radius / num_circles

    for i in range(num_circles, 0, -1):
        radius = i * step


        red = random.random()
        green = random.random()
        blue = random.random()
        turtle.color((red, green, blue))


        turtle.penup()
        turtle.goto(0, -radius)
        turtle.setheading(0)
        turtle.pendown()

        turtle.begin_fill()
        turtle.circle(radius)
        turtle.end_fill()

def main():
    print("This program draws colorful concentric circles using Turtle Graphics!")

    while True:
        num_str = input("Enter the number of circles (positive integer): ")
        if is_valid_positive_integer(num_str):
            num_circles = int(num_str)
            break
        else:
            print("Invalid input! Please enter a positive integer.")

    while True:
        radius_str = input("Enter the maximum radius (positive integer): ")
        if is_valid_positive_integer(radius_str):
            max_radius = int(radius_str)
            break
        else:
            print("Invalid input! Please enter a positive integer.")

    turtle.colormode(1.0)
    turtle.speed(0)
    turtle.bgcolor("black")

    draw_colored_circles(num_circles, max_radius)

    time.sleep(5)
    os._exit(0)

main()