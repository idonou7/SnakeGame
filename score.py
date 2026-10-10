from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=-1
        self.color("white")
        self.speed("fastest")
        self.hideturtle()
        self.penup()
        self.cplusplus()
    def cplusplus(self):
        self.score+=1
        self.clear()
        self.teleport(x=0, y=275)
        self.write(f"SCORE: {self.score}", True, align="center", font=('Courier', 15, "normal"))

    def game_over(self):
        self.teleport(0,0)
        self.write(f"GAME OVER", True, align="center", font=('Courier', 30, "normal"))