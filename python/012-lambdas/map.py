import math

def area(r):
    return math.pi*(r**2)
# end def

def main():
    print(area(2))
    print(area(5.3))
    
    # Mapping values to functions
    r = [2, 5, 7.1, 0.3, 10, 44]
    areas = map(area, r)
    print(list(areas))
    
    # Now with lambda
    a = lambda r: math.pi*(r**2)
    areas = map(a, r)
    print(list(areas))
    
    # Note: After using map() (ex. list(areas)) first usage the memory for map is deleted   
#end def

if __name__ == "__main__":
    main()
    