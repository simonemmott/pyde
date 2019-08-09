import click
from python_dev import about as about_pyde

@click.group()
def run():
    pass

@click.command(help='Show about message and exit')
@click.option('--version', is_flag=True, help='Show the version and exit')
def about(version):
    if version:
        print(about_pyde.version)
    else:
        print('#####################################')
        print()
        print(about_pyde.description)
        print()
        print('Version: {ver}'.format(ver=about_pyde.version))
        print()
        print('Author:  {author}'.format(author=about_pyde.author))
        print()
        print('Email:   {email}'.format(email=about_pyde.author_email))
        print()
        print('Package: {package}'.format(package=about_pyde.package))
        print()
        print('URL:     {url}'.format(url=about_pyde.url))
        print()
        print('#####################################')
run.add_command(about)