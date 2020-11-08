from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.setpos(-280, -280)
        self.level = 1
        self.hideturtle()
        self.write(f"Level: {self.level}", align="Left", font=("Courier", 12, "normal"))

    def level_up(self):
        self.level += 1

    def refresh(self):
        self.clear()
        self.setpos(-280, -280)
        self.write(f"Level: {self.level}", align="Left", font=("Courier", 12, "normal"))

    def game_over(self):
        self.setpos(0, 0)
        self.write(f"Game over\nYou reached level: {self.level}", align="Left", font=("Courier", 12, "normal"))