def get_letter_occurences(word):
    occurences = dict()
    for letter in word:
        if letter in occurences:
            occurences[letter] += 1
        else:
            occurences[letter] = 1
    return occurences


print(get_letter_occurences('kukułka'))
