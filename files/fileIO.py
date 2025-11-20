#
# File IO demo 
#
# 
# AMF

input_file = open( "data.txt", "r")

# data.txt is a file of lines (strings terminated by new lines). We want to keep reading lines until the end of the file. 
# Repetitively reading lines, So we will be using a loop!
#
# What kind of loop? We don't know how many lines are in the file so we can't have 
# a counted loop, we need a ..... 

# initialize 

line = input_file.readline()  # priming read 

# how do we know when the last line is read? If we reach end of file, readline returns "". 
cnt = 0
while line != "": # this works because the newline is included in the string. 
    print( f"Line: {cnt} Length: {len( line)}")
    print( f"Line: {cnt} String: {repr( line)}")
    cnt = cnt + 1
    line = input_file.readline() # update the LCV

# We are done with the file, so close it! (Always put your toys away when you are finished with them.)
input_file.close()

