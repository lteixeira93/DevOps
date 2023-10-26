aa_list = [12, 4, 53, 3, 45]

print(all(list(map(lambda x: x > 3, aa_list))))

# Any return True if any value from iterable is true
print(any(list(map(lambda x: x > 4, aa_list))))


# Remove repeated values from a list
r_list = list(range(0, 10))
r_list += list(range(0, 10, 2))

print(r_list)
print(list(set(r_list)))