# 
# 
# List operations 

# Using this list: 

animals = ["elk", "moose", "deer", "black bear", "beaver", "raven"]

# Access an element. Remember that the indexes go from 0 to n-1
# 
print( len(animals)) 

print( animals[2])

# Access a sublist: 
# 
# [ i, j] gets a sublist with element i to element j-1
sublist = animals[2:4]
print( type(sublist))
print( sublist)

# Access the first n items 
sublist = animals[:3] 
print( sublist)

# Access the last n items 
sublist = animals[4:] 
print( sublist)

# Add an item to the list 
# to the end of the list
newanimal = "bison"
animals.append(newanimal)
print( animals)

# at a certain position 
newanimal = "pika"
animals.insert(2, newanimal)
print( animals)

