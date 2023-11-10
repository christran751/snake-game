from turtle import Turtle, Screen
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    # whenever a snake object is initialize it automatically has the following attributes as denoted below
    def __init__(self):
        self.snake = []
        self.create_snake()   # All instance method can call another instance method within the same class.
        # Just first use the self parameter

    def create_snake(self):
        """This method here create our 3 snake segment for us"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        main_body = Turtle(shape="square")
        main_body.color("white")
        main_body.penup()
        main_body.goto(position)
        self.snake.append(main_body)

    # Movement of the snake
    # Here, we call for the move_up method first inside the move method then defined the move_up method later
    def move(self):
        # Use screen as a parameter, that way we could import it on the main file and do it there instead
        """This method has two purpose. First, it make it so that the snake automatically moves
        Second, it allows for the user to control the snake"""
        for body_num in range(len(self.snake) - 1, 0, -1):
            self.snake[body_num].goto(self.snake[body_num - 1].position())
        self.snake[0].forward(MOVE_DISTANCE)

    def move_up(self):
        if self.snake[0].heading() != 270:
            # If snake isn't already facing  south, we can move the snake upwards
            self.snake[0].setheading(90)

    def move_down(self):
        if self.snake[0].heading() != 90:
            # If snake isn't  facing north, we can move snake down
            self.snake[0].setheading(270)

    def move_right(self):
        if self.snake[0].heading() != 180:
            self.snake[0].setheading(0)

    def move_left(self):
        if self.snake[0].heading() != 0:
            self.snake[0].setheading(180)

    def grow_size(self):
        position = self.snake[-1].position()
        self.add_segment(position)











