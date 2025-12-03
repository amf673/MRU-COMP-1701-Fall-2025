# A program that demonstrates many useful things including: reading and writing files and sorting. 
# 
# COMP 1701
# 

def read_file( file:str) -> list:
    """ Reads a text file of integers and returns a list 
    of integers."""
    
    int_list = []
    input_file = open(file, "r")
    
    line = input_file.readline()
    while line != "":
        line_list = line.strip().split()
        for i in range( 0, len(line_list)):
            int_list.append( int( line_list[i]))
        line = input_file.readline()
        
    input_file.close()
        
    return int_list

def save_file( file:str, ints:list) -> None:
    """ Write the list of ints to a file with no more than 10 ints per line
    """
    
    output_file = open( file, "w")
    
    for i in range( 1, len( ints) + 1):
        output_file.write( f"{ints[ i-1]:4} ") 
        if (i % 10 == 0):
            output_file.write( "\n")
            
    output_file.close()

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

def main(): 
    """ Read a list of integers, sort it and save """
    int_list = read_file( "ints.txt")
    selection_sort( int_list) 
    save_file( "sorted.txt", int_list)

main()
