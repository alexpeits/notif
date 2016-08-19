#!/usr/bin/env python

import os
from subprocess import call

from notif.utils import search_by_date, clear_notifications
from notif.db.session import session
from notif.db.models import Notification


env = os.environ.copy()
env['DISPLAY'] = ':0'

ICON = 'task-due'
NOTIFY_SEND = '/usr/bin/notify-send'
ICON_ARG = '--icon={}'


def check_todo():

    todos = search_by_date()

    if todos:
        for task in todos:
            call([NOTIFY_SEND, ICON_ARG.format(ICON), task.subject, task.body],
                 env=env)
            task.displayed = True
            session.commit()

    clear_notifications()
