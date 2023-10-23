import collections
import datetime
import random

import sys

DataPoint = collections.namedtuple(typename="DataPoint", field_names="id, x, y, temp, quality")


def main():
    print("Creating data...", end=' ')
    sys.stdout.flush()

    data_list = []  # 500,000 DataPoint items
    random.seed(0)
    for d_id in range(500000):
        x = random.randint(0, 1000)
        y = random.randint(0, 1000)
        temp = random.randint(-10, 50)
        quality = random.random()
        data_list.append(DataPoint(d_id, x, y, temp, quality))

    print("done.")
    sys.stdout.flush()

    # Reordering data for random access
    print("Reordering data for random access ...", end=' ')
    sys.stdout.flush()

    data_list.sort(key=lambda d: d.quality)
    print("done.")

    # Creating set of interesting ids
    interesting_ids = {random.randint(0, len(data_list) - 1) for _ in range(0, 100)}
    print(interesting_ids)
    print("Creating {} interesting IDs to seek.".format(len(interesting_ids)))

    # Locating data in list
    print("Locating data in list...", end=' ')
    sys.stdout.flush()

    # 1. From data_list, create dictionary via comprehension, key = id
    data_dict = {d.id: d for d in data_list}

    # 2. locate the data in dictionary
    interesting_points = []
    for d_id in interesting_ids:
        d = data_dict[d_id]
        interesting_points.append(d)
    print(interesting_points)

if __name__ == '__main__':
    main()
