from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear() #upgrade
        self.write(f"Score: {self.score}" f"Hight score: {self.highscore}", align=ALIGN, font=FONT)

#upgrade
    def rest(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode= "w") as data:
                data.write(f'{self.highscore}')
        self.score = 0
        self.update_scoreboard()

    #upgrade
    #def game_over(self):
     #   self.goto(0, 0)
      #  self.write("Game over", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        #self.clear() upgrade
        self.update_scoreboard()
