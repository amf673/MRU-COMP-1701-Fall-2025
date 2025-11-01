# 
# List membership
#

alist = ["moose", "deer", "elk", "grizzly bear"]
animal = input( "Enter an animal: ")

# in can be used to test is an item is in a list. 
# `item in list` evaluates to a boolean. 
if animal in alist: 
    print("It is in the list!") 
else: 
    print("It is not in the list")

# the list .index() method returns the index of the item given. 
# BUT! if the item does not exist, it throws an error. 
print( alist.index(animal)) 
