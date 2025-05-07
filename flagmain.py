import turtle
import time
from flag import Flag

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")
    pen = turtle.Turtle()
    pen.speed("fastest")
    pen.hideturtle()

    with open("panama.txt") as file:
        flag = Flag(file)
        print(flag)
        flag.draw(pen)

    time.sleep(5)
    turtle.bye()

if __name__ == "__main__":
    main()
