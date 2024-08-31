def ft_filter(f: any, n: list) -> list:
    """
    This function filters the elements.
    Of a sequence for which the function returns True.
    """
    if not callable(f):
        raise AssertionError("First argument must be a function")
    return [x for x in n if f(x)]


def main():
    """ Main function """
    print(ft_filter.__doc__)
    print(ft_filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))
    print(ft_filter(lambda x: x % 2 != 0, [1, 2, 3, 4, 5, 6]))
    print(ft_filter(lambda x: x > 0, [-1, 2, -3, 4, -5, 6]))
    print(ft_filter(lambda x: x < 0, [-1, 2, -3, 4, -5, 6]))
    # print(ft_filter("s", [-1, 2, -3, 4, -5, 6]))


if __name__ == "__main__":
    main()
