#
# wc - word count 
# 
# Count the number of lines, words and characters in a text file a la the Linux wc command. 
# 
#

def main():
    # Get the name of the file to process. 
    file_name = input( "Enter the file name: ") 

    # Open the file. You always need to open the file to get the 
    # 'file handle', input_file. In this case we are opening the file 
    # for reading, so we add the "r".  
    
    # input_file keeps track of the file that we opened and where we are in the file. 
    # (Files are read from first character to last, in order.)
    input_file = open( file_name, "r")

    # Set up our counters. 
    lines = 0
    chars = 0
    words = 0 

    # Read the first line of the file. .readline() reads up to the next newline character. If
    # we are at the end of the file, .readline() returns an empty string, otherwise 
    # it returns the next line of text. 
    line = input_file.readline()
    while line != "":
        # we read a line so we can add one to the number of lines. 
        lines = lines + 1
        # line is a string so we can get the length of the string with len(), which 
        # is the number of characters that we can add to our character count. 
        chars = chars + len(line)
        # .split() breaks the line up into words (using one or more spaces to separate a word and then puts 
        # those words into a list of strings. The length of that list is the number of words on this line 
        # which we can then add to words. 
        words = words + len( line.split())
        # This is for debugging. repr() prints a string representation of an object and in 
        # this case is useful to see the newlines. 
        print( f"{lines:10} {len(line):10} {len(line.split()):10} {repr( line)}")

        # get the next line. 
        line = input_file.readline()
    
    # Always close the file! 
    input_file.close() 
    # Print out the counts. 
    print( lines, words, chars)

main()