from turtle import Turtle
import random


class Food(Turtle):
    """The Food class used to create a food object for the snake to eat"""
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # creates a 10 x 10 circle
        self.color("green")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Refresh the food random location"""
        self.goto(x=random.randint(-280, 280), y=random.randint(-280, 280))




