from turtle import Turtle
from  time import sleep
SNAKE_UNIT_WIDTH = 20
DIRECTIONS={'Right':0,'Left':180,'Up':90,'Down':270}
SNAKE_HEAD=0
SNAKE_TAIL=-1
PREV_BODY_UNIT=-2
class Snake:
    snake_body = []
    snake_screen = None
    def __init__(self, screen):
        self.snake_screen = screen
        self.create_snake()
    def create_snake(self):
        for i in range(3):
            self.extend_snake()
            self.snake_body[i].goto(-SNAKE_UNIT_WIDTH * i, 0)
    def move(self):
        self.snake_screen.tracer(0)
        sleep(0.1)
        for i in range(len(self.snake_body)-1, SNAKE_HEAD, -1):
            if i>SNAKE_HEAD and self.snake_body[i].distance(self.snake_body[SNAKE_HEAD])< (SNAKE_UNIT_WIDTH//2): # head touched snake body
                return False # game over
            self.snake_body[i].goto(self.snake_body[i-1].position())
        self.snake_body[SNAKE_HEAD].forward(SNAKE_UNIT_WIDTH)
        self.snake_screen.update()
        return True # game on
    def up(self):
        if self.snake_body[SNAKE_HEAD].heading() != DIRECTIONS["Down"]: # no 180-degree tern
            self.snake_body[SNAKE_HEAD].setheading(DIRECTIONS["Up"])
    def down(self):
        if self.snake_body[SNAKE_HEAD].heading() != DIRECTIONS["Up"]: # no 180-degree tern
            self.snake_body[SNAKE_HEAD].setheading(DIRECTIONS["Down"])
    def left(self):
        if self.snake_body[SNAKE_HEAD].heading() != DIRECTIONS["Right"]: # no 180-degree tern
            self.snake_body[SNAKE_HEAD].setheading(DIRECTIONS["Left"])
    def right(self):
        if self.snake_body[SNAKE_HEAD].heading() != DIRECTIONS["Left"]: # no 180-degree tern
            self.snake_body[SNAKE_HEAD].setheading(DIRECTIONS["Right"])
    def get_snake_head(self):
        return self.snake_body[SNAKE_HEAD]
    def extend_snake(self):
        self.snake_body.append(Turtle(shape="square"))
        self.snake_body[SNAKE_TAIL].penup()
        self.snake_body[SNAKE_TAIL].color("white")
    def reset(self):
        for link in self.snake_body:
            link.hideturtle()
            del link
        self.snake_body.clear()
        self.create_snake()
