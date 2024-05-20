from turtle import Turtle
import time

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 0.1  
        self.y_move = 0.1  
        self.move_speed = 0.05 

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()

# Example usage to test the ball's speed
if __name__ == "__main__":
    from turtle import Screen

    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    screen.tracer(0)

    ball = Ball()

    while True:
        ball.move()
        screen.update()
        time.sleep(ball.move_speed)  # Add delay based on move_speed to control ball speed
