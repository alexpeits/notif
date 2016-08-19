from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text, Boolean
from sqlalchemy_utils import ArrowType

from notif.config import DB_URI


Base = declarative_base()


class Notification(Base):
    """Notification database table."""

    __tablename__ = 'notifications'

    if 'sqlite' in DB_URI:
        __table_args__ = {'sqlite_autoincrement': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    subject = Column(Text, nullable=False)
    body = Column(Text, nullable=True)
    date = Column(ArrowType, nullable=False)
    displayed = Column(Boolean, default=False)
