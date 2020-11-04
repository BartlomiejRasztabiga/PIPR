def generate_fuzz_list(n):
    return ["fuzz" if x % 3 == 0 else x for x in range(1, n+1)]


print(generate_fuzz_list(12))
