from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.update_sc()

    def update_sc(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 60, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 60, "normal"))


    def l_point(self):
        self.l_score+=1
        self.update_sc()
        if self.l_score>2:
            self.goto(-50, 50)
            self.write("1st player won!\n GAME OVER!!", align="center", font=("Courier", 40, "normal"))


    def r_point(self):
        self.r_score+=1
        self.update_sc()
        if self.r_score>2:
            self.goto(-50, 50)
            self.write("2nd player won \nGAME OVER!!!", align="center", font=("Courier", 40, "normal"))




