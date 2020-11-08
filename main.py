from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from cars import Car
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
loop_count = 0
speed = 0.2
car = Car()
all_cars = [car]

screen.listen()
screen.onkey(player.move_forward, "Up")
screen.onkey(player.move_backward, "Down")

game_is_on = True
while game_is_on:

    time.sleep(speed)
    loop_count += 1
    screen.update()
    for item in all_cars:
        item.move()
        if item.xcor() - 30 < player.xcor() < item.xcor() + 30 and item.ycor() - 20 < player.ycor() < item.ycor() + 20:
            game_is_on = False

    if loop_count % 6 == 0:
        new_car = Car()
        all_cars.append(new_car)

    if player.ycor() > 280:
        scoreboard.level_up()
        scoreboard.refresh()
        player.level_up()
        speed *= 0.8

scoreboard.game_over()

screen.exitonclick()