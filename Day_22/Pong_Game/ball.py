from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        # Create the ball
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        #Basic math to invert the direction in x cor
        self.y_move *= -1
