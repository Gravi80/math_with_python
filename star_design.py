from turtle import *
shape('turtle')
speed(0)

def star(side_length=100):
	for i in range(5):
		forward(side_length)
		right(144)


def starSpiral():
	for length in range(5,600,5):
		star(length)
		right(5)

starSpiral()