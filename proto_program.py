# 
# Header comment that includes your name, date, what the program is
# 
# Exercise 999 - Some awesome code!
#
# Maria Wang
# Sept 12, 2025
# 

# import any modules that you need ... 
import math
import random 


# Any constants that you need ... 
TIP_RATE = 0.10
GST = 0.05 
ASSIGNMENT_WEIGHT = 10


# function definitions. 
# Notes: 
# - there are two blank lines between the end of one function and the next function defintion;
# - all function parameters include type hints. 
# - all functions have a return type hint. 
# - all functions have a docstring describing what it does. 
def foo( x:float, n:int) -> bool: 
   """ 
   foo takes two parameters and if they are both positive it returns 
   True, else it returns False
   """
   return x > 0 and n > 0


def bar( y:bool) -> bool:
   """ 
   bar takes one parameter and returns the negation
   """
   return not y


# A main function. Main usually has no parameters and returns None. 

def main() -> None: 
   """ 
   pass is a placeholder operation that does nothing. It is just there until the real 
   code gets added.It is handy as you are developing a program.
   """
   # pass is a placeholder that does nothing
   pass 

# invoke main() 

main()
