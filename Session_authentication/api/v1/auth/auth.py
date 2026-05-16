#!/usr/bin/env python3
""" Auth module """

from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """ Auth class """

    def require_auth(self, path: str,
                     excluded_paths: List[str]) -> bool:
        """ Checks if path requires authentication """

        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        if not path.endswith('/'):
            path += '/'

        if path in excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Returns authorization header """

        if request is None:
            return None

        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ Returns current user """

        return None

    def session_cookie(self, request=None):
        """ Returns cookie value """

        if request is None:
            return None

        session_name = getenv("SESSION_NAME")

        return request.cookies.get(session_name)
