# Ex. 1
for num in range (10):
    print(num)
print()
    
# Ex. 2
for num in range (1, 10):
    print(num)
print()
    
# Ex. 3
for num in range (1, 10, 2):
    print(num)
print()

# Ex. 4
for num in range (10, 1, -1):
    print(num)
print()

# Ex. 5
r_list = list(range(10))
str_list = list("Geek Tech Guy")
str_geek = "Geek Tech Guy"
print(r_list)
print(str_list)

if 'G' in str_list:
    print(dict(zip(r_list, str_list)))
    
print(f'Count: {str_list.count("e")}')
print(f'Take last element: {r_list[-1]}')
print(f'Reverse: {r_list[::-1]}')
print(f'Pop: {r_list.pop()}')
print(f'Sort: {sorted(r_list, reverse=True)}')
split_list = str_geek.split()
print(f'Split: {split_list}')
print(f'Join: {"-".join(split_list)}')
print(f'Index (By value, index): {r_list.index(8, 4)}')
print(f'Index step: {r_list[::2]}')

# I have a string, want the last word to be the first
str_to_process = "Geek University Interview Study"
str_to_process = str_to_process.split()
print(str_to_process)
str_to_process = [str_to_process.pop()] + (str_to_process)
print(' '.join(str_to_process))

# I have a string, want the whole string to be reversed
str_to_process = "Geek University Interview Study"
print(' '.join(str_to_process.split()[::-1]))
print()