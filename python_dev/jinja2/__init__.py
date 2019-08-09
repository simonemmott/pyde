from jinja2 import Environment, FileSystemLoader, ChoiceLoader
import os
import os.path
import inspect
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

def _get_template_location():
    init_loc = os.path.abspath(inspect.getfile(inspect.currentframe()))
    jinja2_loc = Path(init_loc).parent
    return os.path.sep.join([str(jinja2_loc), 'templates'])

_templates = [_get_template_location()]

def add_templates(*additional_templates):
    _templates.extend(additional_templates)
    
def secret(length=30):
    return ''.join(random.choice('abcdefghighjklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for i in range(length))

def environment(**options):
    options['trim_blocks'] = options.get('trim_blocks', True)
    options['lstrip_blocks'] = options.get('lstrip_blocks', True)
    env = Environment(**options)
    env.globals.update({
        'secret': secret,
    })
    return env

def _configured_environment():
    logger.info('Loading templates from {dir}'.format(dir=_templates))
    loaders = []
    for templates in _templates:
        loaders.append(FileSystemLoader(templates))
    return environment(loader=ChoiceLoader(loaders))
    

env = _configured_environment()