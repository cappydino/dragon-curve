import turtle
from time import sleep

def nextPath(l):
    return l + 'R' + ''.join(map(lambda r: 'L' if r == 'R' else 'R', l[::-1]))

def pathN(l, n):
    if n <= 1:
        return l
    else:
        return pathN(nextPath(l), n - 1);

def turtleDraw(turns, segmentLength):
    for turn in turns:
        turtle.forward(segmentLength)
        if turn == 'R':
            turtle.right(90)
        else:
            turtle.left(90)
    turtle.forward(segmentLength)

start = 'L'
length = 300

for i in range(1, 50):
    turtle.reset()
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    
    turtle.speed(i * 3)
    turtle.setheading(0)
    turtle.left(45 * i + 45)
    turtleDraw(pathN(start, i), length / pow(pow(2, 1/2), i) ) 

    sleep(1)