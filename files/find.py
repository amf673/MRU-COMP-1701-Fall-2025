# find
# Find words in a file. 
# 

def find( file_name:str, word:str) -> None: 
    """ Prints the lines that contain `word` """
    input_file = open( file_name, "r")
    line_number = 0 
    line = input_file.readline()
    while line != "":
        line_number = line_number + 1
        line_list = line.lower().split()
   
        if word.lower() in line_list: 
           print(f"{line_number:5}. {line.strip()}")
        line = input_file.readline()
    
    # Always close the file! 
    input_file.close() 


def main():
    find( "h.txt", "water")
main()