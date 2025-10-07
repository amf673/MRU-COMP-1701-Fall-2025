# Fun with decisions
# 
# A. Fedoruk & COMP 1701 001
# 
# 

import turtle as t
import random as r

# Constants for directions in the turtle graphic cartesion plane. 

EAST = 0 
WEST = 180 
NORTH = 90 
SOUTH = 270
COLOURS = ["red", "green", "blue", "yellow", "orange", "wheat", "turquoise"]

MENU = "1. Draw a square\n2. Draw a Circle\n3. Draw a Hexagon\n4. Exit\n"

def polygon(tur, x,y, len_side, sides, colour) -> None:
    """ Draw a regular polygon with the given sides and length """
    angle = int(360/sides)
    tur.penup()
    tur.goto(x,y)
    tur.pencolor(colour)
    tur.pendown()
    for _ in range(sides):
        tur.forward(len_side)
        tur.left(angle)
    tur.penup()


def circ(tur, radius, x, y, colour, fill:bool):
    """Draw a circle with turtle tur with bottom at x,y, radius radius in colour colour"""
    
    tur.fillcolor(colour)
    if fill == True:
        tur.begin_fill()
    tur.penup()
    tur.goto(x,y)
    tur.pencolor(colour)
    tur.pendown()
    tur.circle(radius)

    tur.end_fill()
    tur.penup()


def square(tur, len_side, x, y, colour):
    """Draw a square with turtle tur with bottom left corner at x,y, sides of length len_side in colour colour"""
    tur.penup()
    tur.pencolor(colour)
    tur.goto(x,y)
    tur.begin_fill()
    tur.pendown()
    tur.setheading(EAST)
    tur.forward(len_side)
    tur.left(90)
    tur.forward(len_side)
    tur.left(90)
    tur.forward(len_side)
    tur.left(90)
    tur.forward(len_side)
    tur.end_fill()
    tur.penup()


def rand_colour() -> str: 
    """ Return a random colour """
    index = r.randint( 0, len( COLOURS)-1)
    return COLOURS[index]


def main():
    otto = t.Turtle()
    otto.speed('slow')
    otto.shape('turtle')
    otto.pensize(5)

    print( MENU)
    command = int(input("Enter what you want to do: "))
    if command > 0 and command < 4: 
        col = input("Enter the colour (red,green,blue,turquoise): "))
    if command == 1: 
        square(otto, 100, 0, 0,col)
    elif command == 2: 
        circ(otto, 225, 0, -100, col,True)
    elif command == 3:
        polygon( otto, 0, 0, 200, 6,col)
    elif command == 4:
        exit()
    else:
        length = r.randint(50,200)
        sides = r.randint(3,12)
        col = rand_colour()
        print( length, sides, col)
        polygon(otto, 0,0, length, sides, col)
        
    t.exitonclick()

main()
