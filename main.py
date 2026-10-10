from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Serpulea")
screen.tracer(0)
on=True
screen.update()
snake=Snake()
food=Food()
score=Score()
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.left, key="Left")

while on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.snake[0].distance(food)<5:
        food.refresh()
        score.cplusplus()
        snake.sizeplusplus()
    if snake.snake[0].xcor()>280 or snake.snake[0].xcor()<-300 or snake.snake[0].ycor()>280 or snake.snake[0].ycor()<-280:
        score.game_over()
        on=False
    for i in snake.snake[1:]:
        if snake.snake[0].distance(i)<10:
            on=False
    screen.update()

screen.exitonclick()