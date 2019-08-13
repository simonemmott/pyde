from unittest import TestCase
from unittest.mock import patch
import python_dev
from python_dev import pyde
from python_dev import include
import os
import os.path
import shutil

def _clear_dir(dir):
    for file in os.listdir(dir):
        file_path = os.path.join(dir, file)
        if os.path.isfile(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
            
            
class Dummy(object):
    def __init__(self, **kw):
        for key, value in kw.items():
            setattr(self, key, value)
            
def assert_in_file(file, text, msg=None):
    with open(file, 'r') as fp:
        data = fp.read()
    assert text in data, '' if not msg else ': {msg}'.format(msg=msg)
                
            

class IncludeTests(TestCase):
    
    def setUp(self):
        pass
        
    def tearDown(self):
        pass
    
    def test_get_templates_dir_throws_value_error_if_no_inclusion_found(self):
        with self.assertRaisesRegex(ValueError, "No inclusion found for: 'XXXX'"):
            include._get_templates_dir('XXXX')
        
    def test_get_templates_dir_passes_if_inclusion_found(self):
        expected = os.path.sep.join([os.getcwd(), 'python_dev', 'jinja2', 'templates'])
        self.assertEqual(expected, include._get_templates_dir('logging'))
        
    def test_get_included_files(self):
        included = include._get_included_files(os.path.sep.join(['python_dev', 'jinja2', 'templates', 'include', 'logging']))
        self.assertEqual(2, len(included))
        self.assertTrue('logger.py' in included)
        self.assertTrue('logging.yaml' in included)
        
    def test_include_installs_files(self):
        pyde.install_dir = os.path.sep.join(['testing', 'test_environments', 'include_tests', 'install_files'])
        pyde.meta = Dummy(root_module='ROOT_MODULE', modules=['ROOT_MODULE', 'OTHER_MODULE'])
        _clear_dir(pyde.install_dir)
        include.include('logging')
        included = os.listdir(pyde.install_dir)
        self.assertEqual(3, len(included))
        self.assertTrue('logging.yaml' in included)
        self.assertTrue('logger.py' in included)
        assert_in_file(os.path.sep.join([pyde.install_dir, 'logging.yaml']),'  ROOT_MODULE:')
        assert_in_file(os.path.sep.join([pyde.install_dir, 'logging.yaml']),'  OTHER_MODULE:')






















