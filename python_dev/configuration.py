import os
import os.path
import configparser
from importlib.resources import path
import sys
from pathlib import Path

def check_includes(install_dir):
    for name in os.listdir(install_dir):
        dir = os.path.sep.join([install_dir, name])
        if os.path.isdir(dir):
            about_py = os.path.sep.join([dir, 'about.py'])
            if os.path.exists(about_py):
                configuration_py = os.path.sep.join([dir, 'configuration.py'])
                return os.path.exists(configuration_py)
    return False
                    

def _default_config(config):
    config['pyde'] = {
    }
    
def find(name):
    if not name or name == '':
        raise ValueError('The name of the configuration file to be found must be supplied')
    if os.path.exists(name):
        return os.path.abspath(name)
    cwd = os.getcwd()
    if os.path.exists(os.path.sep.join([os.path.dirname(cwd), name])):
        return os.path.abspath(os.path.sep.join([os.path.dirname(cwd), name]))
    exec_path = Path(sys.executable).parent
    if (os.path.exists(os.path.sep.join([str(exec_path), name]))):
        return os.path.abspath(os.path.sep.join([str(exec_path), name]))
    home = os.getenv('HOME', None)
    if (home and os.path.exists(os.path.sep.join([home, name]))):
        return os.path.abspath(os.path.sep.join([home, name]))
    
    raise FileNotFoundError('Unable to find a file named {file}'.format(file=name))
    
    
        
def read_config(name=None, env_key='PYDE_CFG'):
    config = configparser.ConfigParser()
    if name:
        config_name = name
    else:
        config_name = os.getenv(env_key, None)
    if not config_name:
        config_name = 'pyde.ini'       
    path = find(config_name)
    try:
        config.read(path)
    except Exception as e:
        print(e)
        print('Error in configuration file: {file}. Using default configs'.format(file=path))
        _default_config(config)
    return config

config = read_config()

