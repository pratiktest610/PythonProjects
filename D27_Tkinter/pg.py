def add(*args):
    sums = 0
    for n in args:
        sums += n
    return sums


print(add(2, 4, 5, 6))
