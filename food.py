from turtle import Turtle
import random


class Food():

    def __init__(self):
        self.snack = Turtle('circle')
        self.snack.penup()
        self.snack.color('green')

    def randomize(self):
        x_cord = random.randint(-280, 280)
        y_cord = random.randint(-280, 280)
        self.snack.setposition(x_cord, y_cord)

    def get_position(self):
        return self.snack.pos()

    def hit_detection(self, snake):
        """ Function to check if the snake has 'eaten the food """

        # Define the x_axis and y_axis of the food location
        x_axis = self.get_position()[0]
        y_axis = self.get_position()[1]

        if (snake[0] - 10 <= x_axis <= (snake[0] + 10)
                and snake[1] - 10 <= y_axis <= snake[1] + 10):
            return True
