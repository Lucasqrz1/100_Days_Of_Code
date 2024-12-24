import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

level = 0
#screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing Game")

car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect if player has reached the other side
    if player.is_at_finish():
       player.go_to_start()
       car_manager.increase_speed()
       scoreboard.increase_level()

screen.exitonclick()



