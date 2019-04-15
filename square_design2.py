from turtle import *
shape('turtle')
speed(0)

def square(sidelength=100): 
	for i in range(4):
		forward(sidelength) # move the turtle forward a certain number of steps(100 pixels) while leaving a trail behind it.
		right(90) # make the turtle turn a specified number of degrees


# Make a function to draw 60 squares, 
# turning 5 degrees after each square and making each successive square bigger. 
# Start at a lengthof 5 and increment 5 units every square. 
for sidelength in range(5,305,5):
	square(sidelength)
	right(5)