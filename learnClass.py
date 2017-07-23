import turtle

def drawsq():
    rats = turtle.Turtle()
    #turtle.shape("turtle")
    count = 0
    while count < 4:
        rats.forward(100)
        rats.right(90)
        count = 1+count
    cats = turtle.Turtle()
    cats.circle(100)
    dogs = turtle.Turtle()
    tri = 0
    while tri < 4:
        dogs.forward(300)
        dogs.left(120)
    #dogs.forward(300)
    #dogs.left(120)
    #dogs.forward(300)
        tri = 1 + tri
drawsq()
