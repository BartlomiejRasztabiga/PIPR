def get_indices_of_given_chars(text, chars_list):
    result = []
    for char in text:
        if char not in chars_list:
            result.append(-1)
        else:
            result.append(chars_list.index(char))
    return result


sample_text = 'Ala ma kota'
sample_list = ['a', 'A', ' ', 'k']
print(get_indices_of_given_chars(sample_text, sample_list))