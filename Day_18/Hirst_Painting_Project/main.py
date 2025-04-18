import random
from colorsys import rgb_to_hls
import colorgram
import turtle as turtle_module
import random

# Extracting the colors from the selected image

# rgb_colors = []
# colors = colorgram.extract('daft_punk.jpg',6)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(9, 13, 15), (142, 160, 188), (205, 219, 236), (26, 20, 17), (250, 226, 120),(218, 158, 70) ]


tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list) )
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
