def validate_lab_score(lab_score):
    if not isinstance(lab_score, list):
        raise ValueError('lab_score is not a list!')


def validate_single_lab_score(score):
    if not isinstance(score, int) and not isinstance(score, float):
        raise ValueError('score in lab_score is not a number!')


def get_lab_points(lab_score):
    validate_lab_score(lab_score)
    for score in lab_score:
        validate_single_lab_score(score)

    return lab_score


def get_student_lab_score(student):
    return student[1]


def get_student_name(student):
    return student[0]


def get_sum_of_lab(student):
    try:
        lab_points = get_lab_points(get_student_lab_score(student))
        return sum(lab_points)
    except:
        return None


def get_sum_of_max_lab_points(max_lab_points):
    return sum(max_lab_points)


def get_student_avg_lab_percentage(student, max_lab_points):
    sum_of_lab = get_sum_of_lab(student)
    if sum_of_lab == None:
        return None

    return int(sum_of_lab / get_sum_of_max_lab_points(max_lab_points) * 100)


def get_single_student_summary(student, max_lab_points):
    sum_of_lab = get_sum_of_lab(student)
    avg_lab_percentage = get_student_avg_lab_percentage(
        student, max_lab_points)

    return (get_student_name(student), sum_of_lab, avg_lab_percentage)


def get_all_students_summary(students, max_lab_points):
    pass


def get_all_students_avg_lab_score(students):
    pass


def print_all_students_summary(students, max_lab_points):
    pass


def print_all_students_avg_lab_score(students):
    pass


max_lab = [10, 20, 30]
dane = [
    ("Adam Abacki", [5, 10, 15]),
    ("Basia Babacka", [10, 20, 30]),
    ("Cecylia Cabacka", [1, 2, 3])
]

get_all_students_summary(dane, max_lab)
