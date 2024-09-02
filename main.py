import turtle
from turtle import Turtle, Screen
import random

screen=Screen()
timmy_the_turtle=Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.pensize(5)

directions=[0,90,180,270]
colours=["red","green","black","orange","blue","violet","yellow","indigo"]
timmy_the_turtle.speed("fastest")

b=""
for _ in range(200):
    timmy_the_turtle.color(random.choice(colours))
    timmy_the_turtle.forward(30)
    timmy_the_turtle.setheading(random.choice(directions))















screen=Screen()
screen.exitonclick()