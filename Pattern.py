import turtle

# set up the turtle screen
turtle.setup(width=600, height=600)
turtle.speed(0)

# define the colors to use
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# create the pattern
for i in range(200):
    turtle.color(colors[i % 6])
    turtle.forward(i)
    turtle.right(59)

# exit the turtle screen when done
turtle.done()