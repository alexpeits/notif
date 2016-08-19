from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql.expression import false, true
import arrow

from notif.db.models import Notification
from notif.db.session import session
from notif.errors import NewNotificationError


UNIT_SEARCH = 'minutes'
TIME_DELTA_SEARCH = 15
UNIT_CLEAR = 'days'
TIME_DELTA_CLEAR = -2


def create_notification(subject, date, body):
    date = arrow.get(date, 'YYYY-MM-DD hh:mm:ss').replace(tzinfo='local')

    notification = Notification(subject=subject,
                                date=date,
                                body=body)
    session.add(notification)

    try:
        session.commit()
    except SQLAlchemyError:
        session.rollback()
        raise


def search_by_date(date=None):
    if date is None:
        date = arrow.utcnow()
    else:
        date = arrow.get(date, 'YYYY-MM-DD hh:mm:ss')\
                   .replace(tzinfo='local')
    margin = date.replace(**{UNIT_SEARCH: TIME_DELTA_SEARCH})

    query = session.query(Notification)\
            .filter(Notification.date <= margin.datetime)\
            .filter(Notification.displayed == false())

    return query.all()


def clear_notifications():
    now = arrow.utcnow()
    margin = now.replace(**{UNIT_CLEAR: TIME_DELTA_CLEAR})
    session.query(Notification)\
        .filter(Notification.displayed == true())\
        .filter(Notification.date <= margin.datetime)\
        .delete()
    session.commit()
