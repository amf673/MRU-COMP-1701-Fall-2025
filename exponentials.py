#
# Exponential Functions 
# COMP 1701 Fall 2025
# 
# A. Fedoruk
#

PAPER_THICKNESS = 0.0001 # thickness of a sheet of paper in m (0.1 mm)
M_PER_KM = 1000
M_PER_AU = 149597870700
M_PER_LY = 9.4607e+15

def compound( p_0:float, rate:float, time:float) -> float:
    """ Return the value of a initial value compounding. 
        Parameters: 
             p_0 (float): the intial value
             rate (float): the compounding rate (e.g. 0.05 for 5%)
             time (float): the number of steps to compound
        Returns: 
             p (float) the compounded value. """
  
    p = p_0 * (1 + rate)**time
    return p


def doubling( p_0:float, time:float) -> float: 
    """ Returns a value after a number of doublings. 
    Parameters: 
             p_0 (float): the intial value
             time (float): the number of times to double
        Returns: 
             p (float) the doubled value. """
  
    return compound( p_0, 1, time)


def main() -> None: 
   # input
   initial_investment = float(input("Enter the initial value of the investment: "))
   rate = float(input("Enter the interest rate: "))
   time = float(input("Enter the number of years to invest: "))

   # processing 
   investment_value = compound( initial_investment, rate, time)

   # output:  note the line continuation \ 
   print("An investment of", initial_investment, "at", rate * 100, \
            "% will be worth", round(investment_value,2), "after", time, "years.")
   #
   # Paper folding 
   # 
   folds = int( input( "Enter the number of folds: ")) 
   folded_thickness = doubling(PAPER_THICKNESS, 100)
   folded_km = folded_thickness / M_PER_KM
   folded_au = folded_thickness / M_PER_AU 
   folded_ly = folded_thicness / M_PER_LY

   print( f"The folded paper will be {folded_thickness:,.2f} m, {folded_km:,.2f} km, {folded_au:,.2f} AU, or {folded_ly:,.2f} LY")
    
main()
