import turtle
from turtle import Turtle, Screen
import random

my_turtle = Turtle()
turtle.colormode(255)

#Generating a random 16 millions color using tuples.
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


#my_turtle.shape("turtle")
#my_turtle.color("#800000")

# TODO 1: Challenge 1 - Draw a square.
def draw_square():
    for i in range(4):
        my_turtle.speed(1)
        my_turtle.forward(100)
        my_turtle.right(90)


# TODO 2: Challenge 2 - Draw a dashed line.
def dashed_line():
    for i in range(15):
        my_turtle.speed(1)
        my_turtle.forward(10)
        my_turtle.penup()
        my_turtle.forward(10)
        my_turtle.pendown()


# TODO 3: Challenge 3 - Draw a Different Shapes.
def draw_shapes(n):
    color = ["red", "blue", "green", "yellow", "purple", "orange", "black"]
    for i in range(7):
        random_color = random.choice(color)
        my_turtle.color(random_color)
        angle = 360 / n
        my_turtle.speed(1)
        for _ in range(n):
            my_turtle.forward(50)
            my_turtle.right(angle)
        n += 1
# draw_shapes(3)


# TODO 4: Challenge 4 - Draw a Random Walk.
def random_walk(number_of_steps):
    #color = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
             #"LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
    directions = [0, 90, 180, 270]
    for i in range(number_of_steps):
        my_turtle.pensize(15)
        random_direction = random.choice(directions)
        #random_color = random_color()
        my_turtle.speed(3)
        my_turtle.color(random_color())
        my_turtle.forward(30)
        my_turtle.setheading(random_direction)

# random_walk(100)


# TODO 5: Challenge 5 - Draw a Spirograph.
def draw_spirograph():
    my_turtle.speed("fastest")
    for i in range(75):
        my_turtle.color(random_color())
        my_turtle.pensize(1)
        my_turtle.left(5)
        my_turtle.circle(100)


draw_spirograph()

screen = Screen()
screen.exitonclick()
