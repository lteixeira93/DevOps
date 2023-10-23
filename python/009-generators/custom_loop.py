def custom_loop(my_iterable):
    it = iter(my_iterable)
    
    while True:
        try:
            print(next(it))
        except StopIteration:
            break
# end def

my_iterable = "John Marston"
custom_loop(my_iterable)
            