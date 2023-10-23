# aka Tuple comprehension
# Generators allow you to create iterators in a very pythonic manner.
# Iterators allow lazy evaluation, only generating the next element of an iterable object when requested. This is useful for very large data sets.
# Iterators and generators can only be iterated over once.
# Generator Functions are better than Iterators.
# Generator Expressions (Comprehensions) are better than Iterators (for simple cases only).

def create_cubes(n):  
    # Yield does not store in memory 
    for x in range(n):
        yield x**3
# end def

def main():   
    g = create_cubes(10)
    print(next(g)) 
    print(next(g)) 
    print(next(g)) 
    # for x in create_cubes(10):
    #     print(x)
    
    s = 'Iterator_sample'
    s_iter = iter(s)
    print(next(s_iter)) 
    print(next(s_iter)) 
    print(next(s_iter)) 
    print(next(s_iter)) 
    
    # Tuple comprehension - Generator - Use less resource
    names = ["Carlos", "Kamila", "Kassiano"]
    res = (name[0] == 'C' for name in names)
    print(res)
    print(tuple(res))
    
    from sys import getsizeof
    
    list_comp = getsizeof([x * 10 for x in range(1000)])
    set_comp = getsizeof({x * 10 for x in range(1000)})
    dict_comp = getsizeof({x: x * 10 for x in range (1000)})
    gen_tuple_comp = getsizeof(x for x in range(1000))
    
    print("Memory usage:")
    print(f"List comprehension={list_comp}, Set comprehension={set_comp}, Dict comprehension={dict_comp}, Tuple comprehension={gen_tuple_comp}")
    
    # Memory waste
    nums_list_comprehension = [i * i for i in range(100_000)]
    sum(nums_list_comprehension) # 333333328333333350000000
    
    # Memory saver
    nums_generator = (i * i for i in range(100_000)) # <generator object <genexpr> at 0x106ecc580>
    sum(nums_generator) # 333333328333333350000000
    
    print(getsizeof(nums_generator)) # 112 bytes
    print(getsizeof(nums_list_comprehension)) # 835128600 bytes
# end def

if __name__ == "__main__":
    main()
    