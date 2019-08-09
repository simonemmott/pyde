from unittest import TestCase
from unittest.mock import patch
import python_dev
from python_dev import jinja2
import os
import os.path


class Dummy(object):
    def __init__(self, **kw):
        for key, value in kw.items():
            setattr(self, key, value)


class Jinja2Tests(TestCase):
    
    def setUp(self):
        pass
        
    def tearDown(self):
        pass
    
    def test_get_template_location(self):
        self.assertEqual(
            os.path.sep.join([os.getcwd(), 'python_dev', 'jinja2', 'templates']), 
            jinja2._get_template_location(), 
            "Incorrect base template location")
        
    def test_test_template(self):
        template = jinja2.env.get_template('test_template.txt')
        self.assertEqual('Hello WORLD!', template.render(data=Dummy(name='WORLD')))





















