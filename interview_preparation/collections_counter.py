from collections import Counter
import re

# Ex. 1
t_list = [1, 1, 1, 3, 33, 4, 5, 6, 7, 3, 3, 23, 2, 76, 1]
print(f'Pop: {t_list.pop(3)}')
print(t_list)
c_type = Counter(t_list)

print(dict(c_type.most_common(3)))
print(f"Elements: {list(c_type.elements())}")
print(f"Values: {c_type.values()}")

# Is anagram
str_1 = 'earth'
str_2 = 'hearT'

str_2_c = Counter(str_2)
str_2_c['h'] -= 0
str_2 = str_2_c

print(Counter(str_1).values())
print(Counter(str_2).values())

if list(Counter(str_1).values()) == list(Counter(str_2).values()):
    print("Is anagram")

# Is palindrome
str_1 = "A man, a plan, a canal: Panamx"
str_1_cleared_list = []

for text in str_1.lower().split():
    str_1_cleared_list.append(((re.sub(r'\W+', '', text))))

if ''.join(str_1_cleared_list) == ''.join(str_1_cleared_list[::-1]):
    print("Is palindrome")
