try:
    f = open('testfile', 'r')
    f.write("Test line")
except TypeError:
    print("Type Error exception")
except OSError:
    print("OS Error exception")   
else:
    print("Open file OK!")   
finally:
    print("Always run")  