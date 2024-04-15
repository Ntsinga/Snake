from turtle import Turtle

FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.highest_score = self.get_highscore()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(-50, 270)
        self.write(f"Score:{self.score}", move=False, align="center", font=FONT)
        self.goto(80, 270)
        self.write(f"HighScore:{self.highest_score}", move=False, align="center", font=FONT)

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            self.update_highscore()
        self.score = 0
        self.write_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER",align="center",)

    def update_score(self):
        self.score += 1
        self.write_score()

    def get_highscore(self):
        with open("data.txt") as file:
            contents = file.read()
            self.highest_score = int(contents)
            return self.highest_score

    def update_highscore(self):
        with open("data.txt", mode="w") as file:
            file.write(f"{self.highest_score}")
