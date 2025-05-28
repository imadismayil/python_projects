from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.goto(0,260)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}",align=ALIGNMENT,font=FONT)

    def update_score(self):
        self.score += 1
        self.write_score()

    def end_game(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER! Final Score: {self.score}",align=ALIGNMENT,font=FONT)

