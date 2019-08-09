from python_dev import jinja2
from python_dev import pyde
import yaml
import os.path

def _get_templates_dir(inclusion):
    for loc in jinja2._templates:
        include_dir = os.path.sep.join([loc, 'include'])
        if os.path.exists(include_dir):
            mod_dir = os.path.sep.join([include_dir, inclusion])
            if os.path.exists(mod_dir):
                return loc
    raise ValueError("No inclusion found for: '{inclusion}'".format(inclusion=inclusion))

def _get_included_files(dir):
    return [name for name in os.listdir(dir) if name != 'control.yaml']

def _get_include_control(dir):
    control_file = os.path.sep.join([dir, 'control.yaml'])
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
        if name in control:
            pass
        else:
            template_loc = os.path.sep.join([template_loc, name])
            file_path = os.path.sep.join([templates_dir, template_loc])
            as_file = os.path.sep.join([as_dir, name])
            if os.path.isfile(file_path):
                _include_file(template_loc, as_file)
            elif os.path.isdir(file_path):
                _include_dir(templates_dir, template_loc, as_file)
        

def _include_file(template_loc, as_file, data=None):
    template = jinja2.env.get_template(template_loc)
    if os.path.exists(as_file):
        print('The included file {file} already exist. Skipping'.format(file=as_file))
    else:
        with open(as_file, 'w') as fp:
            print('Writing template {name} to {file}'.format(name=template_loc, file=as_file))
            fp.write(template.render(meta=pyde.meta, data=data))
            

def include(inclusion):
    templates_dir = _get_templates_dir(inclusion)
    inclusion_loc = os.path.sep.join([templates_dir, 'include', inclusion])
    included = _get_included_files(inclusion_loc)
    control = _get_include_control(inclusion_loc)
    for name in included:
        if name in control:
            pass
        else:
            template_loc = os.path.sep.join(['include', inclusion, name])
            file_path = os.path.sep.join([templates_dir, template_loc])
            as_file = os.path.sep.join([pyde.install_dir, name])
            if os.path.isfile(file_path):
                _include_file(template_loc, as_file)
            elif os.path.isdir(file_path):
                _include_dir(templates_dir, template_loc, as_file)

        









    
    
    
    
    