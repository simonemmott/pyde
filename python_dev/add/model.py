from python_dev import pyde
from python_dev import utils
from python_dev import jinja2
from json_api.model import Schema
import json_model
import os
import os.path
import click


@pyde.add.command(help='Add a model to the development package')
@click.argument('model')
@click.option('--replace/--no-replace', default=False)
@click.option('--echo/--no-echo', default=False)
@click.option('--cascade/--no-cascade', default=False)
@click.option('--show-schema/--no-show-schema', default=False)
def model(model, replace, echo, cascade, show_schema):
    _model(model, replace, echo, cascade, show_schema)
    
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
            fp.write(template.render(meta=pyde.meta)+os.linesep)
            
def _echo_file(file):
    print('#### - BEGIN: {file} - ####'.format(file=file))
    with open(file, 'r') as fp:
        print(fp.read())
    print('#### - END - ####')
            
def _create_model_module(model_dir, schema, replace, echo, cascade, show_schema, created=[]):
    if schema in created:
        return
    model_module = schema.module_name()+'.py'
    model_module_file = os.path.sep.join([model_dir, model_module])
    if os.path.exists(model_module_file):
        if replace:
            print('The model module {m} already exists and will be replaced'.format(m=model_module_file))
        else:
            print('The model module {m} already exists'.format(m=model_module_file))
            return
    template = jinja2.get_template('add', 'model', 'model.py')
    with open(model_module_file, 'w') as fp:
        print('Adding model at {file}'.format(file=model_module_file))
        fp.write(template.render(schema=schema, meta=pyde.meta))
    created.append(schema)
    if show_schema:
        schema.__show__(unpack=False)        
    if echo:
        _echo_file(model_module_file)
        
    if cascade:
        for ref_schema in schema.get_referenced_schemas():
            _model(ref_schema, replace, echo, cascade, show_schema, created)
            
    
        
        
def _add_model_to_barrel(model_dir, schema):
    model_init = utils.build_path(model_dir, '__init__.py')
    with open(model_init, 'r') as fp:
        init = fp.readlines()
    found = False
    model_import = 'from .{module} import {cls}'.format(
                module=schema.module_name(), 
                cls=schema.class_name())
    with open(model_init, 'w') as fp:
        for line in init:
            if line.startswith('register_models(') and not found:
                fp.write(model_import+os.linesep)
                fp.write(line)
                found = True
                continue
            if line.strip() == model_import:
                fp.write(line)
                found = True
                continue
            fp.write(line)
        if not found:
            fp.write(model_import+os.linesep)
    

def _model(model, replace=False, echo=False, cascade=False, show_schema=False, created=None):
    if not created:
        created = []
    with json_model.references():
        if isinstance(model, Schema):
            schema = model
        else:
            schema = None
        if pyde.meta.api and not schema:
            if model in pyde.meta.api.components.schemas:
                schema = pyde.meta.api.components.schemas[model]
        if not schema:
            schema = Schema()
            schema.__index__ = model
        install_dir = pyde.install_dir
        target_module = pyde.meta.root_module
        module_dir = os.path.sep.join([pyde.install_dir, target_module.module_dir()])
        model_dir = os.path.sep.join([module_dir, 'model'])
        _create_module_dir(model_dir, 'add', 'model', 'init.py')
        _create_model_module(model_dir, schema, replace, echo, cascade, show_schema, created)
        _add_model_to_barrel(model_dir, schema)

    






