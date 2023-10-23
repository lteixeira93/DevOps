def main():
    list_numbers = [1, 2, 3, 4, 5] # Extra will be ignored
    list_letters = ['a', 'b', 'c']
    list_hundreds = [100, 200, 300]
    
    for item in zip(list_numbers, list_letters, list_hundreds):
        print(item)
        
    print(list(zip(list_numbers, list_letters, list_hundreds)))
    
    data = [(1 , 6), (4 , 1), (5 , 22), (9 , 3), (19 , 43)]
    print(list(zip(*data)))
    
    test_1 = [43, 42, 11]
    test_2 = [41, 11, 100]
    students = ["Maria", "Luiz", "Johan"]
    
    final = {data[0]: max(data[1], data[2]) for data in zip(students, test_1, test_2)}
    print(final)
# end def

if __name__ == "__main__":
    main()