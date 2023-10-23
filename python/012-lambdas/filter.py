import statistics

sensor_data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Filter data of a collection
average = statistics.mean(sensor_data)
print(average)

res = filter(lambda x: x > average, sensor_data)

print(list(res))

names = ['Ana', 'Maria', 'Rita Lee']

print(list(map(lambda name: f'Teacher name: {name}', filter(lambda name: len(name) < 5, names))))
