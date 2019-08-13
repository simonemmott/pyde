import click
import os
import os.path
from python_dev import about as about_pyde
from python_dev import get_module_metadata, write_about
import python_dev.include
import python_dev.init
import logging
import re
import importlib.util

logger = logging.getLogger(__name__)

install_dir = os.getcwd()

meta = None
            

@click.group()
@click.option('--target', help='Set the target directory')
def run(target):
    if target:
        global install_dir
        install_dir = target
    global meta
    meta = get_module_metadata(install_dir)

@run.command(help='Show about message and exit')
@click.option('--version', is_flag=True, help='Show the version and exit')
def about(version):
    if version:
        click.echo(about_pyde.version)
    else:
        click.echo('#####################################')
        click.echo()
        click.echo(about_pyde.description)
        click.echo()
        click.echo('Version: {ver}'.format(ver=about_pyde.version))
        click.echo()
        click.echo('Author:  {author}'.format(author=about_pyde.author))
        click.echo()
        click.echo('Email:   {email}'.format(email=about_pyde.author_email))
        click.echo()
        click.echo('Package: {package}'.format(package=about_pyde.package))
        click.echo()
        click.echo('URL:     {url}'.format(url=about_pyde.url))
        click.echo()
        click.echo('#####################################')
        

@run.command(help='Initialise a new development environment')
@click.argument('module')
@click.option('--version', prompt=True, type=str, help="Set the version of the module")
@click.option('--author', prompt=True, type=str, help="Set the author of the module")
@click.option('--email', prompt=True, type=str, help="Set the support email of the module")
@click.option('--description', prompt=True, type=str, help="Set the short description the module")
@click.option('--package', prompt=True, type=str, help="Set the package name which supplies the module")
@click.option('--url', prompt=True, type=str, help="Set the URL which documents the module")
def init(module, version, author, email, description, package, url):
    python_dev.init.init(module, version, author, email, description, package, url)

@run.command(help='Include additional functionality in the development environment')    
@click.argument('inclusion')
def include(inclusion):
    python_dev.include.include(inclusion)

@run.group(help='Add additional items to the package being developed')    
def add():
    python_dev.add.add()
    
    
from python_dev import add as imported_add




























