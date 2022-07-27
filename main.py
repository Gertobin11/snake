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

screen.update()
snake_head = snake.get_snake_head()

screen.listen()
screen.onkey(key='Left', fun=snake.turn_left)
screen.onkey(key='Right', fun=snake.turn_right)
screen.onkey(key='Up', fun=snake.turn_up)
screen.onkey(key='Down', fun=snake.turn_down)


while game_is_on:
    sleep(0.3)
    screen.update()
    snake.move()


screen.exitonclick()