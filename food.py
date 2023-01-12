from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("red")
        self.penup()
        self.new_location()

    # Move object to a random location that is aligned with the snake
    def new_location(self):
        self.goto(x=random.randint(-14, 14) * 20, y=random.randint(-11, 11) * 20)
