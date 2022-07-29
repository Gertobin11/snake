from time import sleep
from turtle import Screen
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)
game_is_on = True

snake = Snake()
food = Food()
food.randomize()
print(food.get_position())

def hit_detection(snake, food):
    print(snake)
    if (snake[0] -10) <= food[0] <= (snake[0] + 10) and (snake[0] -10) <= food[0] <= (snake[0] + 10):
        print('hit')

screen.update()
snake_head = snake.get_snake_head()
snake_hit = snake.get_head_location()
print(snake_hit)
food_location = food.get_position()
print(food_location)

screen.listen()
screen.onkey(key='Left', fun=snake.turn_left)
screen.onkey(key='Right', fun=snake.turn_right)
screen.onkey(key='Up', fun=snake.turn_up)
screen.onkey(key='Down', fun=snake.turn_down)


while game_is_on:
    sleep(0.1)
    screen.update()
    snake.move()
    snake_head = snake.get_snake_head()
    snake_hit = snake.get_head_location()
    hit_detection(snake=snake_hit, food=food_location)


screen.exitonclick()