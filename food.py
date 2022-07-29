from turtle import Turtle
import random

class Food():
    
    def __init__(self):
        self.snack = Turtle('circle')
        self.snack.penup()
        self.snack.color('green')

    def randomize(self):
        x_cord = random.randint(-300, 300)
        y_cord = random.randint(-300, 300)
        self.snack.setposition(x_cord, y_cord)
    
    def get_position(self):
        return self.snack.pos()