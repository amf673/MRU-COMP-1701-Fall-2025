# Reading and Writing Files.
# 
# In this example we convert a file to sarcastic text. 
# 
# AMF


f = open( "data1.txt", "r")
out = open( "outout.txt", "w")
for line in f:
    newline = ""
    upper = True
    for ch in line:
        if upper: 
            newline = newline + ch.upper()
        else:
            newline = newline + ch.lower()
        upper = not upper
    out.write(newline)

out.close()    
f.close()
