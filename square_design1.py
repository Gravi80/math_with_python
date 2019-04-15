from turtle import *
shape('turtle')
speed(0)

def square(sidelength=100): 
	for i in range(4):
		forward(sidelength) # move the turtle forward a certain number of steps(100 pixels) while leaving a trail behind it.
		right(90) # make the turtle turn a specified number of degrees


for deg in range(0,360):
	square()
	right(deg)
