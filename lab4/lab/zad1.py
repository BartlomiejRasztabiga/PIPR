def power(a):
    return a**3

print(list(map(lambda x: power(x), [0, 1, -3, 2e3])))