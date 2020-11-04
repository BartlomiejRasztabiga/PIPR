def get_gcd(m, n):
    while n > 0:
        m, n = n, m % n
    return m


print(get_gcd(26, 52))
