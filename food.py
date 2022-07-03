import random
import turtle
from turtle import Turtle,Screen
import time
# screen = Screen()
# screen.tracer(0)
# foodie = Turtle()
# foodie.turtlesize(0.5,0.5)
# foodie.penup()
# foodie.shape("triangle")
# foodie.color("blue")
# for i in range(0, 4):
#     x_cor = random.choice(range(-280, 281))
#     y_cor = random.choice(range(-280, 281))
#     foodie.goto(x_cor , y_cor)
#     screen.update()
#     time.sleep(1)
# turtle.exitonclick()
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.turtlesize(0.5,0.5)
        self.refresh()

    def refresh(self):
        x_cor = random.choice(range(-280, 281))
        y_cor = random.choice(range(-280, 281))
        self.goto(x_cor, y_cor)