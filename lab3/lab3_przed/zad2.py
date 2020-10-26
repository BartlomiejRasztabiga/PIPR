def generate_filename(id: int) -> str:
    return f"data_{id:04}.txt"


# verifying results
print(list(map(lambda x: generate_filename(x), [0, 1, 23, 400, 1001])) == [
      'data_0000.txt', 'data_0001.txt', 'data_0023.txt', 'data_0400.txt', 'data_1001.txt'])
