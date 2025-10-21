from turtle import Turtle
from  random import randint
class Food(Turtle):
    food_screen = None
    def __init__(self, screen):
        super().__init__()
        self.food_screen=screen
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()
    def get_random_point(self):
        return (randint(-self.food_screen.window_width()//2+10,self.food_screen.window_width()//2-10),
                randint(-self.food_screen.window_height()//2+10, self.food_screen.window_height()//2-10))
    def refresh(self):
        self.goto(self.get_random_point())


