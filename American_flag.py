# Draw the American Flag using Turtle Graphics

import turtle

def get_color(color):
    if color == "red":
        return 178/255, 34/255, 52/255
    elif color == "white":
        return 1, 1, 1
    elif color == "blue":
        return 60/255, 59/255, 110/255
    else:
        return 0, 0, 0

def draw_rectangle(length, height, color):
    r, g, b = get_color(color)
    turtle.color((r, g, b))
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

def draw_star(size, color):
    r, g, b = get_color(color)
    turtle.color((r, g, b))
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)
    turtle.end_fill()

def draw_flag(height):
    turtle.speed(100)
    turtle.colormode(1.0)
    width = 1.9 * height
    stripe_height = height / 13
    union_height = stripe_height * 7
    union_width = width * 0.4
    star_size = stripe_height * 0.6
    h_gap = union_width / 12
    v_gap = union_height / 10

    # Draw stripes
    turtle.penup()
    turtle.goto(-width/2, height/2)
    for i in range(13):
        turtle.pendown()
        draw_rectangle(width, stripe_height, "red" if i % 2 == 0 else "white")
        turtle.penup()
        turtle.right(90)
        turtle.forward(stripe_height)
        turtle.left(90)

    # Draw blue union
    turtle.goto(-width/2, height/2)
    turtle.pendown()
    draw_rectangle(union_width, union_height, "blue")
    turtle.penup()

    # Draw stars
    start_x = -width/2 + h_gap
    start_y = height/2 - v_gap
    for row in range(9):
        num_stars = 6 if row % 2 == 0 else 5
        x = start_x if row % 2 == 0 else start_x + h_gap
        y = start_y - row * v_gap
        for _ in range(num_stars):
            turtle.goto(x, y)
            turtle.setheading(0)
            turtle.pendown()
            draw_star(star_size / 3, "white")
            turtle.penup()
            x += 2 * h_gap

def main():
    draw_flag(260)
    turtle.hideturtle()
    turtle.done()

main()
