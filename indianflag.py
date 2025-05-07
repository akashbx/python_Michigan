# indian_flag.py
# Draw the Indian Flag using Turtle Graphics

import turtle

def draw_rectangle(width, height, color):
    turtle.begin_fill()
    turtle.fillcolor(color)
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

def draw_chakra(radius):
    turtle.penup()
    turtle.goto(0, -radius)
    turtle.setheading(0)
    turtle.pendown()
    turtle.color("blue")
    turtle.pensize(2)
    turtle.circle(radius)
    
    # Draw 24 spokes
    for i in range(24):
        turtle.penup()
        turtle.goto(0, 0)
        turtle.setheading(i * 15)
        turtle.pendown()
        turtle.forward(radius)

def draw_flag(height):
    width = 1.5 * height
    stripe_height = height / 3

    turtle.speed(100)
    turtle.penup()
    turtle.goto(-width / 2, height / 2)
    turtle.setheading(0)

    # Saffron stripe
    turtle.pendown()
    draw_rectangle(width, stripe_height, "#FF9933")  # Saffron
    turtle.right(90)
    turtle.forward(stripe_height)

    # White stripe
    turtle.left(90)
    draw_rectangle(width, stripe_height, "white")
    turtle.right(90)
    turtle.forward(stripe_height)

    # Green stripe
    turtle.left(90)
    draw_rectangle(width, stripe_height, "#138808")  # Green

    # Draw the Ashoka Chakra
    turtle.penup()
    turtle.goto(0, stripe_height / 2)
    turtle.setheading(0)
    draw_chakra(stripe_height / 2.5)

def main():
    turtle.bgcolor("white")
    draw_flag(300)
    turtle.hideturtle()
    turtle.done()

main()
