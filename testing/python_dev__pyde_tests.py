from unittest import TestCase
import os
import os.path
from python_dev import pyde
from python_dev.pyde import run
from python_dev import about as about_pyde
from click.testing import CliRunner
import shutil

class PydeTests(TestCase):
    
    def setUp(self):
        self.cwd = os.getcwd()
        
    def tearDown(self):
        os.chdir(self.cwd)
        
    def test_about(self):
        runner = CliRunner()
        result = runner.invoke(run, ['about'])
        self.assertEqual(0, result.exit_code)
        self.assertTrue('Version: {ver}'.format(ver=about_pyde.version) in result.output)
        self.assertTrue('Author:  {author}'.format(author=about_pyde.author) in result.output)
        self.assertTrue('Email:   {email}'.format(email=about_pyde.author_email) in result.output)
        self.assertTrue('Package: {package}'.format(package=about_pyde.package) in result.output)
        self.assertTrue('URL:     {url}'.format(url=about_pyde.url) in result.output)

    def test_about_version(self):
        runner = CliRunner()
        result = runner.invoke(run, ['about', '--version'])
        self.assertEqual(0, result.exit_code)
        self.assertEqual(about_pyde.version+os.linesep, result.output)

    def test_init_creates_module(self):
        runner = CliRunner()
        os.chdir('testing/test_environments/new_module_test')
        if os.path.exists('new_module'):
            shutil.rmtree('new_module')
        try:
            result = runner.invoke(run, ['init', 'new_module'], input='VERSION{sep}AUTHOR{sep}EMAIL{sep}DESCRIPTION{sep}PACKAGE{sep}URL{sep}'.format(sep=os.linesep))
            self.assertTrue(os.path.exists('new_module'), 'Module directory not created')
            self.assertTrue(os.path.exists(os.path.sep.join(['new_module', '__init__.py'])), '__init__.py not created in module directory')
            self.assertTrue(os.path.exists(os.path.sep.join(['new_module', 'about.py'])), 'about.py not created in module directory')
            with open(os.path.sep.join(['new_module', 'about.py']), 'r') as fp:
                about = fp.readlines()
            self.assertTrue("version = 'VERSION'"+os.linesep in about, 'Version not written to about correctly')
            self.assertTrue("author = 'AUTHOR'"+os.linesep in about, 'Author not written to about correctly')
            self.assertTrue("author_email = 'EMAIL'"+os.linesep in about, 'Author email not written to about correctly')
            self.assertTrue("description = 'DESCRIPTION'"+os.linesep in about, 'Description not written to about correctly')
            self.assertTrue("package = 'PACKAGE'"+os.linesep in about, 'Package not written to about correctly')
            self.assertTrue("url = 'URL'"+os.linesep in about, 'URL not written to about correctly')
        finally:
            if os.path.exists('new_module'):
                shutil.rmtree('new_module')
                
    def test_update_about(self):
        os.chdir('testing/test_environments/update_module_test')
        with open(os.path.sep.join(['update_module', 'about.py']), 'w') as fp:
            fp.write("# This is a comment"+os.linesep)
            fp.write(""+os.linesep)
            fp.write("version = 'version'"+os.linesep)
            fp.write("author = 'author'"+os.linesep)
            fp.write("author_email = 'author_email'"+os.linesep)
            fp.write("description = 'description'"+os.linesep)
            fp.write("package = 'package'"+os.linesep)
            fp.write("url = 'url'"+os.linesep)
            fp.write("somthing_new = 'NEW'"+os.linesep)
        pyde._write_about(
            os.path.sep.join(['update_module', 'about.py']),
            version='VERSION',
            author='AUTHOR',
            description='DESCRIPTION',
            package="PACKAGE",
            url='URL')
        with open(os.path.sep.join(['update_module', 'about.py']), 'r') as fp:
            about = fp.readlines()
        self.assertTrue("# This is a comment"+os.linesep in about, 'Comment removed from about')
        self.assertTrue(""+os.linesep in about, 'Blank line removed from about')
        self.assertTrue("somthing_new = 'NEW'"+os.linesep in about, 'Existing code removed from about')
        self.assertTrue("version = 'VERSION'"+os.linesep in about, 'Version not written to about correctly')
        self.assertTrue("author = 'AUTHOR'"+os.linesep in about, 'Author not written to about correctly')
        self.assertTrue("author_email = 'author_email'"+os.linesep in about, 'Author email not written to about correctly')
        self.assertTrue("description = 'DESCRIPTION'"+os.linesep in about, 'Description not written to about correctly')
        self.assertTrue("package = 'PACKAGE'"+os.linesep in about, 'Package not written to about correctly')
        self.assertTrue("url = 'URL'"+os.linesep in about, 'URL not written to about correctly')

        
    def test_init_updates_module(self):
        runner = CliRunner()
        os.chdir('testing/test_environments/update_module_test')
        with open(os.path.sep.join(['update_module', '__init__.py']), 'w') as fp:
            fp.write('# This is a comment')
        with open(os.path.sep.join(['update_module', 'about.py']), 'w') as fp:
            fp.write("# This is a comment"+os.linesep)
            fp.write(""+os.linesep)
            fp.write("version = 'version'"+os.linesep)
            fp.write("author = 'author'"+os.linesep)
            fp.write("author_email = 'author_email'"+os.linesep)
            fp.write("description = 'description'"+os.linesep)
            fp.write("package = 'package'"+os.linesep)
            fp.write("url = 'url'"+os.linesep)
            fp.write("somthing_new = 'NEW'"+os.linesep)
        result = runner.invoke(run, ['init', 'update_module'], input='VERSION{sep}AUTHOR{sep}EMAIL{sep}DESCRIPTION{sep}PACKAGE{sep}URL{sep}'.format(sep=os.linesep))
        self.assertTrue(os.path.exists('update_module'), 'Module directory not created')
        self.assertTrue(os.path.exists(os.path.sep.join(['update_module', '__init__.py'])), '__init__.py removed from module directory')
        self.assertTrue(os.path.exists(os.path.sep.join(['update_module', 'about.py'])), 'about.py removed from module directory')
        with open(os.path.sep.join(['update_module', 'about.py']), 'r') as fp:
            about = fp.readlines()
        self.assertTrue("# This is a comment"+os.linesep in about, 'Comment removed from about')
        self.assertTrue(""+os.linesep in about, 'Blank line removed from about')
        self.assertTrue("somthing_new = 'NEW'"+os.linesep in about, 'Existing code removed from about')
        self.assertTrue("version = 'VERSION'"+os.linesep in about, 'Version not written to about correctly')
        self.assertTrue("author = 'AUTHOR'"+os.linesep in about, 'Author not written to about correctly')
        self.assertTrue("author_email = 'EMAIL'"+os.linesep in about, 'Author email not written to about correctly')
        self.assertTrue("description = 'DESCRIPTION'"+os.linesep in about, 'Description not written to about correctly')
        self.assertTrue("package = 'PACKAGE'"+os.linesep in about, 'Package not written to about correctly')
        self.assertTrue("url = 'URL'"+os.linesep in about, 'URL not written to about correctly')
        
        

