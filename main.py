
def round6(num):
    """This function has a bug in it"""
    return int(num + .4)


def upper_lower(text):
    """
    Checks if a given string contains an occurrence
    of upper case letter followed by lower case letter.
    Returns True if such thing exists, False otherwise.
    """
    for i in range(0, len(text)):
        if text[i].isupper():
            try:
                if text[i+1].islower():
                    return True
            except IndexError:
                return False
    return False


def sumnums(lo, hi):
    """Returns the sum of the numbers in the range [lo..hi]
    Precondition: lo <= hi
    """
    pass


def main() -> None:
    print(round6(3.5)) # 3
    print(round6(3.6)) # 4


if __name__ == '__main__':
    main()
