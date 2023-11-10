from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x=0, y=265)
        self.current_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.current_score}",align="center", font=('Courier', 24, 'normal'))

    def calculate_score(self):
        self.current_score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(f"Game Over.", align="center", font=('Courier', 24, 'normal'))






