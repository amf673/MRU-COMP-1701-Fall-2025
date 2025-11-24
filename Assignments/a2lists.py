# 
# list functions 

GOOD_AQ = 50

def is_even( i:int) -> bool:
    """ Returns true if i is an even number. """
    
    return (i % 2 == 0)


def avg( x:float, y:float) -> float:
    """ Returns the average of the two arguments """
    
    return (x + y ) / 2


def find_in_list( item, alist) -> int:
    """ find the first occurrence of item in list. 
     If the item is not in the list, return -1 """

    if item in alist: 
        return alist.index(item)
    else:
        return -1


def copy( alist:list) -> list: 
    """ make a copy of alist """
    new_list = []
    i = 0
    while i < len(alist):
        new_list.append(alist[i])
        i = i + 1
    
    return new_list


def empty_list( n:int) -> list:
    """ Create an empty list of length n """
    new_list = [] 
    i = 0
    while i < n:
        new_list.append(None)
        i = i + 1

    return new_list


def swap( alist:list, i, j) -> None:
    """ swap the ith and jth item in alist """

    temp = alist[i]
    alist[i] = alist[j]
    alist[j] = temp


def sort( alist:list) -> None:
    """ sorts alist from smallest to largest """

    i = 0
    while i < len( alist): 
        j = 0
        while j < len( alist) - (i+1): 
            if alist[j] > alist[j+1]:
                swap( alist, j, j+1)
            j = j + 1
        i = i + 1


def sort_dual( alist:list, blist:list) -> None:
    """ sorts both lists based on blist """

    i = 0
    while i < len( blist): 
        j = 0
        while j < len( blist) - (i+1): 
            if blist[j] > blist[j+1]:
                swap( alist, j, j+1)
                swap( blist, j, j+1)
            j = j + 1
        i = i + 1



def mean( alist:list) -> float:
    """ return the mean of a list of numbers """

    i = 0
    sum = 0
    while i < len(alist): 
        sum = sum + alist[i]
        i = i + 1
    avg = 0
    if i > 0:
        avg = sum / i 

    return avg


def median( alist:list) -> float:
    """ return the median of a list of numbers """

    b = copy( alist)
    sort( b)
    mid = len( b) // 2

    if is_even( len(b)): 
        med = avg( b[ mid - 1], b[ mid])
    else:
        med = alist[ mid]

    return med


def max( alist:list) -> int:
    """ Return the location of the largest value in alist """

    if len(alist) == 0: 
        mx_loc = -1 
    else:
        i = 0
        mx_loc = 0
        while i < len(alist):
            if alist[i] > alist[mx_loc]: 
                mx_loc = i
            i = i + 1

    return mx_loc


def get_aq( station:str, locations:list, air_quality:list) -> float:
    """ Return the aq reading for location station """
    
    i = find_in_list( station, locations)
    if i != -1:
        return air_quality[i]
    else: 
        return -1


def enter_list() -> list:
    """ Enter a list of items and return the list """

    new_list = []
    item = input( "Enter an item <Ret> to end: ")
    while item.strip() != "":
        new_list.append( item)
        item = input( "Enter an item <Ret> to end: ")

    return new_list



def enter_air_quality( locations:list) -> list:
    """ prompts for a list of air quality readings at the given 
    locations. """

    air_quality = []
    i = 0 
    while i < len( locations):
        aq = float( input( f"Enter air quality for {locations[i]}: "))
        air_quality.append( aq)
        i = i + 1
    return air_quality



def worst_aq( air_quality:list, n: int) -> list:
    """ Return the indexes of the n locations with the worst (highest) air quality. """
    
    worst = []
    b = copy( air_quality)
    i = 0
    while i < n:
        mx = max( b)
        worst.append( mx)
        b[ mx]=0
        i = i + 1

    return worst



def good_pct( air_quality:list) -> float: 
    """ returns the percentage of air_quality readings that are good, that is less or 
     equal to GOOD_AQ """
    
    i = 0
    count = 0
    while i < len(air_quality):
        if air_quality[i] <= GOOD_AQ: 
            count = count + 1
        i = i + 1
    return count / len(air_quality)


def main(): 
    """ Testing stuff """
    a = [10, 15, 23, 12, 8, 2]
    b = [11, 10, 1, 2, 3, 6, 9, 4, 5, 7, 8]
    #c = []
    print(good_pct( b))
    #print(b)
    print( max(a))
    print( a[max(a)])
    print( b[max(b)])

    c = empty_list(20)
    print(c)
    # print(median(b))
    # print( mean(a))
    # print( median(a))
    # print(a)
    # locs = ["a", "foo", "spam", "eggs"] 
    # print( enter_air_quality(locs))


if __name__ == "__main__": 
    main() 


