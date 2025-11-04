#
# Fun with decisions
# 
# A. Fedoruk & COMP 1701 001
# 
# Shows nested versus elif decisions

import turtle as t
import random as r

# Constants for directions in the turtle graphic Cartesion plane. 
EAST = 0 
WEST = 180 
NORTH = 90 
SOUTH = 270

# Some colours
COLOURS = ["black", "green", "blue", "yellow", "orange", "wheat", "turquoise", "cyan"]


def circ(tur, x:int, y:int, radius:int, colour:str, fill:bool) -> None:
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

def t_or_f( t:str) -> bool: 
    """ return True if t is T or True False otherwise """

    return (t.lower() == "true") or (t == "T")

def get_colour( sw1:bool, sw2:bool) -> str:
    """ Get a colour based on the rules 
        T T = 0 
        T F = 1
        F T = 2
        F F = 3 
    and indexing into COLOURS
    """
    # This one uses a nested if 

    col_ind = 0
    if sw1:
        if sw2: 
            col_ind = 0
        else: 
            col_ind = 1
    else:
        if sw2: 
            col_ind = 2
        else:
            col_ind = 3

    col = COLOURS[col_ind]

    return col

def get_colour2( sw1:bool, sw2:bool) -> str:
    """ Get a colour based on the rules 
        T T = 0 
        T F = 1
        F T = 2
        F F = 3 
    and indexing into COLOURS
    """
    # This one uses an elif 

    col_ind = 0
    if sw1 and sw2: 
        col_ind = 0
    elif sw1 and not sw2: 
        col_ind = 1
    elif not sw1 and sw2:
        col_ind = 2
    else:
        col_ind = 3

    col = COLOURS[col_ind]

    return col

def main():
    otto = t.Turtle()
    otto.speed('slow')
    otto.shape('turtle')
    otto.pensize(5)

    switch1 = t_or_f( input( "Enter True or False for switch 1: "))
    switch2 = t_or_f( input( "Enter True or False for switch 2: "))
    
    print( switch1, switch2)

    col = get_colour( switch1, switch2)
    
    circ( otto, 0, 0, 100, col, True)
        
    t.exitonclick()
    
main()
