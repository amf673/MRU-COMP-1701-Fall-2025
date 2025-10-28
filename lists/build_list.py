#
# 
# building a list from input  
#

alist = []
item = input( "Enter an item (<CR> to end): ")
while item != "":
    alist.append(item)
    item = input( "Enter an item (<CR> to end): ")

print(alist)
