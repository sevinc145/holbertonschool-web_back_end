def user_object_from_credentials(
        self, user_email: str, user_pwd: str):
    """ Returns User object from credentials """

    if user_email is None or not isinstance(user_email, str):
        return None

    if user_pwd is None or not isinstance(user_pwd, str):
        return None

    from models.user import User

    try:
        users = User.search({"email": user_email})
    except Exception:
        return None

    if len(users) == 0:
        return None

    user = users[0]

    if not user.is_valid_password(user_pwd):
        return None

    return user
