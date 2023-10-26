from functools import reduce


print(list(map(lambda x: x * 2, [1, 2, 3]))) # Return list of values -> All values multiplied by 2
print(reduce((lambda x, y: x if(x > y) else y), [1, 7, 99, 2, 3])) # Return one final value only -> The biggest