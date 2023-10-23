def main():
    d = {'k1':1, 'k2':2}
    
    print({x:x**2 for x in range(10)})
    print({k:v**2 for k, v in zip(['a','b'], range(2))})
    
    for k in d.items():
        print(k)
# end def

if __name__ == "__main__":
    main()