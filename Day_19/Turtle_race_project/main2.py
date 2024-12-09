from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="Which turtle will win the race? enter a color: ")


tim = Turtle()
tim.goto(-235, 0)


screen.exitonclick()
