def main():    
    for idx in range(1, 101):
        print(idx)
        if(idx%3 == 0):         
            print("Fizz".format(idx), end="")
        if(idx%5 == 0):         
            print("Buzz".format(idx), end="")
        print()
        
# end def

if __name__ == "__main__":
    main()