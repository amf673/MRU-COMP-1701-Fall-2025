#
# Types of loops 
#

def counted_loop( start:int, stop:int, increment: int)-> None:
    """ example of a counted loop. counts from start to stop by increment  """
    
    # Our loop control variable will be i 
    # Initialize it to start 
    i = start 

    # Our loop condition will be i < stop. The loop will continue until i >= stop
    while i < stop:
        # add code to do whatever we wanted to do multiple times here. For this example 
        # just print the number.
        print( f"{i:4}.")
        # update our loop control variable.
       
        i = i + increment

def sentinel_loop( sentinel:int)->None:
    """ example of a sentinel loop. Enter numbers until 'sentinel' is entered """

    # Our loop control variable will be num 
    # We will initialize it with an input 
    num = int( input( "Enter a number: "))
    while num != sentinel: 
        print( f"num: {num}")
        num = int( input( "Enter a number: ")) # update the LCV

def accumulator_loop( sentinel: int) -> int:
    sum = 0
    num = int( input( "Enter a number: "))
    while num != sentinel: 
        print( f"num: {num}")
        sum = sum + num
        num = int( input( "Enter a number: "))
    return sum

def acc_loop_count( sentinel: int) -> int:

    sum = 0
    i = 0
    num = int( input( "Enter a number: "))
    while num != sentinel: 
        print( f"num: {num}")
        sum = sum + num
        i = i + 1
        num = int( input( "Enter a number: "))
    avg = 0
    if i > 0: 
        avg = sum / i
        
    return  avg

def main(): 
    counted_loop(2, 20, 2)
    print( accumulator_loop(0))
    
main()
