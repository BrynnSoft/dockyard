import logging
from abc import ABC, abstractmethod
from random import choice
from sqlalchemy.orm import Session

from .engine import ro_engine, engine

from ..dependency_injection import di

_logger = logging.getLogger(__name__)

# Temp setup - Needs improvement
_ENGINES = [engine, ro_engine, ro_engine]

class ReadOnlyDatabaseSession(ABC):
    @property
    @abstractmethod
    def session(self) -> Session:
        raise NotImplementedError()

class ReadOnlyDatabaseSessionImpl(ReadOnlyDatabaseSession):
    _session: Session

    def __init__(self) -> None:
        self._session = None
    
    def __del__(self):
        if self._session is not None:
            _logger.debug('Closing RO DB Session {%x}', id(self))
            self._session.close()
    
    @property
    def session(self) -> Session:
        if self._session is None:
            selected_engine = choice(_ENGINES)
            _logger.debug('Open RO DB Session {%x} - "%s"', id(self), selected_engine.url.host)
            self._session = Session(selected_engine)
        return self._session
    
di.register_scoped(ReadOnlyDatabaseSession, ReadOnlyDatabaseSessionImpl)