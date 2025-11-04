# 
# Tracing 

def area_rectangle( length: float, width:float) -> float: 
    """ return the area of a rectangle with the given length and width """

    print( f"in area_rectangle() length={length} width = {width}")
    area = length * width
    return area 

def perimeter_rectangle( length: float, width:float) -> float: 
    """ Return the perimter of a rectangle with given sides """

    print( f"in perimeter_rectangle() length={length} width = {width}")
    perimeter = length * 2 + width * 2
    return perimeter

def area_square( side: float) -> float:
    """ return the area of a square with the given side """

    print(f"In area_square() side = {side}")
    area = area_rectangle( side, side)
    return area

def main() -> None: 
    """ """
    length = float( input( "Enter the length of the side: "))
    width = float( input( " Enter the width: "))

    print( f"in main() length={length} width = {width}")
    if length == width: 
        area = area_square( length)
        print(f"The area of the square is {area}")
    else: 
        area = area_rectangle( length, width)
        perimeter = perimeter_rectangle( length, width)
        print( f"The rectangle has perimeter {perimeter} and area {area}")

main()
