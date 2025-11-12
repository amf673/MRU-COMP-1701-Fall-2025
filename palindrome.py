## 
## Three different ways to determine if a string is a palindrome. 
## There is one more that is even shorter! 
##

def reverse( a_str:str) -> str: 
    """ Returns the reverse of a_Str """
  
    i = len(a_str) - 1
    new_str = ""
    while i >= 0: 
        new_str = new_str + a_str[i]
        i = i - 1
    return new_str

def palindrome( word:str) -> bool: 
    """ Returns true if a_str is a palindrome """
    
    palin_flag = True
    i = 0 
    while i < (len(word) // 2) - 1 and palin_flag:
        if word[i] != word[-1 * i]:
            palin_flag = False
        i = i + 1
    return palin_flag

def palindrome2( word:str) -> bool: 
    """ Returns true if a_str is a palindrome """
    
    return reverse( word) == word

def palindrome3( word:str) -> bool: 
    """ Returns true if a_str is a palindrome using recursion """
    
    if len(word) < 2:  
        # a word of length 1 or 0 is a palindrome
        return True
    elif word[0] != word[-1]: 
        # if the first letter does not equal the last letter it is not a palindrome
        return False
    else: 
        # the first and last characters are the same so check if the middle makes a palindrome
        return palindrome3( word[1:-1])
