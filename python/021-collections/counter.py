from collections import Counter

number_of_shoes = int(input())
shoe_sizes = [int(num) for num in input().split()]

number_of_customers = int(input())
shoe_size_and_price = []
for customers in range(0, number_of_customers):
    k, v = input().split()
    shoe_size_and_price.append({int(k): int(v)})

shoe_size_stock = dict(Counter(shoe_sizes).items())

profit_list = []
for inner_dict in shoe_size_and_price:
    for c_key, c_value in inner_dict.items():
        if c_key in shoe_size_stock:
            if shoe_size_stock[c_key] > 0:
                shoe_size_stock[c_key] -= 1
                profit_list.append(c_value)

print(sum(profit_list))
