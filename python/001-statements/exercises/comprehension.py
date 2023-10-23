def main():    
    st = "Create a list of the first letters of every word in this string".split(' ')
    my_st_list = [s[0] for s in st]
    print(my_st_list)
# end def

if __name__ == "__main__":
    main()