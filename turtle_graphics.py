import turtle

pen = turtle.Turtle()
pen.shape("turtle")
pen.color("red")

# Draw Square
for i in range(4):
    pen.forward(100)
    pen.left(90)

screen = turtle.Screen()
screen.exitonclick()



import turtle

pen = turtle.Turtle()
pen.color("black", "yellow")  # black = border, yellow = fill
pen.begin_fill()

# Draw square
for i in range(4):
    pen.forward(100)
    pen.left(90)

pen.end_fill()

screen = turtle.Screen()
screen.exitonclick()


import turtle

pen = turtle.Turtle()
pen.color("blue")

for i in range(3):
    pen.forward(100)
    pen.left(120)

screen = turtle.Screen()
screen.exitonclick()


import turtle

pen = turtle.Turtle()
pen.color("green")
pen.circle(80)

screen = turtle.Screen()
screen.exitonclick()


import turtle

pen = turtle.Turtle()
pen.color("red", "orange")
pen.begin_fill()

for i in range(5):
    pen.forward(100)
    pen.right(144)

pen.end_fill()

screen = turtle.Screen()
screen.exitonclick()





