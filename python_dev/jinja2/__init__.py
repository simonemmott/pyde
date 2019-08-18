from jinja2 import Environment, FileSystemLoader, ChoiceLoader
import os
import os.path
import inspect
import logging
import python_dev.utils
from pathlib import Path

logger = logging.getLogger(__name__)

def _get_template_location():
    init_loc = os.path.abspath(inspect.getfile(inspect.currentframe()))
    jinja2_loc = Path(init_loc).parent
    return os.path.sep.join([str(jinja2_loc), 'templates'])

_templates = [_get_template_location()]

def add_templates(*additional_templates):
    _templates.extend(additional_templates)
    

def environment(**options):
    options['trim_blocks'] = options.get('trim_blocks', True)
    options['lstrip_blocks'] = options.get('lstrip_blocks', True)
    env = Environment(**options)
    env.globals.update({
        'secret': python_dev.utils.secret,
        'to_snake_case': python_dev.utils.to_snake_case,
        'to_kebab_case': python_dev.utils.to_kebab_case,
        'to_camel_case': python_dev.utils.to_camel_case,
        'to_class_case': python_dev.utils.to_class_case,
        'to_sentence_case': python_dev.utils.to_sentence_case,
        'to_title_case': python_dev.utils.to_title_case,
        'to_plural': python_dev.utils.to_plural,
        'is_number': python_dev.utils.is_number
    })
    return env

def _configured_environment():
    logger.info('Loading templates from {dir}'.format(dir=_templates))
    loaders = []
    for templates in _templates:
        loaders.append(FileSystemLoader(templates))
    return environment(loader=ChoiceLoader(loaders))

def get_template(*path):
    return env.get_template(os.path.sep.join(list(path)))
    

env = _configured_environment()