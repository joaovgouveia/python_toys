import turtle
turtle.bgcolor("black")

pen = turtle.Turtle()
pen.speed(0)

def spiral_1():

    colors = ["red", "dark red"]
    for n in range(500):
        pen.forward(n)
        pen.right(89)
        pen.pencolor(colors[n % 2])

def spiral_2():
    colors = ["red", "dark red"]
    for n in range(500):
        pen.forward(n)
        pen.right(59)
        pen.pencolor(colors[n % 2])