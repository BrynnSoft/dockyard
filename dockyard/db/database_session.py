import logging

from abc import ABC, abstractmethod
from sqlalchemy.orm import Session

from .engine import engine

from ..dependency_injection import di

_logger = logging.getLogger(__name__)

class DatabaseSession(ABC):
    @property
    @abstractmethod
    def session(self) -> Session:
        raise NotImplementedError()

class DatabaseSessionImpl(DatabaseSession):
    _session: Session

    def __init__(self) -> None:
        self._session = None
    
    def __del__(self):
        if self._session is not None:
            _logger.debug('Close DB Session')
            if not self._session.info.get('committed', False):
                _logger.info('Closing RW DB Session without Writing!')
            self._session.close()
    
    @property
    def session(self) -> Session:
        if self._session is None:
            _logger.debug('Open DB Session')
            self._session = Session(engine)
        return self._session

di.register_scoped(DatabaseSession, DatabaseSessionImpl)