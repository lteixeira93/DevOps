def function(x):
    return 3 * x + 1


# end def

def f_square(a, b, c):
    return lambda x: a * x ** 2 + b * x + c


# end def

def main():
    # Without lambda
    print(function(4))

    # With lambda
    calc = lambda x: 3 * x + 1

    print(calc(4))

    authors = ['Luiz Teixeira', 'Beatriz Castro', 'Mike Ross', 'Donna Bella']
    authors.sort(key=lambda a_name: a_name.split()[-1].lower())
    print(authors)

    test = f_square(2, 3, -5)
    print(test(0))
    print(test(1))

    print(f_square(2, 3, -5)(0))


# end def

if __name__ == "__main__":
    main()
