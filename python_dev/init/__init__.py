import os.path
import os
from python_dev import write_about


def init(module, version, author, email, description, package, url):
    if not os.path.exists(module):
        print('Creating the root module. {root}'.format(root=module))
        os.mkdir(module)
    else:
        print('The root module directory {root} already exists'.format(root=module))
    init_py = os.path.sep.join([module, '__init__.py'])
    if not os.path.exists(init_py):
        print('Creating __init__.py in root module. {root}'.format(root=module))
        open(init_py, 'w').close()
    else:
        print('The __init__.py in root module {root} already exists'.format(root=module))
    about_py = os.path.sep.join([module, 'about.py'])
    write_about(
        about_py, 
        version=version,
        author=author,
        email=email,
        description=description,
        package=package,
        url=url)
