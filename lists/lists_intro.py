#
# lists introduction

# Create a list of strings from literals 
# Lists do not have to be all of the same type, but it is good practice to do it that way, for now. 

towns = ["Bella Coola", "Nakusp", "Anaheim Lake", "Port McNeil"]

# 
# The length of a list: 

print( len( towns))

# print an element of the list: 

print( f"Element 3 is {towns[3]}" )

# print all of the list: 

i = 0
while i < len( towns):
    print( f" Element {i} is {towns[i]}")
    i = i + 1

# Create another list that is parallel with the first one. 
# These are the populations of the towns. 
populations = [2163, 1589, 1500, 2356]

# Find an element in the list: 

to_find = "Anaheim Lake"
# We want to find if the string `to_find` appears in the list towns
# use a counted list with a possible early exit.
# Look closely at the loop condition to be sure you understand what is happening! 
i = 0
while i < len( towns) and towns[i] != to_find:
    i = i + 1

# If we found the town, print out the population
if i == len(towns): 
    print( "not found")
else: 
    print( f"{to_find}, is element {i}")
    print( f"The population of {to_find} is {populations[i]}")

# Find total population
# This is an example of working with a list of numbners. 
# In this case, summing them up.

i = 0
sum = 0 
while i < len( populations):
    sum = sum + populations[i]
    i = i + 1

print(sum)

# Once we have the sum, it is easy to get the average. 
# 

if len(populations) > 0:
    print( sum/len(populations))
