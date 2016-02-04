"""
Get podcast config info.

       Created: 2016-07-04 13:02
 Last modified: 2016-02-04 13:45
"""
import os
try:
    import configparser as cp
except ImportError:
    import ConfigParsers as cp

REQUIRED_CONFIG = {'url': 'The URL of the initial feed',
                   'folder': 'The folder to write to'}

# Python2/3 user interaction
input = input if input else raw_input


def get_config(file):
    """Return a config parser class with config.

    If file is empty, request defaults from user and write to file.

    :file:    The config file to use.
    :returns: Dictionary of config params
    """
    file = os.path.abspath(os.path.expanduser(file))
    conf = cp.ConfigParser()
    if os.path.isfile(file):
        conf.read(file)
        for i in REQUIRED_CONFIG:
            if i not in conf['DEFAULT']:
                j = input('{} is a required config parameter\n.'.format(i) +
                          '{}: '.format(REQUIRED_CONFIG[i]))
    else:
        for arg, help in REQUIRED_CONFIG.items():
            conf['DEFAULT'][arg] = input(help + ': ')
    conf['DEFAULT']['folder'] = os.path.abspath(
        os.path.expanduser(conf['DEFAULT']['folder']))
    if not os.path.exists(conf['DEFAULT']['folder']):
        os.mkdir(conf['DEFAULT']['folder'])
    if not os.path.isdir(conf['DEFAULT']['folder']):
        raise ConfigError('{} is not a folder.'.format(
            conf['DEFAULT']['folder']))
    with open(file, 'w') as fout:
        conf.write(fout)
    config = {}
    for key, value in conf['DEFAULT'].items():
        config[key] = value
    return config


class ConfigError(Exception):

    """Failure in the config."""

    pass
