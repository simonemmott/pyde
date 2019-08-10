from unittest import TestCase
import os
import logging
import json
import python_dev


class PythonDevTests(TestCase):

    def setUp(self):
        self.cwd = os.getcwd()
        
    def tearDown(self):
        os.chdir(self.cwd)
        
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
        python_dev.write_about(
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


