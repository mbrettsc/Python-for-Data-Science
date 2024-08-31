import sys


NESTED_MORSE = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
    "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    " ": "/"
}


def text_to_morse(text):
    for i, c in enumerate(text):
        print(NESTED_MORSE[c.upper()], end="" if i == len(text) - 1 else " ")


def main():
    if len(sys.argv) != 2:
        raise AssertionError("the arguments are bad")
    text = sys.argv[1]
    if [i for i in text.split(" ") if i.isalpha() is False]:
        raise AssertionError("the arguments are bad")
    text_to_morse(text)


if __name__ == "__main__":
    main()
