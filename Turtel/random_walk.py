import turtle as T
import random 

Crazy_turtle = T.Turtle()
screen = T.Screen()
T.colormode(255)

screen.bgcolor("black")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    
    random_color = (r,g,b)
    return random_color

directions = [0,90,180,270]
Crazy_turtle.pensize(10)
Crazy_turtle.speed("fastest")

for _ in range(200):
    Crazy_turtle.color(random_color())
    Crazy_turtle.forward(30)
    Crazy_turtle.setheading(random.choice(directions))


