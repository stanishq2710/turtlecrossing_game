import turtle as t
STARTING_POSITION = (0,-280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Turtles(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("Green")
        self.penup()
        self.goto_start()
        self.setheading(90)

    def goto_start(self):
        self.goto(STARTING_POSITION)

    def go_froward(self):
        self.forward(MOVE_DISTANCE)
