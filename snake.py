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
        return self.get_snake_head().forward(20)

    def turn_left(self):
        if self.get_snake_head().heading() != 0:
            return self.get_snake_head().setheading(180)

    def turn_right(self):
        if self.get_snake_head().heading() != 180:
            return self.get_snake_head().setheading(0)

    def turn_up(self):
        if self.get_snake_head().heading() != 270:
            return self.get_snake_head().setheading(90)

    def turn_down(self):
        if self.get_snake_head().heading() != 90:
            return self.get_snake_head().setheading(270)

    def get_head_location(self):
        return self.get_snake_head().position()

    def add_body_segment(self):
        new_segment = Turtle('square')
        new_segment.color('black', 'white')
        last_segment_pos = self.body[-1].pos()
        new_segment.setposition(last_segment_pos)
        return self.body.append(new_segment)

    def check_snake_hit_self(self):
        """
        Method to check if the snake head touches
        any section of the snake
        """
        for i in range(1, len(self.body)):
            if self.body[i].position() == self.get_head_location():
                print('exit   self    hit')
                return True

    def check_border_hit(self):
        """ Method to check if the snake head goes outside the border """

        # Get the location of the head on the x and y axis
        x_axis = self.get_head_location()[0]
        y_axis = self.get_head_location()[1]

        # Return True if the snakehead exceeds the screen
        if -290 > x_axis or x_axis > 290:
            return True
        elif -290 > y_axis or y_axis > 290:
            return True
