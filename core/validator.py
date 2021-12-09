from functools import wraps


def mentor_authentication(user):
    if not user.user_type == "mentor":
        return False

    return True


def student_authentication(user):
    if not user.user_type == "student":
        return False

    return True