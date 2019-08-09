import os.path
import os
from python_dev import write_about


def init(module, version, author, email, description, package, url):
    if not os.path.exists(module):
        os.mkdir(module)
    init_py = os.path.sep.join([module, '__init__.py'])
    if not os.path.exists(init_py):
        open(init_py, 'w').close()
    about_py = os.path.sep.join([module, 'about.py'])
    write_about(
        about_py, 
        version=version,
        author=author,
        email=email,
        description=description,
        package=package,
        url=url)
