# import colorgram
# color =[]
# new_colors = colorgram.extract("hirst_image.jpg", 12)
#
# for colr in new_colors:
#     r = colr.rgb.r
#     g = colr.rgb.g
#     b = colr.rgb.b
#     new_color = (r, g, b)
#     color.append(new_color)
#
# print(color)
import random
import turtle
from turtle import Turtle, Screen

colors =[(197, 13, 32), (249, 237, 21), (39, 77, 188), (238, 227, 5),
 (39, 216, 68), (228, 160, 47), (28, 40, 155), (214, 75, 14)]

timmy = Turtle()
timmy.shape("turtle")
timmy.hideturtle()
timmy.penup()
timmy.speed("fastest")
turtle.colormode(255)
timmy.setheading(180+45)
timmy.forward(260)
timmy.left(45+90)


for dots in range(1,101):
    timmy.dot(30 , random.choice(colors))
    timmy.forward(50)
    if dots % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

screen = turtle.TurtleScreen
Screen().exitonclick()
