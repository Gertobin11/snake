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
snake_head = snake[0]

def turn_left():
    snake_head.left(90)

def turn_right():
    snake_head.right(90)

screen.listen()
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='d', fun=turn_right)


while game_is_on:
    sleep(0.3)
    screen.update()
    for seg_num in range(len(snake) - 1, 0, -1):
        cords = snake[seg_num - 1].pos()
        snake[seg_num].goto(cords)
    snake_head.forward(20)


screen.listen()
screen.onkey(key='w', fun=turn_left)
    
screen.exitonclick()