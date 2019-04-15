from turtle import *
shape('turtle')
speed(1)

def star(side_length=100):
	for i in range(5):
		forward(side_length)
		right(144)
	
star()
# starSpiral