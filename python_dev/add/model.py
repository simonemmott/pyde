from python_dev import pyde
from python_dev import utils
from python_dev import jinja2
from json_api.model import Schema
import os
import os.path
import click


@pyde.add.command(help='Add a model to the development package')
@click.argument('model')
def model(model):
    _model(model)
    
def _create_module_dir(module_dir, *template_path):
    if not template_path:
        template_path = ['common', 'init.py']
    if not os.path.exists(module_dir):
        print('Creating directory {dir}'.format(dir=module_dir))
        os.mkdir(module_dir)
    module_dir_init = os.path.sep.join([module_dir, '__init__.py'])
    if not os.path.exists(module_dir_init):
        template = jinja2.get_template(*template_path)
        with open(module_dir_init, 'w') as fp:
            print('Adding __init__.py to {dir}'.format(dir=module_dir))
            fp.write(template.render(meta=pyde.meta))
            
def _create_model_module(model_dir, schema):
    model_module = schema.module_name()+'.py'
    model_module_file = os.path.sep.join([model_dir, model_module])
    if os.path.exists(model_module_file):
        raise FileExistsError('The model module {m} already exists'.format(m=model_module_file))
    template = jinja2.get_template('add', 'model', 'model.py')
    with open(model_module_file, 'w') as fp:
        print('Adding model {name} in {file}'.format(name=model, file=model_module_file))
        fp.write(template.render(schema=schema, meta=pyde.meta))
        
def _add_model_to_barrel(model_dir, schema):
    model_init = utils.build_path(model_dir, '__init__.py')
    with open(model_init, 'a') as fp:
        fp.write('from .{module} import {cls}'.format(
            module=schema.module_name(), 
            cls=schema.class_name())+os.linesep)
    

def _model(model):
    schema = Schema(title=model)
    install_dir = pyde.install_dir
    target_module = pyde.meta.root_module
    module_dir = os.path.sep.join([pyde.install_dir, target_module.module_dir()])
    model_dir = os.path.sep.join([module_dir, 'model'])
    _create_module_dir(model_dir, 'add', 'model', 'init.py')
    _create_model_module(model_dir, schema)
    _add_model_to_barrel(model_dir, schema)
    






