from turtle import Turtle
ALIGMENT = "center"
FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle):

  def __init__(self):
    
    super().__init__()
    self.score = 0
    self.color("white")
    self.penup()
    self.goto(0, 230)
    self.hideturtle()
    self.update_scoreboard()
  


  def update_scoreboard(self):
    self.write(f"score: {self.score}", align=ALIGMENT, font=FONT)
  
  def gameover(self):
    self.goto(0, 0)
    self.write(f"GAMEOVER: {self.score}", align=ALIGMENT, font=FONT)

  def increase_score(self):
    self.score += 1
    self.clear()
    self.update_scoreboard()