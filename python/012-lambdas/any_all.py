# all() returns true if all elements of iter are true or if iter is empty
print(all([0, 1, 2, 3]))
print(all([1, 2, 3]))
print(all([]))

names = ["Carlos", "Camila", "Kassiano"]
print(all([name[0] == 'C' for name in names]))

# any() returns true if any elements of iter are true, if iter is empty returns false
print(all([0, 1, 2, 3]))
print(all([1, 2, 3]))
print(all([]))

names = ["Carlos", "Kamila", "Kassiano"]
print(any([name[0] == 'C' for name in names]))
