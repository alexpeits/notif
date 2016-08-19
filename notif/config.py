import os
from ConfigParser import SafeConfigParser
from ConfigParser import NoSectionError, NoOptionError


def bind_config(config_obj):

    config_obj = config_obj

    def get_conf_wrapper(section, key, default=None):
        try:
            return config_obj.get(section, key)
        except (NoOptionError, NoSectionError):
            return default

    return get_conf_wrapper


_CONF_FILENAME = 'config.ini'

_APP_DIR = os.path.abspath(os.path.dirname(__file__))

_USER_HOME = os.environ.get('HOME')
_LOCAL_CONF_DIR = os.path.join(_USER_HOME, '.notifrc')
if not os.path.exists(_LOCAL_CONF_DIR):
    os.mkdir(_LOCAL_CONF_DIR)

_APP_CONFIG = os.path.join(_APP_DIR, os.pardir, _CONF_FILENAME)
_LOCAL_CONFIG = os.path.join(_LOCAL_CONF_DIR, _CONF_FILENAME)
if os.path.exists(_LOCAL_CONFIG):
    _CONFIG = _LOCAL_CONFIG
else:
    _CONFIG = _APP_CONFIG

_config = SafeConfigParser()
_config.read(_CONFIG)
get_config = bind_config(_config)


# Defaults
_DEFAULT_DB_URI = 'sqlite:///{}'\
                  .format(os.path.join(_LOCAL_CONF_DIR, 'db.sqlite'))


# Main configuration
DB_URI = get_config('db', 'DB_URI', default=_DEFAULT_DB_URI)
