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
    except ValueError:
        return None


def get_sum_of_max_lab_points(max_lab_points):
    return sum(max_lab_points)


def get_student_avg_lab_percentage(student, max_lab_points):
    sum_of_lab = get_sum_of_lab(student)
    if sum_of_lab is None:
        return None

    return int(sum_of_lab / get_sum_of_max_lab_points(max_lab_points) * 100)


def get_single_student_summary(student, max_lab_points):
    sum_of_lab = get_sum_of_lab(student)
    avg_lab_percentage = get_student_avg_lab_percentage(
        student, max_lab_points)

    return (get_student_name(student), sum_of_lab, avg_lab_percentage)


def get_all_students_summary(students, max_lab_points):
    return list(map(lambda student: get_single_student_summary(student, max_lab_points), students))


def get_all_students_avg_lab_score(students):
    sum_of_students_scores = 0
    number_of_students = 0

    for student in students:
        student_lab_score = get_sum_of_lab(student)

        if student_lab_score is not None:
            sum_of_students_scores += student_lab_score
            number_of_students += 1

    return int(sum_of_students_scores / number_of_students)


def print_all_students_summary(students, max_lab_points):
    print(get_all_students_summary(students, max_lab_points))


def print_all_students_avg_lab_score(students):
    print(get_all_students_avg_lab_score(students))
