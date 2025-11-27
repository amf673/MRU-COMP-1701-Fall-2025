
def bar( a:str)-> str:
    """ Returns the string a reversed.  """
    b = ""
    c = 0
    while c < len(a): 
        b = a[c] + b
        c = c + 1
    return b


def foo( a:str) -> list:
    """ Returns a str made up of the last and first words from a """
    b = a.split()
    c = b[0] + b[len(b)-1]
    return c
    
 
def bar2( a:str)-> None:
    """ Returns Nothing """
    c = 0
    while c < len(a): 
        temp = a[c]
        a[c] = a[len(a) - (c+1)] # you cannot change a string so this will throw an error. 
        a[len(a) - (c+1)] = temp
        c = c + 1
    return 

def main(): 
    print( bar("pika"))     # will print akip
    print( foo("wolf   fox  cougar bobcat"))  # will print bobcatwolf
    print( bar2("pika")) # will throw an error. 

main()
