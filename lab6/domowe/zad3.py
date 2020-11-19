def validate_lab_score(lab_score):
    if not isinstance(lab_score, list):
        raise ValueError('lab_score is not a list!')


def validate_single_lab_score(score):
    if not isinstance(score, int) and not isinstance(score, float):
        raise ValueError('score in lab_score is not a number!')


def get_lab_points(lab_score):
    lab_points = lab_score
    try:
        validate_lab_score(lab_score)
        for score in lab_score:
            validate_single_lab_score(score)
    except:
        lab_points = None
    return lab_points


def get_sum_of_lab(student_score):
    pass


def get_student_avg_lab_percentage(student_score, max_lab_points):
    pass


def get_single_student_summary(student_score, max_lab_points):
    pass


def get_all_students_summary(students_scores, max_lab_points):
    pass


def get_all_students_avg_lab_score(students_scores):
    pass


def print_all_students_summary(students_scores, max_lab_points):
    pass


def print_all_students_avg_lab_score(students_scores):
    pass


max_lab = [10, 20, 30]
dane = [
    ("Adam Abacki", [5, 10, 15]),
    ("Basia Babacka", [10, 20, 30]),
    ("Cecylia Cabacka", [1, 2, 3])
]

get_all_students_summary(dane, max_lab)
