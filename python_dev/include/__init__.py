from python_dev import jinja2
from python_dev import pyde
import yaml
import os.path
import importlib

control_name = 'control.yaml'

class Inclusion(object):
    def __init__(self, **kw):
        if kw.get('dir'):
            dir = kw.get('dir')
            self.name = os.path.basename(dir)
            include = os.path.dirname(dir)
            self.location = os.path.abspath(os.path.dirname(include))
            self.template = os.path.sep.join(['include', self.name])
            control_file = os.path.sep.join([dir, control_name])
            self.control = None
            if os.path.exists(control_file):
                with open(control_file, 'rt') as f:
                    self.control = yaml.safe_load(f.read())
        else:
            self.name=kw.get('name')
            self.template=kw.get('template')
            self.location=kw.get('location')
            self.control=kw.get('control')
        self.check = None
        if self.control:
            self.check = self.control.get('check')
        self.check = kw.get('check', self.check)
        if isinstance(self.check, str):
            check_mod = importlib.import_module('.'.join(self.check.split('.')[:-1]))
            func = self.check.split('.')[-1]
            if hasattr(check_mod, func):
                self.check = getattr(check_mod, func)
                
                
        
def check_includes(install_dir):
    return 'testing' in os.listdir(install_dir)
        

def _get_inclusions():
    inclusions = {}
    for loc in jinja2._templates:
        include_dir = os.path.sep.join([loc, 'include'])
        if os.path.exists(include_dir):
            for inclusion in os.listdir(include_dir):
                inclusion_dir = os.path.sep.join([include_dir, inclusion])
                if os.path.isdir(inclusion_dir):
                    inclusion = Inclusion(dir=inclusion_dir)
                    if inclusion.name not in inclusions:
                        inclusions[inclusion.name] = inclusion
    return inclusions

inclusions = _get_inclusions()
    

def _get_templates_dir(inclusion):
    for loc in jinja2._templates:
        include_dir = os.path.sep.join([loc, 'include'])
        if os.path.exists(include_dir):
            mod_dir = os.path.sep.join([include_dir, inclusion])
            if os.path.exists(mod_dir):
                return loc
    raise ValueError("No inclusion found for: '{inclusion}'".format(inclusion=inclusion))

def _get_included_files(dir):
    return [name for name in os.listdir(dir) if name != control_name]

def _get_include_control(dir):
    control_file = os.path.sep.join([dir, control_name])
    if os.path.exists(control_file):
        with open(control_file, 'rt') as f:
            return yaml.safe_load(f.read())
    return {}

def _include_dir(templates_dir, template_loc, as_dir):
    inclusion_loc = os.path.sep.join([templates_dir, template_loc])
    control = _get_include_control(inclusion_loc)
    if os.path.exists(as_dir) and os.path.isfile(as_dir):
        print('{dir} exists and is a file. Skipping'.format(dir=as_dir))
        return
    elif os.path.exists(as_dir) and os.path.isdir(as_dir):
        print('The directory {dir} already exists.'.format(dir=as_dir))
    else:
        os.mkdir(as_dir)
    for name in _get_included_files(inclusion_loc):
        template_name = os.path.sep.join([template_loc, name])
        file_path = os.path.sep.join([templates_dir, template_name])
        if name in control:
            name_template = control[name]['name']
            data_path = control[name]['path']
            data = pyde.meta.__find__(data_path)
            for item in data:
                item_name = jinja2.env.from_string(name_template).render(meta=pyde.meta, item=item)
                as_file = os.path.sep.join([as_dir, item_name])
                if os.path.isfile(file_path):
                    _include_file(template_name, as_file)
                elif os.path.isdir(file_path):
                    _include_dir(templates_dir, template_name, as_file)
        else:
            as_file = os.path.sep.join([as_dir, name])
            if os.path.isfile(file_path):
                _include_file(template_name, as_file)
            elif os.path.isdir(file_path):
                _include_dir(templates_dir, template_name, as_file)
        

def _include_file(template_loc, as_file, item=None):
    template = jinja2.env.get_template(template_loc)
    if os.path.exists(as_file):
        print('The included file {file} already exist. Skipping'.format(file=as_file))
    else:
        with open(as_file, 'w') as fp:
            print('Writing template {name} to {file}'.format(name=template_loc, file=as_file))
            fp.write(template.render(meta=pyde.meta, item=item))
            

def include(inclusion):
    templates_dir = _get_templates_dir(inclusion)
    inclusion_loc = os.path.sep.join([templates_dir, 'include', inclusion])
    included = _get_included_files(inclusion_loc)
    control = _get_include_control(inclusion_loc)
    for name in included:
        template_name = os.path.sep.join(['include', inclusion, name])
        file_path = os.path.sep.join([templates_dir, template_name])
        if name in control:
            name_template = control[name]['name']
            data_path = control[name]['path']
            data = pyde.meta.__find__(data_path)
            for item in data:
                item_name = jinja2.env.from_string(name_template).render(meta=pyde.meta, item=item)
                as_file = os.path.sep.join([as_dir, item_name])
                if os.path.isfile(file_path):
                    _include_file(template_name, as_file)
                elif os.path.isdir(file_path):
                    _include_dir(templates_, template_name, as_file)
            
        else:
            as_file = os.path.sep.join([pyde.install_dir, name])
            if os.path.isfile(file_path):
                _include_file(template_name, as_file)
            elif os.path.isdir(file_path):
                _include_dir(templates_dir, template_name, as_file)

        









    
    
    
    
    