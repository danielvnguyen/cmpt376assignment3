# Teaching Loops with the Python Turtle Graphics Library
import turtle

t = turtle.Turtle()
t.speed(1)
t.color("blue")

num_sides = 4
angle = 360 / num_sides
side_length = 100

for i in range(num_sides):
    t.forward(side_length)
    t.right(angle)
