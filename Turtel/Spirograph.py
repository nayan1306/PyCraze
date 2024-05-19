import turtle as T
import random 

Crazy_turtle = T.Turtle()
screen = T.Screen()
T.colormode(255)

# screen.bgcolor("black")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    
    color = (r,g,b)
    return color


Crazy_turtle.speed("fastest")

for _ in range(100):
    Crazy_turtle.color(random_color())
    Crazy_turtle.circle(100)
    Crazy_turtle.setheading(Crazy_turtle.heading() + 5)


screen.exitonclick()


