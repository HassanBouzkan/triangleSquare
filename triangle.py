import turtle

# create a turtle object
t = turtle.Turtle()

# draw a triangle
for i in range(3):
    t.forward(100)
    t.left(120)

# move the turtle to the starting position of the square
t.penup()
t.goto(150, 0)
t.pendown()


# exit the turtle screen 
turtle.exitonclick()
