# 
# L6 - part1.py 
# 
# 

def sum_all() -> int:
    """
    Prompts the user to enter positive integers one at a time, then displays the
    number and the running total. Finishes when a negative number is entered.
    Returns the final total.
    """
    prompt = "Enter a positive integer to sum, or negative integer to finish: "
    number = int(input(prompt))  # the priming read
    total = 0

    while number >= 0:
        number = int(input(prompt))  # the internal read
        print(f"You entered {number}")
        total = total + number
        print(f"The running sum is {total}")

    return total


def main():
    total = sum_all()
    print(f"\nThe final sum is {total}")


main()
