from turtle import Turtle, Screen
import random
is_race_true = False
screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "yellow", "purple", "chocolate4", "bisque3", "DarkGrey"]
turtles = []
for i in range(len(colors)):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-240, -80 + ((i + 1) * 30))
    turtles.append(new_turtle)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle would win the race?,Enter your color")
if user_bet:
    is_race_true = True

while is_race_true:
    for turtle in turtles:
        turtle_distance = random.randint(1,10)
        turtle.forward(turtle_distance)
        if turtle.xcor() >= 240:
            is_race_true = False
            winning_color = turtle.pencolor()
            if winning_color.lower() == user_bet.lower():
                print("You Win!")

            else:
                print("You Lose!")
            print("The winning color is: ", winning_color)


screen.exitonclick()
