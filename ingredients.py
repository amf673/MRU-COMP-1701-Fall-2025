# ingredients.py 
# 
# An incomplete cooking program. 
# 
# COMP 1701 
# Fall 2023 


def add_ingredient(item: str, quantity: float) -> str:
    """
    Returns a string indicating that ingredient type and quantity are added.
    """
    print(f"Added {quantity} grams of {item}.")

def main() -> None:
    ingredient = input("What ingredient would you like to add? ")
    quantity = float(input(f"How many grams of {ingredient} are needed? "))

    print(add_ingredient(ingredient, quantity))

main()