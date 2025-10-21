from turtle import Turtle, Screen
import random
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
COLLISION_WITH_FOOD=15

def snake_game():
    s_screen = Screen()
    s_screen.setup(width=600, height=600)
    s_screen.bgcolor('black')
    s_screen.title("Snake Game")
    snake_obj=Snake(s_screen)
    food_obj=Food(s_screen)
    score_board_obj=ScoreBoard(s_screen)
    s_screen.listen()
    s_screen.onkey(fun=snake_obj.up,key="Up")
    s_screen.onkey(fun=snake_obj.down,key="Down")
    s_screen.onkey(fun=snake_obj.right,key="Right")
    s_screen.onkey(fun=snake_obj.left,key="Left")
    game_is_on=True
    while game_is_on:
        game_is_on=snake_obj.move()
        if snake_obj.get_snake_head().distance(food_obj)<COLLISION_WITH_FOOD:
            print("Mmmm Goooot\'th")
            food_obj.refresh()
            score_board_obj.add_score(10)
            snake_obj.extend_snake()
        if (snake_obj.get_snake_head().xcor() >  s_screen.window_width() // 2   or
            snake_obj.get_snake_head().xcor() < -(s_screen.window_width() // 2) or
            snake_obj.get_snake_head().ycor() >  s_screen.window_height() // 2  or
            snake_obj.get_snake_head().ycor() < -(s_screen.window_height() // 2)):
            score_board_obj.reset_scoreboard()
            snake_obj.reset()
            # game_is_on=False
    s_screen.exitonclick()

snake_game()


