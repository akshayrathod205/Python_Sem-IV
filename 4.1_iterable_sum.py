def sum_iterable(*args):
    s = 0
    for iterable in args:
        if type(iterable) == dict:
            for item in iterable:
                s += iterable[item]
        else:
            for item in iterable:
                s += item
    return s

a = sum_iterable([40, 30, 20, 10], [20, 10])
print(a)
