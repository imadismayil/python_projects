from turtle import Turtle

class DashedLine(Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor('white')
        self.hideturtle()
        self.penup()
        self.goto(0,-280)

    def draw(self):
        while True:
            self.pendown()
            self.setheading(90)
            self.forward(20)
            self.penup()
            self.forward(20)

            if self.ycor() > 280:
                break
