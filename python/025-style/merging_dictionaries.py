route = {'id': 271, 'title': 'Fast apps'}
query = {'id': 1, 'render_fast': True}
post = {'email': 'j@j.com', 'name': 'John'}

print("Individual dictionaries")
print(f"Route: {route}")
print(f"Query: {query}")
print(f"Post: {post}")

# Classic
merged_web_dict_classic = {}
merged_web_dict_classic.update(route)
merged_web_dict_classic.update(query)
merged_web_dict_classic.update(post)
print(f"Classic merged dicts: {merged_web_dict_classic}")

# Comprehension
merged_web_dict_comp = {k: v for d in [route, query, post] for k, v in d.items()}
print(f"Comp merged dicts: {merged_web_dict_comp}")

# Modern python 3.5+
merged_web_dict_modern = {**route, **query, **post}
print(f"Modern merged dicts: {merged_web_dict_modern}")
