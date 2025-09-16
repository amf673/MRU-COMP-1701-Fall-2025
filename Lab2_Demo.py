#
# Demo to prepare for Lab 2 - Exponential Function 
# A. Fedoruk Sept 2025

import math

def main() -> None:
    """ This program asks for the two sides of a right 
    triangle and calculates and displays the hypotenuse. 
    Uses https://en.wikipedia.org/wiki/Pythagorean_theorem """


    a = float( input( "Enter a: "))
    b = float( input( "Enter b: "))

    c = math.sqrt( (a ** 2) + (b ** 2) ) 

    print( "The hypotenuse is ", c)

main() 
