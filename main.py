
def round6(num):
    """This function has a bug in it"""
    return int(num + .6)


def main() -> None:
    print(round6(3.5)) # 3
    print(round6(3.6)) # 4


if __name__ == '__main__':
    main()
