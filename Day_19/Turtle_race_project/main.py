from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.shape("turtle")
tim.color("purple")

def move_forwards():
    tim.forward(10)

#Create the function with the given 'onkey' arguments:
def move_backwards():
    tim.backward(10)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
#def jump():
    tim.penup()
    tim.forward(20)
    tim.pendown()

num = []
for i in range (10):
    num.append(tim)


screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(move_backwards, "s")
screen.onkey(jump, "space")
screen.exitonclick()
