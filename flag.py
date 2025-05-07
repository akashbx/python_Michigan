import turtle
import time

class Star:
    def __init__(self, x, y, arm_length, color):
        self.x = x
        self.y = y
        self.arm_length = arm_length
        self.color = color.strip()

    def draw(self, t):
        t.penup()
        t.goto(self.x, self.y)
        t.setheading(-72)  # face left slightly
        t.pendown()
        t.color(self.color)
        t.begin_fill()
        for _ in range(5):
            t.forward(self.arm_length)
            t.right(144)
        t.end_fill()

    def __str__(self):
        return f"Star x:{self.x}, y:{self.y}, arm:{self.arm_length}, color:{self.color}"

class Rectangle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color.strip()

    def draw(self, t):
        t.penup()
        t.goto(self.x - self.width // 2, self.y + self.height // 2)
        t.setheading(0)
        t.pendown()
        t.color(self.color)
        t.begin_fill()
        for _ in range(2):
            t.forward(self.width)
            t.right(90)
            t.forward(self.height)
            t.right(90)
        t.end_fill()

    def __str__(self):
        return f"Rectangle x:{self.x}, y:{self.y}, width:{self.width}, height:{self.height}, color:{self.color}"

class Flag:
    def __init__(self, f_obj):
        self.rectangles = []
        self.stars = []
        
        rect_count = int(f_obj.readline())
        for _ in range(rect_count):
            line = f_obj.readline().strip()
            x, y, w, h, color = line.split(",")
            self.rectangles.append(Rectangle(int(x), int(y), int(w), int(h), color))

        star_count = int(f_obj.readline())
        for _ in range(star_count):
            line = f_obj.readline().strip()
            x, y, arm, color = line.split(",")
            self.stars.append(Star(int(x), int(y), int(arm), color))

    def draw(self, t):
        for r in self.rectangles:
            r.draw(t)
        for s in self.stars:
            s.draw(t)

    def __str__(self):
        result = "Rectangles\n"
        for r in self.rectangles:
            result += f"{r}\n"
        result += "Stars\n"
        for s in self.stars:
            result += f"{s}\n"
        return result.strip()
