#
# Times Tables
# This is a simple example of nested loops
#

def times_table( n:int)->None:
    """ print a times table of size n """
    i = 1
    while i <= n:
        j = 1
        while j <= n:
            print( f" {i * j:^8d}", end="")
            j = j + 1
        print()
        i = i + 1
    print()

def main(): 
    times_table(20)

main()
