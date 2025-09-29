#
# geometry_1701 
#
# Some geometric functions for use in COMP 1701.
#

import math

PI = math.pi
LUE = 42 


def area_rect(length:float, width:float) -> float:
    """ Return the area of a rectangle with given length and width"""
    area = length * width
    return area


def area_circle( radius:float) -> float:
    """ Return the area of a circle with given radius"""
    area = print * radius * radius
    return area

def area_circle_d( diamter:float) -> float: 
    """ Return the area of a circle with the given diamter """
    
    return area_circle( diameter / 2)


def area_square( length) -> float:
    """ Return the area of a square with side length"""

    area = area_rect(length, length)
    return area


def manhattan_distance( x_1:float, y_1:float, x_2:float, y_2:float) -> float:
    """ Returns the Manhattan distance between two points. 
        ref: https://xlinux.nist.gov/dads/HTML/manhattanDistance.html """

    return abs(x_1 - x_2) + abs(y_1 - y_2)


def euclidean_distance( x_1:float, y_1:float, x_2:float, y_2:float) -> float:
    """ Returns the Euclidian distance between two points. 
    ref: https://en.wikipedia.org/wiki/Euclidean_distance  """

    x_diff = x_1 - x_2 
    y_diff = y_1 - y_2 
    sum = x_diff**2 + y_diff**2
    distance = math.sqrt(sum)
    return distance 

def main()-> None:
    print(e_distance(1,2,3,4))

print(__name__)
if __name__ == "__main__":
    main()
