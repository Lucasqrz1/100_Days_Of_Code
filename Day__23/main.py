import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

level = 0

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title(f"Level: {level}")

turtle = Turtle()
turtle.color("Black")
turtle.shape("turtle")
turtle.setheading(90)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

screen.onkey(turtle.up, "Up")
