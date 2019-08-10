import os
import os.path
import re
import importlib.util
import logging
logger = logging.getLogger(__name__)
from python_dev import utils
from json_model import Finder


ignore_dirs = ['^testing$', '^htmlcov$', '^build$', '^dist$', '^__.*', '.*.egg-info$']

class About(object):
    def __init__(self, **kw):
        self.package=kw.get('package')
        self.version=kw.get('version')
        self.author=kw.get('author')
        self.author_email=kw.get('author_email')
        self.description=kw.get('description')
        self.url=kw.get('url')
        
class Module(object):
    def __init__(self, **kw):
        self.meta=kw.get('meta')
        self.name=kw.get('name')
        
    def testing_module_name(self):
        return '{name}_tests'.format(name=self.name)
    
    def testing_class_name(self):
        return '{name}Tests'.format(name=utils.to_class_case(self.name))

class Meta(Finder):
    def __init__(self, **kw):
        self.root_module = kw.get('root_module', None)
        self.modules = kw.get('modules', [])
        self.about = kw.get('about', About())
        self.includes = kw.get('includes', [])
        
    def module(self, name=None):
        if not name:
            name = self.root_module.name
        if name not in [module.name for module in self.modules]:
            raise ValueError('No module exists with name {name}'.format(name=name))
        return Module(meta=self, name=name)

def get_module_metadata(install_dir):
    meta = Meta()
    from python_dev import include
    for inclusion in include.inclusions.values():
        if inclusion.check and inclusion.check(install_dir):
            meta.includes.append(inclusion)
    for file in os.listdir(install_dir):
        for ignore in ignore_dirs:
            if re.compile(ignore).match(file):
                print('Ignoring {file} matches {ignore}'.format(file=file, ignore=ignore))
        file_path = os.path.sep.join([install_dir, file])
        if os.path.isdir(file_path):
            init_py = os.path.sep.join([file_path, '__init__.py'])
            if os.path.exists(init_py):
                meta.modules.append(Module(meta=meta, name=file))
            about_py = os.path.sep.join([file_path, 'about.py'])
            if os.path.exists(about_py):
                meta.root_module = meta.module(file)
                spec = importlib.util.spec_from_file_location('about', about_py)
                about = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(about)
                meta.about = about
#        elif os.path.isfile(file_path):
#            if file[-3:].lower() == '.py':
#                meta.modules.append(Module(meta=meta, name=file[:-3]))
    return meta

def write_about(about_py, version=None, author=None, email=None, description=None, package=None, url=None):
    if not os.path.exists(about_py):
        print('Creating {about}'.format(about=about_py))
        open(about_py, 'w').close()
    with open(about_py, 'r') as fp:
        about = fp.readlines()
    output = []
    included = []
    re_version = re.compile('^version\s*=')
    re_author = re.compile('^author\s*=')
    re_email = re.compile('^author_email\s*=')
    re_package = re.compile('^package\s*=')
    re_description = re.compile('^description\s*=')
    re_url = re.compile('^url\s*=')
    for line in about:
        if re_version.match(line) and version:
            output.append("version = '{ver}'".format(ver=version)+os.linesep)
            included.append('version')
        elif re_author.match(line) and author:
            output.append("author = '{author}'".format(author=author)+os.linesep)
            included.append('author')
        elif re_email.match(line) and email:
            output.append("author_email = '{email}'".format(email=email)+os.linesep)
            included.append('email')
        elif re_package.match(line) and package:
            output.append("package = '{package}'".format(package=package)+os.linesep)
            included.append('package')
        elif re_description.match(line) and description:
            output.append("description = '{description}'".format(description=description)+os.linesep)
            included.append('description')
        elif re_url.match(line) and url:
            output.append("url = '{url}'".format(url=url)+os.linesep)
            included.append('url')
        else:
            output.append(line)
    if version and 'version' not in included:
        output.append("version = '{ver}'".format(ver=version)+os.linesep)
    if author and 'author' not in included:
        output.append("author = '{author}'".format(author=author)+os.linesep)
    if email and 'email' not in included:
        output.append("author_email = '{email}'".format(email=email)+os.linesep)
    if description and 'description' not in included:
        output.append("description = '{description}'".format(description=description)+os.linesep)
    if package and 'package' not in included:
        output.append("package = '{package}'".format(package=package)+os.linesep)
    if url and 'url' not in included:
        output.append("url = '{url}'".format(url=url)+os.linesep)
    print('Updating {about}'.format(about=about_py))
    with open(about_py, 'w') as fp:
        for line in output:
            fp.write(line)

