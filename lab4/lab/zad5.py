def get_binary_representation_length(x):
    return len(bin(x)[2:])  # skipping prefix 0b

print(get_binary_representation_length(2))
print(get_binary_representation_length(10))
