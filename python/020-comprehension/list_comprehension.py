def main():
    my_string = "Hello"
    
    # Without list comprehension
    my_list = []    
    for letter in my_string:
        my_list.append(letter)
        
    # With list comprehension
    my_list = [letter for letter in my_string]    
    print(my_list) 
    
    # More examples of list comprehension
    my_list = [x**2 for x in range(0, 11) if x%2 == 0]      
    print(my_list) 
    
    # Nested list comprehension
    my_list = [x*y for x in [10, 20, 30] for y in [1, 2, 3]]         
    print(my_list) 
        
# end def

if __name__ == "__main__":
    main()