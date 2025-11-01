# 
# List methods: sorting
#

towns = ["Bella Coola", "Nakusp", "Anaheim Lake", "Port McNeil"]
populations = [2163, 1589, 1500, 2356]

# Sort the lists. 
# This will sort low to high. You can see how it works 
# for strings and numbers. .sort() sorts the list in place. 
# 
print( "Towns = \t", towns)
print( "Populations = \t", populations)
towns.sort()
populations.sort()
print( "Towns = \t", towns)
print( "Populations = \t", populations)

# Sort in the reverse order
towns.sort(reverse=True)
print( "Towns = \t", towns)
