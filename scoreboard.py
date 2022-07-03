from turtle import Turtle,Screen
import  time
import random

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt", mode="r") as score_file:
            self.high_score = int(score_file.read())
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0,280)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"S c o r e :-  {self.score}  |  High score :- {self.high_score}", align="center", font=("Arial", 13, "bold"))

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("highscore.txt",mode="w") as score_file:
                score_file.write(f"{self.high_score}")

        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align="center", font=("Arial", 13, "bold"))
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
