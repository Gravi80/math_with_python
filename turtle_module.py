# https://docs.python.org/3.7/library/turtle.html
# http://web.cecs.pdx.edu/~lmd/cs161/turtle-excerpt.htm
from turtle import Turtle, Screen

screen = Screen()
cursor = Turtle(shape="turtle", visible=True)
cursor.speed(1)
# Using speed(0) makes the turtle move the fastest, 
# whereas speed(1) is the slowest. 
# Try different speeds, like sped(5) and sped(10), if you want.

cursor.hideturtle() #make the turtle invisible
cursor.penup() #don't draw when turtle moves
# cursor.goto(screen.window_width(), screen.window_height())
cursor.goto(-50,-50) #move the turtle to a new location
cursor.pendown() #draw when the turtle moves
cursor.showturtle() #make the turtle visible