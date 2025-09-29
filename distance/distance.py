#
# Some distance calculations
# COMP 1701 
#
## Import our custom geometry module. Alias it to g to avoid having to 
## type the whole thing each time. 
import geometry_1701 as g

# Constants 
METERS_IN_KM = 1000


def m2km(meters:float)->float:
    """ returns the value in km """
    return meters/METERS_IN_KM 


def main() -> None:
    p_x = float(input("Enter the x coord of first point (m): "))
    p_y = float(input("Enter the y coord of first point (m): "))
    q_x = float(input("Enter the x coord of second point (m): "))
    q_y = float(input("Enter the y coord of second point (m): "))

    d = g.euclidean_distance( p_x, p_y, q_x, q_y)
    d_km = m2km(d)

    d_manhattan = g.manhattan_distance(  p_x, p_y, q_x, q_y)
    d_man_km = m2km(d_manhattan)

    print(f"The Euclidean distance between ({p_x},{p_y}) and ({q_x},{q_y}) is {d_km} km")
    print(f"The Manhattan distance between ({p_x},{p_y}) and ({q_x},{q_y}) is {d_man_km} km")

main()

# print(e_distance(2,2,5,6))
# print(e_distance(2,4,8,6))
