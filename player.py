from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.penup()
        self.setpos(0, -280)

    def move_forward(self):
        self.forward(20)

    def move_backward(self):
        self.backward(20)

    def level_up(self):
        self.setpos(0, -280)


