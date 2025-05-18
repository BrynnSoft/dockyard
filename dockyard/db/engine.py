from os import environ as env
from sqlalchemy import create_engine, event
from sqlalchemy.orm import Session

from ..utils import strtobool

DATABASE_URI=env.get('DATABASE_URI')
DATABASE_URI_RO=env.get('DATABASE_URI_RO')
DATABASE_ECHO=bool(strtobool(env.get('DATABASE_ECHO', 'false')))

engine = create_engine(DATABASE_URI, echo=DATABASE_ECHO)

if DATABASE_URI_RO is None:
    ro_engine = engine
else:
    ro_engine = create_engine(DATABASE_URI_RO, echo=DATABASE_ECHO)

@event.listens_for(Session, 'after_commit')
def record_commit(session: Session):
    session.info['committed'] = True