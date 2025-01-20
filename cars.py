import turtle as t
import random as r
COLORS = ["red","orange", "yellow","green","blue","purple"]
STARTING_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManage():
    def __init__(self):
        self.all_cars =[]
        self.car_speed = STARTING_DISTANCE

    def create_cars(self):
        random_chance = r.randint(1,6)
        if random_chance == 1:
            new_cars = t.Turtle("square")
            new_cars.shapesize(stretch_wid=1, stretch_len=2)
            new_cars.penup()
            new_cars.color(r.choice(COLORS))
            random_y = r.randint(-250, 250)
            new_cars.goto(300, random_y)
            self.all_cars.append(new_cars)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def inc_level(self):
        self.car_speed *= MOVE_INCREMENT


