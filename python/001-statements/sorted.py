users = [
    {"username": "Samuel", "tweets": ["Hoje eu bebi"]},
    {"username": "Luiz", "tweets": ["Eae men"]},
    {"username": "Johan", "tweets": ["Hallo"]},
    {"username": "Petterson", "tweets": ["Hey mate"]}    
]

print(users)
print(sorted(users, key=lambda users: users["username"], reverse=True))
