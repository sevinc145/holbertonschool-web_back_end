#!/usr/bin/env python3
""" Auth module """

from os import getenv
from typing import List, TypeVar
from flask import request


class Auth:
    """ Auth class """

    def require_auth(self,
                     path: str,
                     excluded_paths: List[str]) -> bool:
        """ Checks if auth required """

        if path is None:
            return True

        if excluded_paths is None or excluded_paths == []:
            return True

        if path[-1] != '/':
            path += '/'

        for excluded_path in excluded_paths:
            if excluded_path == path:
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
        """ Returns a cookie value from request """

        if request is None:
            return None

        session_name = getenv("SESSION_NAME")

        return request.cookies.get(session_name)
