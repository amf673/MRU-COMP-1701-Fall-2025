
# A simple selection sort 
def selection_sort( alist:list) -> None:
    """ sort alist in ascending order """ 
  
    for i in range( len(alist)):
        # assume that item i is the smallest 
        min = i
        for j in range( i, len(alist)):
            if alist[j] <= alist[min]:
                # found a new smallest! 
                min = j
            # swap 
            temp = alist[i]
            alist[i] = alist[min]
            alist[min] = temp

a = [3,4,2,1,8,5,6,7,32,4,4]
selection_sort(a)
print(a)
