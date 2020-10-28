def get_elapsed_time_description(name, exercise_number, elapsed_time):
    is_probably_female = name[-1] == 'a'
    female_verb_suffix = 'a' if is_probably_female else ''

    elapsed_seconds = elapsed_time / 1000

    return f"{name} wykonał{female_verb_suffix} zadanie nr {exercise_number} w {elapsed_seconds:.3f} s."


print(get_elapsed_time_description('Agata', 2, 12305200))
print(get_elapsed_time_description('Tomek', 1, 123052))
