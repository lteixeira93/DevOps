import collections
import uuid

Measurement = collections.namedtuple('Measurement', 'id x y value')

measurements = [
    Measurement(str(uuid.uuid4()), 1, 1, 72),
    Measurement(str(uuid.uuid4()), 2, 1, 40),
    Measurement(str(uuid.uuid4()), 3, 1, 11),
    Measurement(str(uuid.uuid4()), 2, 1, 90),
    Measurement(str(uuid.uuid4()), 2, 2, 60),
    Measurement(str(uuid.uuid4()), 2, 3, 73),
    Measurement(str(uuid.uuid4()), 3, 1, 40),
    Measurement(str(uuid.uuid4()), 3, 2, 44),
    Measurement(str(uuid.uuid4()), 3, 3, 90)
]

# Generator can be run just once
high_values = (
    m.value
    for m in measurements
    if m.value >= 70
)

print(high_values)

# It will return the len, it will store the whole list in memory which
# undo the generator
# print(len(list(high_values)))

# Pythonic counting, do not store in memory
counter = sum(1 for _ in high_values)
print(counter)
