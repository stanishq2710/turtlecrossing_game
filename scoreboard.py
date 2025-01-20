import turtle as t
FONTS = ("Courier",24,"normal")


class Score(t.Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-270,250)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level : {self.level}",align="left", font=FONTS)

    def level_up(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center",font=FONTS)

