from itertools import permutations

s, k = input().split()
k = int(k)

# Unpacking tuple
for x in [x for x in list(permutations(sorted(s), k))]:
    print(*x, sep='')
