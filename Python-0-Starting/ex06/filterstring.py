import sys
from ft_filter import ft_filter


def filterstring(s, c):
    """
    Function that takes a string and returns list of characters from the string
    that have a length greater than the specified integer c.
    """
    return list(ft_filter(lambda i: len(i) > c, s))


def main():
    """ Main function """
    if (len(sys.argv) != 3):
        raise AssertionError("the arguments are bad")
    larg = sys.argv[1].split(" ")
    if larg == [] or sys.argv[2].isdigit() is False:
        raise AssertionError("the arguments are bad")
    if [i for i in larg if i.isalpha() is False]:
        raise AssertionError("the arguments are bad")
    filtered = filterstring(sys.argv[1].split(" "), int(sys.argv[2]))
    print(filtered)


if __name__ == "__main__":
    main()
