from functools import reduce

data = [2, 3, 4, 5, 6, 7, 8, 9]

multi = lambda x, y: x * y
res = reduce(multi, data) # Same as map and filter but for two parameters function
print(res)
