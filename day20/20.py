# from turtle import Screen, Turtle
# import time
#
# screen = Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor("black")
# screen.title("My Snake Game")
# screen.tracer(0)
#
# starting_position = [(0, 0), (-20, 0), (-40, 0)]
#
# segments = []
#
# for position in starting_position:
#     new_segment = Turtle("square")
#     new_segment.color("blue")
#     new_segment.penup()
#     new_segment.goto(position)
#     segments.append(new_segment)
#
# game_is_on = True
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)
#
#     for seg_num in range(len(segments) - 1, 0, -1):
#         new_x = segments[seg_num - 1].xcor()
#         new_y = segments[seg_num - 1].ycor()
#         segments[seg_num].goto(new_x, new_y)
#     segments[0].forward(20)

from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score import Scoreboard
import time

#display igri
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()#activiruet class Snake
food = Food()
score = Scoreboard()

#chast za dvij

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

#zapusk igri
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)#skorost dvij
    snake.move()


    #Otvechaet za sedenie edi
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    #stena
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.rest()
        snake.reset()
        #game_is_on = False upgrade
        #score.game_over() upgrade


    #zakanchivaet igru stolknoveniem soboy
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            score.rest()
            snake.reset()
            #game_is_on = False upgrade
            #score.game_over() upgrade

screen.exitonclick()