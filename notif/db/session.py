from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from notif.config import DB_URI
from notif.db.models import Base


_engine = create_engine(DB_URI)
Base.metadata.bind = _engine

_db_session = sessionmaker(bind=_engine)

session = _db_session()
