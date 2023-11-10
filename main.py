from snake import Snake
from food import Food
from scoreboard import Scoreboard
from turtle import Screen
import time

# Setting up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # This prevents the animation of the piece by piece being formed and move to its spot
screen.listen()
food = Food()
snake = Snake()  # This here is our snake object and invoking it makes our snake segment appear on screen
scoreboard = Scoreboard()
# The actual game. The main page should control the snake movement
# Below is what allow for user to control the snake

screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Down", fun=snake.move_down)
screen.onkey(key="Right", fun=snake.move_right)
screen.onkey(key="Left", fun=snake.move_left)


snake_game = True

while snake_game:
    screen.update()  # Updates the screen, so now we can now see the full snake in all of its piece together
    time.sleep(0.1)  # delay execution by 0.1 second
    snake.move()     # after 0.1 second the snake moves
    if snake.snake[0].distance(food) < 15:
        # If the snake is within 15 pixel of the food, it has eaten the food
        food.refresh()
        snake.grow_size()
        scoreboard.calculate_score()
    if snake.snake[0].xcor() > 290 or snake.snake[0].xcor() < -290 or \
            snake.snake[0].ycor() > 290 or snake.snake[0].ycor() < -290:
        scoreboard.game_over()
        snake_game = False
    for segments in snake.snake[1:]:
        # From index 1 to length of snake - 1.
        # Start off at 1 because 0 is our head
        if snake.snake[0].distance(segments) < 10:
            scoreboard.game_over()
            snake_game = False

screen.exitonclick()
