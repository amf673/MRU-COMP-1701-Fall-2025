#
# tracing example 
#

def f( a:int) -> str:
   """ categorizes numbers """
   category = ""
   if a < 0:
      category = "negative"
   elif a == 0: 
      category = "zero"
   else:
      category = "positive"

    return category

def g( x:int, a:str) -> bool:
    """ Returns a boolean """
    b = False
    if (x < 0 and a == "negative") or (x > 0 and a == "positive"):
        b = True
    return b

def main() -> None:
    a = int(input( "enter a number "))
    x = int(input( "enter another number"))

    cat = f(a)
    if g( x, cat):
        print( "We did it!")
    else:
        print( "We didnt do it")
    
main()
