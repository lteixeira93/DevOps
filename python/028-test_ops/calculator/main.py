from Calculator import Calculator
from DisplayViewer import DisplayViewer


def main():
    display = DisplayViewer(0)
    print(display.errorCode)

    calculator = Calculator(display)

    sum_elem = calculator.sum(5, 6)
    subtract = calculator.subtract(10, 5)

    print("Main Result: ", sum_elem)
    print("Main Result: ", subtract)


if __name__ == '__main__':
    main()
