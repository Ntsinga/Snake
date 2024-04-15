"""Project 20&21:Snake game"""

from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

WALL = 290

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

"""screen.tracer puts a holt to the animation of objects on the screen"""
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

is_game_on = True
while is_game_on:
    """screen.update refreshes/redraws the screen after all animations have been carried out"""
    screen.update()
    """the time.sleep function is used to delay the next action for a given number of seconds"""
    time.sleep(0.1)
    
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update_score()

    # Detect collision with wall
    if snake.head.xcor() > WALL or snake.head.xcor() < -WALL - 10 or snake.head.ycor() > WALL + 15 or snake.head.ycor() < -WALL:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail

    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:
            # is_game_on = False
            # scoreboard.game_over()
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
