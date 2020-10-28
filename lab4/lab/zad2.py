def get_polynomial_value(a, b, c, x):
    return a*x**2 + b*x + c


print(list(map(lambda x: get_polynomial_value(1, 0, 0, x), [0, 1, 2])))
