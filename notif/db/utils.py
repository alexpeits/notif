from sqlalchemy import create_engine

from notif.config import DB_URI
from notif.db.models import Base


def create_tables():
    """Create the database tables."""
    engine = create_engine(DB_URI)
    Base.metadata.create_all(engine)
