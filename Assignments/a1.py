# A. Fedoruk
# COMP 1701 Fall 2025
# Assignment 1

# We will be doing lots of trig and other math so we need the math module. 
import math

## CONSTANTS 

# Mean Earth Radius in km from assignment 
MEAN_EARTH_RADIUS = 6371.230 

# Location of chair statue in decimal degrees, from assignment 
HOMAGE_LAT  = 51.013762 
HOMAGE_LONG = 114.133699

MIN_PER_DEG = 60
SEC_PER_DEG = 3600

STD_FARE = 3.80 # from Calgary Transit 

# Symbols for displaying things 
DEGREE = "\u00B0"
MINUTE = "\u0027"
SECOND = "\u0022"


def to_radians( angle:float) -> float: 
    """ Convert an angle in degrees to radians. or could use math.radian(), but 
    it is more fun to do it myself! """

    return angle * math.pi / 180


def haversine( theta: float) -> float: 
    """ Returns the value of the haversine function of theta given in radians. 
    """

    return math.sin( theta / 2) * math.sin( theta / 2)


def haversine_distance( lat_a:float, long_a:float, lat_b:float, long_b:float) -> float: 
    """" Calculate the geodesic distance between the two points (a and b) given in decimal 
    degrees. 
    """
    # The math module wants to work in radians rather than degrees
    lat_a_rad  = to_radians( lat_a)
    long_a_rad = to_radians( long_a)

    lat_b_rad  = to_radians( lat_b)
    long_b_rad = to_radians( long_b)

    # A tracing statement used to debug
    # print( f"lat a :{lat_a_rad} long a:{long_a_rad} lat b:{lat_b_rad} long b: {long_b_rad}")

    # compute the differences in latitude and longitude
    delta_lat = lat_a_rad - lat_b_rad
    delta_long = long_a_rad - long_b_rad

    a = haversine( delta_lat) + math.cos( lat_a_rad) * math.cos( lat_b_rad) * haversine( delta_long)
    # A tracing statement used to debug
    # print( f"a = {a}")
    
    c = 2 * math.atan2( math.sqrt( a), math.sqrt( 1 - a))
    
    # A tracing statement used to debug
    # print( f"c = {c}")
    
    d = MEAN_EARTH_RADIUS * c
    
    # A tracing statement used to debugprint( f"d = {d}")

    return d


def mru_distance( lat:float, long:float) -> float:
    """ return geodesic distance between Homage statue and given 
    point in dec lat long """

    return haversine_distance( lat, long, HOMAGE_LAT, HOMAGE_LONG)


def to_degrees( deg:int, min:int, sec:float) -> float:
    """ return the decimal degrees from the given lat or long in DMS """

    return deg + min / MIN_PER_DEG + sec / SEC_PER_DEG


def mru_fare( distance:float) -> float:
    """ calculate the discounted fare based on distance """

    reduction = 1 / ( 0.5 + math.exp( 3 - distance))
    
    return STD_FARE - reduction


def main() -> None: 

    print( "For your starting location: ")
    lat_deg = int( input( "What is the latitude's degrees? "))
    lat_min = int( input( "What is the latitude's minutes?" ))
    lat_sec = float( input( "What is the latitude's seconds (precise to 3 decimal places)?" ))

    long_deg = int( input( "What is the longitude's degrees? "))
    long_min = int( input( "What is the longitudes's minutes?" ))
    long_sec = float( input( "What is the longitudes's seconds (precise to 3 decimal places)?" ))

    lat = to_degrees( lat_deg, lat_min, lat_sec)
    long = to_degrees( long_deg, long_min, long_sec)

    # debug statement
    # print( f"In DD {lat:.5f} {long:.5f}")

    distance = mru_distance( lat, long)
    fare = mru_fare( distance)

    print( f"Traveling from the user's starting location {lat_deg}{DEGREE} {lat_min}{MINUTE} {lat_sec}{SECOND} North, {long_deg}{DEGREE} {long_min}{MINUTE} {long_sec}{SECOND} West")
    print( f"to the Homage statue on MRU campus is approximately {distance:.1f} km.")
    print( f"The fare would be ${fare:.2f}.")

main()


