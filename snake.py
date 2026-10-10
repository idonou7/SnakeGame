from turtle import Turtle
import random
MOVE_D=20
START_POS=0
class Snake():
    def __init__(self):
        self.snake = []
        self.size=3
        for i in range(0, self.size):
            self.snake.append(Turtle(shape="square"))
            self.snake[i].penup()
            self.snake[i].color(random.random(), random.random(), random.random())
            self.snake[i].setx(START_POS - i * 20)
    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            x = self.snake[i - 1].xcor()
            y = self.snake[i - 1].ycor()
            self.snake[i].goto(x, y)
        self.snake[0].forward(MOVE_D)
    def up(self):
        if self.snake[0].heading()==0 or self.snake[0].heading()==180:
            self.snake[0].setheading(90)
    def down(self):
        if self.snake[0].heading()==0 or self.snake[0].heading()==180:
            self.snake[0].setheading(270)
    def left(self):
        if self.snake[0].heading()==90 or self.snake[0].heading()==270:
            self.snake[0].setheading(180)
    def right(self):
        if self.snake[0].heading()==90 or self.snake[0].heading()==270:
            self.snake[0].setheading(0)
    def sizeplusplus(self):
        self.snake.append(Turtle(shape="square"))
        self.snake[self.size].penup()
        self.snake[self.size].color(random.random(), random.random(), random.random())
        self.snake[self.size].setpos(x=self.snake[self.size-1].xcor(), y=self.snake[self.size-1].ycor())
        self.size+=1