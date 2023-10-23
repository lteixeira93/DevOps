def main():
    """Nested List Comprehension"""
    my_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print([[value*2 for value in my_list] for my_list in my_lists])
    
    # Printing odds using comprehensions
    even = [x for x in num_list if not x % 2]
    print(even)
# end def

if __name__ == "__main__":
    main()
    