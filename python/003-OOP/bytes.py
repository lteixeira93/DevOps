import math
from datetime import date


def compute(b):
    kib = 1024
    mib = kib * kib

    if (b < kib):
        return str(b)
    elif (b >= kib and b < mib):
        return str(math.floor(b / kib)) + " KiB"
    elif (b >= mib):
        return str(math.floor(b / mib)) + " MiB"


def datet(d):
    d


def spell(my_list):
    my_list = [x for x in my_list if x % 2 == 0]
    # return(sorted(my_list, reverse=True))
    return my_list[::-1]


if __name__ == '__main__':
    # # print(compute(1023))
    # print(compute(999999999))
    # # print(compute(1025))
    # print(compute(1048576))
    # # print(compute(1048577))

    # d = date(2023, 6, 2)
    # # print(d)
    # print(d.day)
    # new_day = d.day + 7
    # new_date = date(d.year, d.month, new_day)
    # print(new_date)

    m_list = [44, 32, 28, 26, 18, 4, 2, 2]
    # print(sorted(m_list, key=lambda even: reverse=True))
    print(spell(m_list))
