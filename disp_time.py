#
# Display time! 
#
# COMP 1701
# A. Fedoruk

SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR = SECONDS_IN_MINUTE * 60
SECONDS_IN_DAY = SECONDS_IN_HOUR * 24 

def main() -> None:
    """ """
    seconds = int(input(" Enter the number of seconds: "))

    days = seconds // SECONDS_IN_DAY
    remainder = seconds % SECONDS_IN_DAY

    hours = remainder // SECONDS_IN_HOUR
    remainder = remainder % SECONDS_IN_HOUR

    min = remainder // SECONDS_IN_MINUTE
    remainder = remainder % SECONDS_IN_MINUTE

    # print( seconds, "seconds is", days, hours, min, remainder)
    print( f"{seconds} seconds is {days}d {hours:02d}:{min:02d}:{remainder:02d}")

main()
