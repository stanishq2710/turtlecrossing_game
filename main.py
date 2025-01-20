import turtle as t
import time
from turtlecross import Turtles
from cars import CarManage
from scoreboard import Score


screen = t.Screen()
screen.setup(width=600,height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing Game")
screen.tracer(0)

tim = Turtles()
car = CarManage()
score = Score()

screen.listen()
screen.onkey(tim.go_froward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move_cars()
    # detecting the collision with car
    for cars in car.all_cars:
        if cars.distance(tim) < 10:
            game_is_on = False
            score.game_over()
    # when turtle reaches the other side
    if tim.ycor() > 280:
        tim.goto_start()
        car.inc_level()
        score.level_up()


screen.exitonclick()
