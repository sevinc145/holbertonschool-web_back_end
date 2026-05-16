#!/usr/bin/env python3
""" Session authentication module """

from uuid import uuid4
from models.user import User
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """ Session authentication class """

    user_id_by_session_id = {}

    def create_session(self, user_id=None):
        """ Creates a Session ID """

        if user_id is None:
            return None

        if type(user_id) is not str:
            return None

        session_id = str(uuid4())

        self.user_id_by_session_id[session_id] = user_id

        return session_id

    def user_id_for_session_id(self, session_id=None):
        """ Returns a User ID based on a Session ID """

        if session_id is None:
            return None

        if type(session_id) is not str:
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ Returns a User instance based on a cookie value """

        session_cookie = self.session_cookie(request)

        user_id = self.user_id_for_session_id(session_cookie)

        if user_id is None:
            return None

        return User.get(user_id)

    def destroy_session(self, request=None):
        """ Deletes the user session / logout """

        if request is None:
            return False

        session_id = self.session_cookie(request)

        if session_id is None:
            return False

        user_id = self.user_id_for_session_id(session_id)

        if user_id is None:
            return False

        del self.user_id_by_session_id[session_id]

        return True
