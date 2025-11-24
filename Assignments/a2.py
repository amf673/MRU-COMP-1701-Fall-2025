#
# a2
LINE_LENGTH = 80

import a2lists as a2

def print_line(n:int) -> None:
    """ print a line of n dashes """
    print( '-' * n)


def print_aq( locations:list, air_quality1:list, air_quality2:list)->None:
    """ Prints the air quality readings as a table """
    
    print_line( LINE_LENGTH)
    print( f"{'No.':3}\t{'Location':^20}\t{'Air Quality June':^20}\t{'Air Quality Nov':^20}")
    print_line( LINE_LENGTH)
    i = 0
    while i < len(locations): 
        print( f"{i+1:3d}.\t{locations[i]:<20}\t{air_quality1[i]:^20}\t{air_quality2[i]:^20}")
        i = i + 1
    print_line( LINE_LENGTH)


def main():
    print( "Enter the list of air quality stations: ")
    locations = a2.enter_list()
    # locations = ["Banff", "Jasper", "Hinton", "Calgary", "Bowness", "Highwood Pass"]
  

    print( "\nEnter air quality readings for June ")
    air_quality_june = a2.enter_air_quality( locations)
    # air_quality_june = [100, 100, 30, 40, 35, 67]

    print( "\nEnter air quality readings for Now ")
    air_quality_now = a2.enter_air_quality( locations)
    # Banair_quality_now = [60, 50, 30, 40, 12, 23]

    print_aq( locations, air_quality_june, air_quality_now)

    print( "For June")
    print( f"\tMean = {a2.median(air_quality_june):.1f}")
    print( f"\tMedian = {a2.mean(air_quality_june):.1f}")
    print( f"\tPercentage Good: {(a2.good_pct(air_quality_june))*100}.1f%")

    two_worst = a2.worst_aq( air_quality_june, 2)
    i = 0 
    print( "\tWorst Stations")
    while i < len(two_worst):
        print( f"\t\t{i+1:2d}. {locations[ two_worst[i]]} =  {air_quality_june[ two_worst[i]]}")
        i = i + 1
    
    print( "\nFor Oct")
    print( f"\tMedian = {a2.median(air_quality_now):.1f}")
    print( f"\tMedian = {a2.mean(air_quality_now):.1f}")
    print( f"\tPercentage Good: {(a2.good_pct(air_quality_now))*100}.1f%")

    two_worst = a2.worst_aq( air_quality_now, 2)
    i = 0 
    print( "\tWorst Stations")
    while i < len(two_worst):
        print( f"\t\t{i+1:2d}. {locations[ two_worst[i]]} =  {air_quality_now[ two_worst[i]]}")
        i = i + 1
    
main()