from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()


screen.listen()
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 300 or ball.ycor() < -300:
        #Needs to bounce
        ball.bounce()
    #Detect collision with Paddle
#(Turn this into a class def
    if ball.distance(r_paddle) < 10) or ball.distance(l_paddle) < 10: 
        ball.move() *=  -1

screen.exitonclick()
