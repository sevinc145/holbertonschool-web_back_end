#!/usr/bin/env python3
""" Basic authentication module """

from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """ BasicAuth class """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """ extracts base64 authorization header """

        if authorization_header is None:
            return None

        if type(authorization_header) is not str:
            return None

        if not authorization_header.startswith('Basic '):
            return None

        return authorization_header.split('Basic ')[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ decodes base64 authorization header """

        if base64_authorization_header is None:
            return None

        if type(base64_authorization_header) is not str:
            return None

        try:
            decoded = base64.b64decode(
                base64_authorization_header)
            return decoded.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """ extracts user credentials """

        if decoded_base64_authorization_header is None:
            return (None, None)

        if type(decoded_base64_authorization_header) is not str:
            return (None, None)

        if ':' not in decoded_base64_authorization_header:
            return (None, None)

        user_email, user_pwd = decoded_base64_authorization_header.split(':', 1)

        return (user_email, user_pwd)
