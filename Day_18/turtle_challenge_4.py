import turtle as t
import random

tim = t.Turtle()
tim.shape("arrow")

colors = ["spring green", "green yellow","orange", "magenta", "darkviolet", "pink","blue", "black", "grey"]
moves = [0,90,180,270]
tim.pensize(15)
tim.speed(10)

for _ in range(100):
    tim.color(random.choice(colors))
    tim.forward(50)
    tim.setheading(random.choice(moves))
