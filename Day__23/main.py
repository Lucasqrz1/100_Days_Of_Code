import time
from player import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

level = 0

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title(f"Level: {level}")

car = CarManager()
#player = Player()
#scoreboard = Scoreboard()

player = Turtle()
player.color("Black")
player.shape("turtle")
player.setheading(90)
player.penup()
player.goto(0, -270)


def move_up(): player.forward(15)

screen.listen()
screen.onkey(move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()
    # Detect collision with car
    for car in car.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            #scoreboard.game_over()
    # Detect if player has reached the other side
    if player.is_at_finish_line():
        player.go_to_start()
        car.increase_speed()
        #scoreboard.increase_level()

screen.exitonclick()



