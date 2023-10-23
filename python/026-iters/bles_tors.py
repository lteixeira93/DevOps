import itertools
from itertools import combinations

n = int(input())
s = input().split()
k = int(input())


def get_values(iterables, key):
    return list(filter(lambda x: key in x, iterables))


a_indexes = [idx + 1 for idx, a in enumerate(s) if a == 'a']
all_indexes = list(combinations([x for x in range(1, n + 1)], k))

result_list = []
for x in a_indexes:
    result_list.append(get_values(all_indexes, x))

print(len(set(itertools.chain.from_iterable(result_list))) / len(all_indexes))
