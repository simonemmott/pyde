from python_dev import jinja2
from python_dev import pyde
import os.path

def _get_include_dir(inclusion):
    for loc in jinja2._templates:
        include_dir = os.path.sep.join([loc, 'include'])
        if os.path.exists(include_dir):
            mod_dir = os.path.sep.join([include_dir, inclusion])
            if os.path.exists(mod_dir):
                return mod_dir
    raise ValueError("No inclusion found for: '{inclusion}'".format(inclusion=inclusion))

def _get_included_files(inclusion):
    include_dir = _get_include_dir(inclusion)
    return os.listdir(include_dir)

def include(inclusion):
    included = _get_included_files(inclusion)
    for name in included:
        template = jinja2.env.get_template(os.path.sep.join(['include', inclusion, name]))
        file_path = os.path.sep.join([pyde.install_dir, name])
        with open(file_path, 'w') as fp:
            print('Writing template {name} to {file}'.format(name=name, file=file_path))
            fp.write(template.render(meta=pyde.meta))

        









    
    
    
    
    