from itertools import combinations

s, k = input().split()
k = int(k)

# Unpacking tuple
for x in [y for x in
          list(combinations(sorted(s), k)
               for k in range(1, k + 1))
          for y in x]:
    print(*x, sep='')
