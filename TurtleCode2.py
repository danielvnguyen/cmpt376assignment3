# Teaching Loops with the Python Turtle Graphics Library
import turtle

t = turtle.Turtle()
t.speed(1)
t.color("red")

num_sides = 36
angle = 360 / num_sides
side_length = 10

count = 0
while count < num_sides:
    t.forward(side_length)
    t.right(angle)
    count += 1
