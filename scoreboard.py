from turtle import Turtle
FONT=("Arial", 15, "bold")
ALIGNMENT="center"
class ScoreBoard(Turtle):
    score = 0
    screen = None
    def __init__(self, screen):
        super().__init__()
        self.score=0
        with open("data.txt","r") as high_score_file:
            self.high_score=int(high_score_file.read())
        self.screen=screen
        self.speed("fastest")
        self.penup()
        self.color("White")
        self.goto((0,self.screen.window_height()//2-40))
        self.hideturtle()
        self.write_score()
    def add_score(self, val):
        self.score+=val
        self.clear()
        self.write_score()
    def write_score(self):
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)
    def reset_scoreboard(self):
        if self.score>self.high_score:
            with open("data.txt", "w") as high_score_file:
                high_score_file.write(str(self.score))
            self.high_score=self.score
        self.score=0
        self.add_score(val=0)
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over.", move=False, align=ALIGNMENT, font=FONT)


