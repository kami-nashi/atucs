'''
UCS Tools common functions
'''

import os
import sys
import ConfigParser


def __file_exists(file_path):
    '''
    Check file exists
    '''
    try:
        with open(file_path):
            return True
    except IOError:
        return False


def get_configuration():
    '''
    Try to read configuration from all possible locations or fail
    '''
    config_file = ""
    if __file_exists('./ucs.cfg'):
        config_file = './ucs.cfg'
    elif __file_exists(os.path.expanduser('~/.config/ucs.cfg')):
        config_file = os.path.expanduser('~/.config/ucs.cfg')
    elif __file_exists('/etc/ucs.cfg'):
        config_file = '/etc/ucs.cfg'

    if config_file == "":
        print(
            'Configuration file (./ucs.cfg, ~/.config/ucs.cfg, /etc/ucs.cfg) not found, cannot continue!')
        sys.exit(1)
    else:
        config = ConfigParser.RawConfigParser()
        config.read(config_file)

        return config


def get_configured_envs(configuration):
    '''
    Get list of envs from configuration
    '''
    envs = []

    for env in configuration.sections():
        envs.append(env)

    return envs
