import os
import configparser
from importlib.resources import path
import sys
from pathlib import Path

config_name = '{{meta.name}}'                   
    
def _default_config(config):
    config[config_name] = {
    }
    
def find(name):
    if not name or name == '':
        raise ValueError('The name of the file to be found must be supplied')
    if os.path.exists(name):
        return os.path.abspath(name)
    exec_path = Path(sys.executable).parent
    if (os.path.exists(os.path.sep.join([str(exec_path), name]))):
        return os.path.abspath(os.path.sep.join([str(exec_path), name]))
    home = os.getenv('HOME', None)
    if (home and os.path.exists(os.path.sep.join([home, name]))):
        return os.path.abspath(os.path.sep.join([home, name]))
    
    raise FileNotFoundError('Unable to find a file named {file}'.format(file=name))
    
    
        
def read_config(name=None, env_key='{{meta.name.upper()}}_CFG'):
    config = configparser.ConfigParser()
    if not name:
        name = os.getenv(env_key, None)
    if not name:
        name = config_name+'.ini'       
    try:      
        path = find(config_name)
    except FileNotFoundError:
        print('Unable to find configuration file: {file}. Using default config'.format(file=name))
        _default_config(config)
        return config
    try:
        config.read(path)
    except Exception as e:
        print(e)
        print('Error in configuration file: {file}. Using default configs'.format(file=path))
        _default_config(config)
    return config

config = read_config()

