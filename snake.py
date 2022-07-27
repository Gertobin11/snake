from turtle import Turtle

class Snake():

    def __init__(self):
        self.body = []
        n = 0
        for i in range(0, 3):
            snake_body = Turtle('square')
            snake_body.color('black', 'white')
            snake_body.setx(n)
            n -= 20
            self.body.append(snake_body)

    def get_snake_head(self):
        return self.body[0]

    def move(self):
        for seg_num in range(len(self.body) - 1, 0, -1):
            cords = self.body[seg_num - 1].pos()
            self.body[seg_num].goto(cords)
        self.get_snake_head().forward(20)

    def turn_left(self):
        self.get_snake_head().left(90)

    def turn_right(self):
        self.get_snake_head().right(90)
