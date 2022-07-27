from time import sleep
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)
game_is_on = True
snake = []

def create_snake():
    n = 0
    for i in range(0, 3):
        snake_body = Turtle('square')
        snake_body.color('black', 'white')
        snake_body.setx(n)
        n -= 20
        snake.append(snake_body)

create_snake()
screen.update()


while game_is_on:
    for section in snake:
        section.fd(20)
    screen.update()
    sleep(1)

    
screen.exitonclick()