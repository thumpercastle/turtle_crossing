from turtle import Turtle
import random

colors = ["black", "blue", "green", "red", "yellow", "purple", "pink", "orange"]

class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(180)
        self.shape("square")
        self.setpos(280, random.randint(-250, 250))
        self.color(random.choice(colors))
        self.shapesize(stretch_len=3)

    def move(self):
        self.forward(20)

