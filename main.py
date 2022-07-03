from turtle import Turtle,Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width= 600, height= 600)
screen.bgcolor("black")
screen.title("Buss Buss Naginn")
screen.tracer(0)
snake = Snake() # Snake sn();
food = Food() # Food fd();
scoree = Score() # Score sc();
screen.listen() #Listen lst();
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoree.increase_score()


    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoree.reset()
        snake.reset()

    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            scoree.reset()
            snake.reset()

screen.exitonclick()