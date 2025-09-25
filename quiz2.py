#
#
# Purchase BITCOIN
# Quiz 2, COMP 1701 F 2025
#

BTC = 159000.00


def main() -> None:
    """ Ask for a number of BTC to buy and return the cost. """

    print("Purchase BTC")

    btc_to_buy = float( input( "Enter the number of BTC to buy: (e.g. 1.03051): "))

    cdn_cost = BTC * btc_to_buy 

    print( f"\n\nYou want to purchase {btc_to_buy:,.8f} for ${cdn_cost:,.2f}\n\n")

main()
