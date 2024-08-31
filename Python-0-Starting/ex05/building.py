import sys
import string


def get_input() -> str:
    """This function gets the input from the user"""
    print("What is the text to count?")
    s = input()
    return s


def count_characters(text) -> dict:
    """Count various types of characters in the text."""
    upper_count = sum(1 for c in text if c.isupper())
    lower_count = sum(1 for c in text if c.islower())
    punctuation_count = sum(1 for c in text if c in string.punctuation)
    space_count = text.count(' ')
    digit_count = sum(1 for c in text if c.isdigit())

    return {
        "upper": upper_count,
        "lower": lower_count,
        "punctuation": punctuation_count,
        "spaces": space_count,
        "digits": digit_count,
    }


def main():
    """This is the main function"""
    if len(sys.argv) > 2:
        raise AssertionError("less than one argument is provided")
    if len(sys.argv) == 2:
        s = sys.argv[1]
    else:
        s = get_input()
    counts = count_characters(s)

    print(f"The text contains {len(s)} characters:")
    print(f"{counts['upper']} upper letters")
    print(f"{counts['lower']} lower letters")
    print(f"{counts['punctuation']} punctuation marks")
    print(f"{counts['spaces']} spaces")
    print(f"{counts['digits']} digits")


if __name__ == "__main__":
    main()
