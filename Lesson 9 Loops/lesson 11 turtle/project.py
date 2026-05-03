import turtle 
turtle.Screen().bgcolor("green")
turtle.Screen().setup(300,400)
polygon = turtle.Turtle()
num_side= 6
side_length= 70
angle= 360.0 / num_side
for i in range(num_side):
    polygon.forward(side_length)
    polygon.right(angle)
turtle.done()