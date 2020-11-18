def is_sequence_one_element(sequence):
    return len(sequence) == 1


def get_max_consistent_subsequence(sequence):
    best_sum = 0
    best_start = 0
    best_end = 0

    current_sum = 0

    for current_end, x in enumerate(sequence):
        if current_sum <= 0:
            # Start a new sequence at the current element
            current_start = current_end
            current_sum = x
        else:
            # Extend the existing sequence with the current element
            current_sum += x

        if current_sum > best_sum:
            best_sum = current_sum
            best_start = current_start
            best_end = current_end + 1  # the +1 is to make 'best_end' exclusive

    max_consistent_subsequence = sequence[best_start:best_end]
    is_one_element = is_sequence_one_element(sequence)

    return sequence if is_one_element else max_consistent_subsequence
