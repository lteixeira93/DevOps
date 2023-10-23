def foo(*args):
    # Returns args tuple  
    print(args)
    return sum(args)
# end def


def foo_2(**kwargs):
    # Returns args dict - Keyword arguments
    print(kwargs)
    if 'fruit' in kwargs:
        print("My fruit of choice is {}".format(kwargs['fruit']))
    else:
        print("Fruit not found")
# end def


def main():
    print(foo(10, 20, 324, 43))
    params = {
        'fruit': "apple",
        'veggie': "lettuce"
    }
    foo_2(**params)
# end def


if __name__ == "__main__":
    main()
