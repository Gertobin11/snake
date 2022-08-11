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
score = 0

screen.update()
snake_head = snake.get_snake_head()
snake_hit = snake.get_head_location()
print(snake_hit)


def play_again():
    """ Reset the Board so the player can play the game again """
    global score
    global food
    global snake
    replay = (screen.textinput(prompt='Play again? Y or N: ',
              title=f'You scored {score} points'))
    if replay.lower() == 'y':
        for turtle in screen.turtles():
            turtle.reset()
        food = Food()
        food.randomize()
        snake = Snake()
        score = 0
    elif replay.lower() == 'n':
        exit()
    else:
        play_again()


while game_is_on:
    # Allow the user to move the snake with the directional buttons
    screen.listen()
    screen.onkey(key='Left', fun=snake.turn_left)
    screen.onkey(key='Right', fun=snake.turn_right)
    screen.onkey(key='Up', fun=snake.turn_up)
    screen.onkey(key='Down', fun=snake.turn_down)

    sleep(0.08)
    screen.update()
    screen.title(f"Score : {score}")
    snake.move()
    snake_head = snake.get_snake_head()
    snake_hit = snake.get_head_location()
    if food.hit_detection(snake=snake_hit):
        food.randomize()
        snake.add_body_segment()
        score += 9
    if snake.check_snake_hit_self():
        play_again()
    if snake.check_border_hit():
        play_again()

screen.exitonclick()
