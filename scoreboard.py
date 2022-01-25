from turtle import Turtle, Screen

ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")
screen = Screen()


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.color("white")
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.final_score = int()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", align=ALIGNMENT, font=FONT)
        self.goto(0, -22)
        self.write(f"Your score was {self.final_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=("Arial", 16, "normal"))
        if self.final_score < self.score:
            self.final_score = self.score

    def print_score(self):
        print(self.final_score)
