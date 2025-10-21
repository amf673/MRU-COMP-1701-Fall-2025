def abstract_decisions(a: bool, b: bool, c: bool) -> None:
    """
    Takes three boolean arguments and combines them to print a result.
    Has no actual functionality.
    """
    if a or not b and c:
        print("expression is true")
    else:
        print("expression is false")

def main() -> None:
    abstract_decisions(False, True, True)

main()