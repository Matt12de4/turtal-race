from turtle import *
from random import randint
speed(0)
penup()
hideturtle()
goto(-140, 140)
for step in range(16):
    write(step, align="center")
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)
showturtle()

ada = Turtle()


ada.color("red")
ada.shape("turtle")

ada.penup()
ada.goto(-160, 100)
ada.pendown()
ada.right(360)
bob = Turtle()
bob.color("blue")
bob.shape("turtle")

bob.penup()
bob.goto(-160, 70)
bob.pendown()
bob.right(360)
yeet = Turtle()
yeet.color("purple")
yeet.shape("turtle")

yeet.penup()
yeet.goto(-160, 40)
yeet.pendown()
yeet.right(360)
b = Turtle()
b.color("green")
b.shape("turtle")

b.penup()
b.goto(-160, 10)
b.pendown()
b.right(360)



for turn in range(100):
    ada.forward(randint(1,5))
    bob.forward(randint(1,5))
    yeet.forward(randint(1,5))
    b.forward(randint(1,5))
