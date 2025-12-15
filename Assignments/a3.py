#
# A3 - Relational Operations 
#
# Alan Fedoruk Fall 2025 COMP 1701
# 

# Set up commands 
COMMANDS = ["read", "save", "count", "columns", "project", "select", "sort", "distr", "exit", "print"]
READ = COMMANDS[0]
SAVE = COMMANDS[1]
COUNT = COMMANDS[2]
COLUMNS = COMMANDS[3]
PROJECT = COMMANDS[4]
SELECT = COMMANDS[5]
SORT = COMMANDS[6]
DISTR = COMMANDS[7]
EXIT = COMMANDS[8]
PRINT = COMMANDS[9]

NL = "\n"


""" *************** """
""" File Operations """
""" *************** """

def read_csv( filename:str) -> list:
    """ Read a csv file and return it as a list of rows
        Assume first row is column headers. if a blank line 
        is encountered, that is the end of the table! 
    """

    table = []
    file = open( filename, "r")
    line = file.readline()
    while line.strip() != "":
        row = line.strip().split( ",")
        table.append( row)
        line = file.readline()
    file.close()

    return table


def save_csv( table:list, filename:str) -> None:
    """ Save the table given as a csv file names filename 
    """

    file = open( filename, "w")

    for i in range( 0, len( table)):
        row = table[i]
        line = ""
        for j in range( 0, len( row)):
            col = row[j]
            if line == "": 
                line = col
            else:
                line = line + "," + col

        file.write( line + NL)

    file.close()


""" *************** """
""" Printing Ops    """
""" *************** """

def total_table_width( columns:list) -> int:
    """ Returns the total print width for the table 
    """

    width = 0 
    for i in range( 0, len( columns)):
        width = width + 2 + columns[i] + 1

    return width


def column_widths( table:list) -> list:
    """ Return a list of maximum column sizes 
    """

    columns = []
    headers = get_header( table)
    for i in range( 0, len( headers)):
        columns.append( len( headers[i]))

    for i in range( 1, len( table)):
        row = table[i]
        for j in range( 0, len( row)):
            if len( row[j]) > columns[j]:
                columns[j] = len( row[j])

    return columns


def print_line( w:int) -> None:
    """ Print a line of length w 
    """
    
    print ( '-' * w)


def print_table( table:list) -> list:
    """ Print the table in a reasonable way. 
    """

    columns = column_widths( table)
    width = total_table_width( columns)
   
    print_line( width)
    first = True
    for i in range( 0, len( table)):
        row = table[i]
        for j in range(0, len( row)):
            print( f" {row[j]:<{columns[j]}} ", end = "")
        print()
        if first:
            print_line( width)
        first = False
    print_line( width)

    print_count( table)


def print_cols( table:list) -> None:
    """ Print the column names in table. 
    """
 
    headers = get_header( table) 
    print( "Columns")
    print_line( len( "Columns"))
    for i in range( 0, len( headers)):
        print( headers[i])
    print_line( len( "Columns"))


def print_count( table:list) -> None:
    """ Print the number of rows in table. 
    """
    
    print( f"{len( table) - 1} rows")


""" *************** """
""" Table Ops       """
""" *************** """

def get_header( table:list) -> list:
    """ Return the header row from the table 
    """

    return table[0]


def get_col_ind( table:list, column:str) -> int:
    """ Return the index of the column heading, 
        return -1 is the column is not present. 
    """

    header = get_header( table)
    if column in header:
        return header.index( column)
    else: 
        return -1


def slice( row:list, cols:list) -> list:
    """ Returns a new list (row) with only the columns (indexed) 
        given in cols
    """

    new_row = []
    for i in range( 0, len( cols)):
        c = cols[i]
        new_row = new_row + row[c:c+1]

    return new_row


def project( table:list, cols:list) -> list:
    """ Returns a new table with only the columns listed in cols 
    """
    
    # get the indexes of the columns we want
    ind_cols =[]
    for a in cols:
        ind_cols.append( get_col_ind( table, a))

    new_table = []
    for i in range( 0, len( table)):
        row = table[i]
        new_table.append( slice( row, ind_cols))

    return new_table


def select( table:list, col:str, value:str) -> list:
    """ Perform a select. 
        Return a new table with only the rows where col==value 
    """

    new_table = []
    new_table.append( table[0]) # add the headers to the new table

    # find the index of the column we are interested in 
    key = get_col_ind( table, col)
    print(key, col, value)
    for i in range( 0, len( table)):
        row = table[i]
        if row[key].strip().lower() == value.strip().lower():
            new_table.append( row)

    return new_table


def swap( table:list, i: int, j:int) -> None:
    """ Swap element i with element j 
    """

    if i != j: 
        temp = table[i]
        table[i] = table[j]
        table[j] = temp


def sort( table:list, col:str) -> None:
    """ Sort the table in place based on column col 
    """

    sort_key = get_col_ind( table, col)

    for i in range(1, len(table)): 
        min = i
        for j in range( i + 1, len( table)):
            if table[j][sort_key] < table[min][sort_key]:
                min = j
        swap( table, i, min)


def distr( table:list, column:str) -> list:
    """ Return a table that is a distribution (value_counts()) 
        of column 
    """

    key = get_col_ind( table, column)
    sort( table, column)

    new_table = []
    new_table.append( [column, "Count"])
    value = table[1][key]
    i = 2
    new_table.append( [value, str(1)])

    while i < len(table):
        if table[i][key] == value:
            new_table[len( new_table)-1][1] = str( int( new_table[len( new_table)-1][1]) + 1) 
        else:
            value = table[i][key]
            new_table.append( [value, str(1)])
            
        i = i + 1

    return new_table


""" ***************** """
""" Command Execution """
""" ***************** """
def exec_command( cmd_line:str, table:list) -> list:
    """ Execute the given command (cmd_line) on table. 
        Return the transformed table. 
    """

    new_table = table.copy() # set new_table to a copy 
                             # and then override 
    token_list = cmd_line.split() 
    command = token_list[0] 

    if command == READ:
        new_table = read_csv( token_list[1])
        print_count( new_table)
    
    elif command in COMMANDS and len( table) == 0:
        print( "No table loaded... ")

    elif command == COLUMNS: 
        print_cols( new_table)

    elif command == PRINT:
        print_table( new_table)

    elif command == COUNT:
        print_count( new_table)

    elif command == PROJECT:
        new_table = project( table, token_list[1:])
        print_count( new_table)

    elif command == SORT:
        new_table = table.copy()
        sort( new_table, token_list[1])
        print_count( new_table)

    elif command == SAVE:
        save_csv( new_table, token_list[1])
        print_count( new_table)

    elif command == DISTR:
        new_table = distr( table, token_list[1])
        print_count( new_table)

    elif command == SELECT:
        new_table = select( table, token_list[1], token_list[2])
        print_count( new_table)

    else: 
        print( f"{command}: Command not recognized")

    return new_table


def main():

    # The table. We start with it empty. Each time a command 
    # is executed we create a new table. 
    table = []

    print( f"Starting... ")

    command = input( "Enter command: ").strip().lower()
    while command != "exit":
        if command.strip() != "":
            table = exec_command( command, table) 

        command = input( "Enter command: ").strip().lower()
    
    print( f"... Exiting")
    
main()