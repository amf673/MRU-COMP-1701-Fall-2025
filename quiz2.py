#
# Purchase BITCOIN
# Quiz 2, COMP 1701 Fall 2025
#

# The current price of 1 Bitcoin (actually over $170,000.00 today). 
BTC = 159000.00

def btc_cost( btc_to_purchase: float) -> float:
    """ Return the cost to purchase btc_to_purchase BTC """
    return BTC * btc_to_purchase

def main() -> None:
    """ Ask for a number of BTC to buy and return the cost in Canadian $. """

    print("Purchase BTC")

    # input section
    btc_to_buy = float( input( "Enter the number of BTC to buy: (e.g. 1.03051): "))

    # processing section 
    cdn_cost = btc_cost( btc_to_buy)

    # output section 
    print( f"\n\nYou want to purchase {btc_to_buy:,.8f} for ${cdn_cost:,.2f}\n\n")

main()
