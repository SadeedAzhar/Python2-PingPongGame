import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
my_screen = Screen()
Ball=Ball()

my_screen.bgcolor('black')
my_screen.setup(width=800,height=600)
my_screen.title('Ping-pong')
my_screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
scoreboard=Scoreboard()
my_screen.listen()
my_screen.onkey(r_paddle.up,'Up')
my_screen.onkey(r_paddle.down,'Down')
my_screen.onkey(l_paddle.up,'w')
my_screen.onkey(l_paddle.down,'s')

l_count=0
r_count=0

game_is_on=True
while game_is_on:
    time.sleep(Ball.move_speed)

    Ball.move()
    my_screen.update()

    if (Ball.ycor() < -280) or (Ball.ycor() > 280):
        Ball.bounce_y()
    if Ball.distance(r_paddle)< 40 and Ball.xcor()>340 or Ball.distance(l_paddle)< 40 and Ball.xcor()<-340:
        Ball.bounce_x()

    if Ball.xcor()<-350:
        scoreboard.r_point()
        r_count+=1
        Ball.reset_pos()

    if Ball.xcor()>350:
        scoreboard.l_point()
        l_count+=1
        Ball.reset_pos()
    if l_count>2 or r_count>2:
        game_is_on=False
my_screen.exitonclick()