from turtle import *
shape('turtle')
speed(1)

def triangle(sidelength=100): 
	for i in range(3):
		forward(sidelength)
		right(120)

triangle(100)