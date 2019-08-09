import os
import os.path
import re
import importlib.util
import logging
logger = logging.getLogger(__name__)

def get_module_metadata(install_dir):
    class Meta(object):
        pass
    meta = Meta()
    meta.modules = []
    for file in os.listdir(install_dir):
        file_path = os.path.sep.join([install_dir, file])
        if os.path.isdir(file_path):
            init_py = os.path.sep.join([file_path, '__init__.py'])
            if os.path.exists(init_py):
                meta.modules.append(file)
            about_py = os.path.sep.join([file_path, 'about.py'])
            if os.path.exists(about_py):
                meta.root_module = file
                spec = importlib.util.spec_from_file_location('about', about_py)
                about = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(about)
                meta.about = about
    return meta

def write_about(about_py, version=None, author=None, email=None, description=None, package=None, url=None):
    if not os.path.exists(about_py):
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
    with open(about_py, 'w') as fp:
        for line in output:
            fp.write(line)

