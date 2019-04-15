from turtle import *
shape('turtle')
speed(1)

def square(sidelength): 
	for i in range(4):
		forward(sidelength) # move the turtle forward a certain number of steps(100 pixels) while leaving a trail behind it.
		right(90) # make the turtle turn a specified number of degrees

square(100)		