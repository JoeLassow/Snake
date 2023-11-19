from turtle import Turtle


ALIGN = "center"
FONT = ("Courier", 18, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as DATA:
            self.high_score = int(DATA.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align=ALIGN, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score}  High Score: {self.high_score}", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as DATA:
                DATA.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


