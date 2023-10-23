# [k for k, g in groupby('AAAABBBCCDAABBB')] --> A B C D A B    -------- KEY
# [list(g) for k, g in groupby('AAAABBBCCD')] --> AAAA BBB CC D -------- GROUP

# Define a printer for comparing outputs
# def print_groupby(iterable, keyfunc=None):
#   for k, g in it.groupby(iterable, keyfunc):
#       print("key: '{}'--> group: {}".format(k, list(g)))

# # Feature A: group consecutive occurrences
# print_groupby("BCAACACAADBBB")

# key: 'B'--> group: ['B']
# key: 'C'--> group: ['C']
# key: 'A'--> group: ['A', 'A']
# key: 'C'--> group: ['C']
# key: 'A'--> group: ['A']
# key: 'C'--> group: ['C']
# key: 'A'--> group: ['A', 'A']
# key: 'D'--> group: ['D']
# key: 'B'--> group: ['B', 'B', 'B']
#
# # Feature B: group all occurrences
# print_groupby(sorted("BCAACACAADBBB"))

# key: 'A'--> group: ['A', 'A', 'A', 'A', 'A']
# key: 'B'--> group: ['B', 'B', 'B', 'B']
# key: 'C'--> group: ['C', 'C', 'C']
# key: 'D'--> group: ['D']
#
# # Feature C: group by a key function
# islower = lambda s: s.islower()                      # equivalent
# def islower(s):
#   """Return True if a string is lowercase, else False."""
#   return s.islower()
# print_groupby(sorted("bCAaCacAADBbB"), keyfunc=islower)

# key: 'False'--> group: ['A', 'A', 'A', 'B', 'B', 'C', 'C', 'D']
# key: 'True'--> group: ['a', 'a', 'b', 'b', 'c']

# groupby objects yield key-group pairs where the group is a generator.
from itertools import groupby

s = '1222311'
occurrence_list = []

key_list = [int(key) for key, _ in groupby(s)]
group_list = [list(group) for _, group in groupby(s)]

[occurrence_list.append(len(group)) for group in group_list]

for x in list(zip(occurrence_list, key_list)):
    print(x, end=' ')

print(*[(len(list(group)), int(key)) for key, group in groupby(input())])
