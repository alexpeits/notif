#!/usr/bin/env python

import argparse
import tempfile
from subprocess import call

from notif.utils import create_notification


def text_from_editor():
    EDITOR = 'nvim'
    with tempfile.NamedTemporaryFile(suffix=".tmp") as tf:
        code = call([EDITOR, tf.name])
        if code:
            raise ValueError('Something went wrong')
        tf.seek(0)
        body_text = tf.read()

    return body_text


def new_todo():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--subject', dest='subject', action='store',
                        type=str, required=True, help='Subject')
    parser.add_argument('-d', '--date', dest='date', action='store',
                        type=str, required=True, help='Date')
    parser.add_argument('-b', '--body', dest='body_flag', action='store_true',
                        default=False)

    args = parser.parse_args()

    if args.body_flag:
        body = text_from_editor()
    else:
        body = ''

    create_notification(subject=args.subject, body=body, date=args.date)
