import sys
from my_modules.util import util, get_data


def main(argv: list[str]):
    data = get_data(argv)
    print(data)
    return util(data)


if __name__ == '__main__':
    main(sys.argv)
