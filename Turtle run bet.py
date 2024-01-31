from turtle import Turtle, Screen, penup
import random


new_turtle = Turtle()
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet",
    prompt="Which turtle will win the race? Enter a color: ")
color = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtle = []

#Create 6 turtle objects 
for turtle_index in range(0, 6):
  new_turtle = Turtle(shape="turtle")
  new_turtle.color(color[turtle_index])
  new_turtle = penup()
  new_turtle.goto(x=-230, y=y_position[turtle_index])
  all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

  for turtle in all_turtle:
    if turtle.xcor() > 230:
      is_race_on = False 
      winning_color = turtle.pencolor()
      if winning_color == user_bet:
        print(f"You've won! The {winning_color} turtle is the winner!")
      else:
        print(f"You've lost! The {winning_color} turtle is the winner!")
# Make turtel move random
    rand_distance = random.randint(0, 10)
    turtle.forword(rand_distance)


screen.exitonclick()
