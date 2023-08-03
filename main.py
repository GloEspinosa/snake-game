from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

END_SCREEN = 290

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
# .bgcolor() changes background color
screen.title("Snake Game")
screen.tracer(0)
# .tracer() y .update()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

game_on = True

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# TODO 2. Move the snake

while game_on:
    screen.update()
    time.sleep(0.1)
    # for square in snake:
    #     square.forward(20)
    snake.move()


# TODO 4. Detect collision with food
# TODO 5. Scoreboard tracking

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

# TODO 6. Detect collision with wall (Game Over.)
# TODO 7. Detect collision with tail (Game Over.)

    if snake.head.xcor() > END_SCREEN or snake.head.xcor() < -END_SCREEN or snake.head.ycor() > END_SCREEN \
            or snake.head.ycor() < -END_SCREEN:
        scoreboard.reset()
        snake.reset()
        # game_on = False
        # scoreboard.game_over()

    for segment in snake.segments[1:]:
        # if segment == snake.head:
        #     pass
        # elif snake.head.distance(segment) < 10:
        #     game_on = False
        #     scoreboard.game_over()
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            # game_on = False
            # scoreboard.game_over()


screen.exitonclick()
