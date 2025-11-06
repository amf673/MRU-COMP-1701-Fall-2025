# Inserting items into a list in order. 
# 

def insertitem( alist:list, item:str)->None:
    """ insert item into alist maintaining ascending order """

    i = 0
    # keep track of whether or not we have inserted the value
    inserted = False
    while i < len(alist) and not inserted:
    # this loop will terminate if we have gone through all 
    # of the items, or we have inserted our new item 

        if item == alist[i]:
            # already in the list
            inserted = True
        elif item < alist[i]:
            alist.insert( i, item)
            inserted = True
        
        i = i + 1
        
    if not inserted:
        alist.append(item)


def enter_items() -> list:
    """ Enter items into a list. """
    newlist = []
    item = input( "Enter an item: ")
    while item != "":
        insertitem( newlist, item)
        item = input( "Enter an item: ")
    return newlist

def main():
    animals = enter_items()
    print( animals)

main()
