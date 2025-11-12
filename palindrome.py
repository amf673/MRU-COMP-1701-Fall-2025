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
    """ Returns true if word is a palindrome """
    
    is_palindrome = True # assume it is a palindrome
    i = 0 
    # Only need to compare the first half to the second
    # if len = 1 or 0 then (len(word) // 2) = 0 and the loop will not execute 
    # and is_palindrome will remain True
    while i < (len(word) // 2) - 1 and is_palindrome:
        if word[i] != word[-1 * i]:
            is_palindrome = False
        i = i + 1
    return is_palindrome

def palindrome2( word:str) -> bool: 
    """ Returns true if word is a palindrome """
    
    return reverse( word) == word

def palindrome3( word:str) -> bool: 
    """ Returns true if word is a palindrome using recursion """
    
    if len(word) < 2:  
        # a word of length 1 or 0 is a palindrome
        return True
    elif word[0] != word[-1]: 
        # if the first letter does not equal the last letter it is not a palindrome
        return False
    else: 
        # the first and last characters are the same so check if the middle makes a palindrome
        return palindrome3( word[1:-1])
