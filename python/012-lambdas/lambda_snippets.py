mk_names_list = ['Shang Tsung', 'Kung Lao', 'kitana', 'liu Kang', 'Johnny Cage']

mk_sorted_names_list = sorted(mk_names_list, key=lambda i: i.lower())
print(mk_sorted_names_list)

# Using map
mk_lower_names_list = map(lambda i: i.lower(), mk_names_list)
print(list(mk_lower_names_list))
