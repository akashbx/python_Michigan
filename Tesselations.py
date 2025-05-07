# Tessellation of hexagons using turtle graphics

import turtle
import math

VALID_COLORS = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink']
CANVAS_SIZE = 500

def get_color_choice():
    print("Choices for colors to use are:")
    for color in VALID_COLORS:
        print(" ", color)
    while True:
        choice = input("Please enter your choice: ").strip().lower()
        if choice in VALID_COLORS:
            return choice
        print(f"'{choice}' is not a legal choice. Please try again:")

def get_num_hexagons():
    while True:
        try:
            n = int(input("Please enter the number of hexagons per row (4–20): "))
            if 4 <= n <= 20:
                return n
            else:
                print("It should be between 4 and 20. Please try again:")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def draw_hexagon(x, y, side_len, pen, color):
    pen.penup()
    angle = math.radians(60)
    pen.goto(x, y)
    pen.fillcolor(color)
    pen.begin_fill()
    pen.setheading(0)
    pen.forward(side_len)
    pen.pendown()
    for _ in range(6):
        pen.left(60)
        pen.forward(side_len)
    pen.end_fill()

def main():
    turtle.setup(CANVAS_SIZE, CANVAS_SIZE)
    pen = turtle.Turtle()
    pen.speed(0)
    pen.hideturtle()

    color1 = get_color_choice()
    color2 = get_color_choice()
    num_hex = get_num_hexagons()
    side = CANVAS_SIZE / num_hex
    height = math.sin(math.radians(60)) * side

    start_x = -CANVAS_SIZE / 2 + side / 2
    start_y = -CANVAS_SIZE / 2 + height / 2

    for row in range(num_hex):
        for col in range(num_hex):
            x_shift = side * col + (row % 2) * (side / 2)
            x = start_x + x_shift
            y = start_y + row * height
            color = color1 if (row + col) % 2 == 0 else color2
            draw_hexagon(x, y, side, pen, color)

    turtle.done()

if __name__ == "__main__":
    main()