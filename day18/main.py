#from turtle import *
import turtle as t
import random

tim = t.Turtle()

# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "LightSeaGreen", "wheat"]
# t.colormode(255)
#
# # def draw_shape(num_sides):
# #     pit = 360 / num_sides
# #     for _ in range(num_sides):
# #         tim.forward(100)
# #         tim.right(pit)
# #
# # for shape_side_n in range(3, 11):
# #     draw_shape(shape_side_n)
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color
#
# direction = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")
#
#
# for _ in range(2000):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(direction))

#Circle

t.colormode(255)

def random_color():
     r = random.randint(0, 255)
     g = random.randint(0, 255)
     b = random.randint(0, 255)
     random_color = (r, g, b)
     return random_color

tim.speed("fastest")

def draw_spiograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + 10)
draw_spiograph(5)

screen = t.Screen()
screen.exitonclick()
