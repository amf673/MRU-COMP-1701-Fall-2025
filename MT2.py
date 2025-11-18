#
# MT2 
# Fall 2025

def average( alist:list) -> float:
    """ Returns the average of the values in the list. """

    i = 0
    sum = 0 
    while i < len(alist):
        sum = sum + alist[i]
        i = i + 1 
    return sum / len(alist)


def above_avg( alist:list)-> int:
    """ Returns the number of values in the list that are above the list average. """

    count = 0
    avg = average( alist)
    i = 0 
    while i < len( alist):
        if alist[i] > avg:
            count = count + 1
        i = i + 1
    return count


def get_capacities() -> list:
    """ Returns a list of capacities """ 

    capacities_list = []
    item = input( "Enter a capacity (>0), blank when done: ")
    # Note that I do not convert item until later so I can check if 
    # it is blank first. 
    while item.strip() != "": 
        cap = int( item)
        if cap < 0: 
            print( "No negatives, positive vibes only")
        else:
            capacities_list.append(int(cap))
        item = input( "Enter a capacity (>0), blank when done: ")
    return capacities_list


def main(): 
    """ Main """ 
    capacities = get_capacities()
    m = above_avg( capacities)
    print( f"Of {len( capacities)} entered, {m} are above average ")

main()
