from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

food = Food()
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

score = ScoreBoard()
snake = Snake()
screen.listen()
screen.onkey(key="Up", fun=snake.Up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
game_is_on = True

while game_is_on:

    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh_food_location()
        snake.extend()
        score.increase_score()

    snake_x = snake.head.xcor()
    snake_y = snake.head.ycor()
    # detect collision with walls
    if snake_x < -280 or snake_x > 280 or snake_y < -280 or snake_y > 280:
        score.reset()
        snake.reset()

    # detect collision with tail

    for segment in snake.segments[1:]:  # list slicing
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()
