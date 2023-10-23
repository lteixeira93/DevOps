from itertools import combinations_with_replacement

s, k = input().split()

combinations = list(combinations_with_replacement(sorted(s), int(k)))

# Unpacking tuple
for x in combinations:
    print(*x, sep='')

