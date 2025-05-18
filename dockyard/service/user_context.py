from abc import ABC, abstractmethod
from flask import request, session
from werkzeug.exceptions import Unauthorized, Forbidden, BadRequest
from uuid import UUID

from ..db.models.users import User as DBUser

from ..db.read_only_database_session import ReadOnlyDatabaseSession
from ..dependency_injection import di
from ..enums.auth_mode import AuthMode
from ..utils.password_helper import context

from pprint import pprint

class UserContext(ABC):

    @abstractmethod
    def handle_auth(self, allowed_auth_modes: AuthMode):
        raise NotImplementedError()
    
    @property
    @abstractmethod
    def user(self) -> DBUser:
        raise NotImplementedError()
    

class UserContextImpl(UserContext):
    _ro_db: ReadOnlyDatabaseSession

    _user_id: UUID

    _user_cached: DBUser

    @di.inject
    def __init__(self, ro_db: ReadOnlyDatabaseSession):
        super().__init__()

        self._ro_db = ro_db

        self._user_id = None

        self._user_cached = None

    def handle_auth(self, allowed_auth_modes):
        if request.authorization is not None:
            if AuthMode.BasicAuth in allowed_auth_modes:
                if request.authorization.type == 'basic':
                    username = request.authorization.parameters.get('username')
                    password = request.authorization.parameters.get('password')
                    
                    user_for_username = self._ro_db.session.query(DBUser).filter(DBUser.username == username).one_or_none()

                    if user_for_username is not None:
                        # TODO handle Hash Updates
                        if context.verify(password, user_for_username.password_hash):
                            self._user_id = user_for_username.id
                            self._user_cached = user_for_username

                            return

            if AuthMode.BearerToken in allowed_auth_modes:
                if request.authorization.type == 'bearer':
                    token = request.authorization.token
                    raise NotImplementedError('Token Auth')
                    # TODO auth

        if AuthMode.Session in allowed_auth_modes:
            if 'user_id' in session:
                self._user_id = session['user_id']

                # TODO handle user disable

                return

        if AuthMode.Public in allowed_auth_modes:
            return
        
        raise Unauthorized()
    
    @property
    def user(self) -> DBUser:
        if self._user_cached is None:
            pass
        return self._user_cached
        

di.register_scoped(UserContext, UserContextImpl)