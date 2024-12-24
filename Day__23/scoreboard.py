from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.update_scoreboard()
        self.game_is_on = False


    def update_scoreboard(self):
        self.clear()
        self.goto(0, 250)
        self.write(f"Level: {self.level}", align="center", font=FONT)
    def increase_level(self):
        self.level +=1
        self.update_scoreboard()

    def game_over(self):
        self.game_is_on = False
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)
