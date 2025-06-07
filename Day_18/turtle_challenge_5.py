import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color =  (r, g, b)
    return color

tim.pensize(1)
tim.speed(20)

def draw_circle(angle):
    tim.color(random_color())
    tim.circle(100)
    tim.penup()
    tim.setheading(angle)
    tim.pendown()

for angle in range(0, 361, 5):
    draw_circle(angle)

screen = t.Screen()
screen.exitonclick()
