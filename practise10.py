# Practise 10 

# 
# Q 1

def sum( int_list:list) -> int:
   """ Returns the sum of the integers in int_list. """
   sum = 0 
   i = 0 
   while i < len(int_list): 
      sum = sum + int_list[i]
      i = i + 1 

   return sum

def sum_for( int_list:list) -> int:
   """ Returns the sum of the integers in int_list. """
   sum = 0 
   for i in range( 0, len(int_list)):
      sum = sum + int_list[i]

   return sum

# Q2 

def rev( astr:str) -> str:
   """ Returns astr in reverse order  """
   new_str = ""
   i = len(astr) - 1
   while i >= 0 : 
      new_str = new_str + astr[i]
      i = i - 1 

   return new_str

def rev_for( astr:str) -> str:
   """ Returns astr in reverse order  """
   new_str = ""
   for i in range( len(astr) - 1, -1, -1): 
      new_str = new_str + astr[i]

   return new_str

# Q3 

# The code prints a times table up to 5 
# Using while loops ... 
def eggs( r:int, n:int):
    """ Times table """ 
    i = 1
    while i < n + 1:
        print( f"{r * i:5}", end=" ")
        i = i + 1
    print()

def spam( n:int): 
    """ Times table """ 
    i = 1
    while i < n + 1:  
        eggs( i, n) 
        i = i + 1

spam(5)

# Q4 
# The code will print 
# 12
# 8
# 4

a = [2, 4, 6, 8, 10, 12]
i = len(a) -1
while i > 0:
    print( a[i])
    i = i -2


# Q5 
"""
*
**
***
****
*****
"""
def star() -> None:
    """ print a star without a nl """
    print( '*', end='')

def spc() -> None: 
    """ print a space without a nl """
    print( ' ', end='')

def nl() -> None: 
    """ print a nl """
    print()

def tri_stars(n:int)->None:
    """ Print a triangle pattern of stars """
    for i in range( 1, n+1): 
        for j in range( 1, i+1):
            star()
        print()
        
tri_stars(7)

# Q6 
"""
    *
   ***
  *****
 *******
*********
"""

def tree_stars(n:int)->None:
    """ Print a tree pattern of stars """
    for i in range( 0, n):
        stars = "*" * (i * 2 + 1)
        print(f"{stars:^{n*2-1}}")
        
def tree( n: int) -> None:
    """ print a pyramid in asterisks """

    width = 2 * n - 1
   
    for i in range( 1, n + 1):
        for j in range( i, (width // 2) + 1):
            spc()
        for j in range( 0, 2 * i - 1):
            star()
        nl()
            
tree(5)


# Q7 
"""For assignment 3. Given a list of strings (at least 5 items) write a function 
that returns a new list  with only items 1 and 3. Remember that you can index into a list to select a particular item and you can add to a list 
with the .append()# methods or concatenate lists with + """

row = [ 'a','g','s','w','u','m']

new_row = []
new_row.append( row[1])
new_row.append( row[4])

print( new_row)

# Q8 
"""
Continuing the question above. Given a list of strings (row) and a list of indices 
(indices), write a function that returns 
a new list consisting of the items in \verb#row# with the indices in \verb#indices#.

i.e. if the function is given row = ['a','b','c','d','e','f'] and indices=[2,3,5] the function will return a list: 
['c','d','f'].
"""

def slice( row:list, indices:list)->list:
    """ """
    new_row = []
    for i in range( 0, len(indices)):
        new_row.append( row[indices[i]])

    return new_row

print( slice( ['a', 'b', 'c', 'd', 'e', 'f'], [1, 4, 5]))
