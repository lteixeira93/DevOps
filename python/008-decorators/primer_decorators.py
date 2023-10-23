def my_dec(func):
    def wrapper(*args, **kwargs):
        print("Before function calling")
        func(*args, **kwargs)
        print("After function calling")
        # return wrapper(*args, **kwargs)

    return wrapper()


@my_dec
def print_statement(name='decorated'):
    print(f"Executing my {name} function")


# The @functools.wraps decorator, which will preserve information about the original function.
# import functools
#
# def decorator(func):
#     @functools.wraps(func)
#     def wrapper_decorator(*args, **kwargs):
#         # Do something before
#         value = func(*args, **kwargs)
#         # Do something after
#         return value
#     return wrapper_decorator
