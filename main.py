from time import sleep
from turtle import Screen
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)
game_is_on = True
snake = []

snake = Snake()
snake.create()

screen.update()
snake_head = snake.get_snake_head()

screen.listen()
screen.onkey(key='a', fun=snake.turn_left)
screen.onkey(key='d', fun=snake.turn_right)


while game_is_on:
    sleep(0.3)
    screen.update()
    snake.move()


screen.exitonclick()