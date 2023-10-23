from collections import defaultdict

data = {"year": 2001, "country": "USA", "title": "Johnny 5", "duration": "119 min"}

# Avoiding key error
yr = data.get('year', 0)
ra = data.get('rating', -1)
print(yr, "and", ra)

# Or

data = defaultdict(lambda: "MISSING", data)
print('accept default value instead style')
print(data['year'])
print(data['rating'])
print()
