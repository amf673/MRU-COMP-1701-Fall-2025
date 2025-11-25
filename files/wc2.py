#
# wc 
# Another version of wc 
# 
# You can see why the other version is better. 
# 
# 

def list_of_words( lines:list) -> list: 
    """  Takes a list of strings and returns a list of lists 
    with each string broken into words. Remove any empty lines. 
    """

    words = []
    i = 0 
    while i < len( lines):
        if lines[i].strip() != "": 
            words.append( lines[i].split())
        i = i + 1 

    return words 


def read_file( filename:str) -> list:
    """ Read the lines in a file and return it as a list of lists. 
    strip() the newlines off the end of the lines. """ 
    
    list_of_lines = []
    # Use the standard way to read a file. 
    input_file = open( filename, "r")
    line = input_file.readline()
    while line != "":
        # strip() removes whitespace and newlines from the line. 
        list_of_lines.append( line.strip() )
        line = input_file.readline()
    input_file.close()

    return list_of_lines

def print_list( words:list)->None:
    """ Print the list of lists """

    i = 0 
    while i < len( words):
        j = 0 
        while j < len( words[i]):
            print( i, j, words[i][j])
            j = j + 1
        i = i + 1
        

def count_chars(lines:list) -> None: 
    """ count the characters in the list of lines """ 

    chars = 0 
    i = 0 
    while i < len( lines):
        j = 0 
        # each line is a list of words so iterate through that 
        while j < len( words[i]):
            chars = chars + len( words[i][j]) 
            j = j + 1
        i = i + 1
        
    return chars 

def count_words(lines:list) -> None: 
    """ count the words  """ 

    words = 0 
    i = 0 
    while i < len( lines):
        words = words + len( lines[i])
        i = i + 1
        
    return words


def main():
    a = read_file( "h.txt")
    b = list_of_words( a)
    print_list(b)

    print( len(b), count_words( b), count_chars( b))

main()