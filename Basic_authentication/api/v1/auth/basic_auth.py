#!/usr/bin/env python3
""" Basic authentication module """

from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """ BasicAuth class """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """ Extract Base64 authorization header """

        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith('Basic '):
            return None

        return authorization_header.split('Basic ')[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ Decode Base64 authorization header """

        if base64_authorization_header is None:
            return None

        if not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded = base64.b64decode(
                base64_authorization_header
            )
            return decoded.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """ Extract user credentials """

        if decoded_base64_authorization_header is None:
            return (None, None)

        if not isinstance(
                decoded_base64_authorization_header, str):
            return (None, None)

        if ':' not in decoded_base64_authorization_header:
            return (None, None)

        user_email, user_pwd = (
            decoded_base64_authorization_header.split(':', 1)
        )

        return (user_email, user_pwd)

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str):
        """ Returns User object based on email and password """

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
