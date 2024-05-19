import turtle as T
import random

# Set up the screen
screen = T.Screen()
screen.bgcolor("black")  # Background color set to black
T.colormode(255)

# Create a turtle object
Crazy_turtle = T.Turtle()
Crazy_turtle.speed("fastest")


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    
    color = (r,g,b)
    return color


Crazy_turtle.speed("fastest")


def spirograph_big():
    for _ in range(100):
        Crazy_turtle.color(random_color())
        Crazy_turtle.circle(100)
        Crazy_turtle.setheading(Crazy_turtle.heading() + 5)
        
def spirograph_small():
    for _ in range(100):
        Crazy_turtle.color(random_color())
        Crazy_turtle.circle(50)
        Crazy_turtle.setheading(Crazy_turtle.heading() + 5)        


# Function to draw Mickey Mouse face
def draw_mickey(turtle):
    spirograph_big()  # Head
    Crazy_turtle.penup()
    Crazy_turtle.goto(180,240)
    Crazy_turtle.pendown()
    spirograph_small()
    Crazy_turtle.penup()
    Crazy_turtle.goto(0,0)
    Crazy_turtle.goto(-180,240)# Right ear
    Crazy_turtle.pendown()
    spirograph_small()

draw_mickey(Crazy_turtle)

screen.exitonclick()
