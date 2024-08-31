import sys

def whatis(x) -> None:
    if x % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
    

def is_integer(value) -> bool:
    try:
        int(value)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    assert len(sys.argv) > 1, "less than one argument is provided"
    assert len(sys.argv) == 2, "more than one argument is provided"
    assert is_integer(sys.argv[1]), "argument is not an integer"
    whatis(int(sys.argv[1]))
