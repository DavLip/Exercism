def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """

    for n in student_info:
        if n[1] != 100:
            continue
        else:
            return n

test = perfect_score(student_info=[["Charles", 90], ["Tony", 80], ["Alex", 100]])
print(test)