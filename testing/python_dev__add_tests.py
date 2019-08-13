from unittest import TestCase
from unittest.mock import patch
import python_dev
from python_dev import pyde
from python_dev import add
from python_dev.utils import build_path, path_exists
import os
import os.path
import shutil

def assert_in_file(file, text, msg=None):
    with open(file, 'r') as fp:
        data = fp.read()
    assert text in data, '' if not msg else ': {msg}'.format(msg=msg)

class AddTests(TestCase):
    
    def setUp(self):
        pass
        
    def tearDown(self):
        pass
    
    def test_add_model_creates_model_package_if_it_doesnt_exist(self):
        pyde.install_dir = build_path('testing', 'test_environments', 'add_tests', 'add_model_test')
        pyde.meta = python_dev.get_module_metadata(pyde.install_dir)
        if path_exists(pyde.install_dir, 'add_model', 'model'):
            shutil.rmtree(build_path(pyde.install_dir, 'add_model', 'model'))
        add.model._model('MODEL')
        self.assertTrue(
            path_exists(pyde.install_dir, 'add_model', 'model'),
            'model package is not created')
        self.assertTrue(
            path_exists(pyde.install_dir, 'add_model', 'model', '__init__.py'),
            '__init__.py not created in model package')

        
    def test_add_model_creates_package_for_model(self):
        pyde.install_dir = build_path('testing', 'test_environments', 'add_tests', 'add_model_test')
        pyde.meta = python_dev.get_module_metadata(pyde.install_dir)
        if path_exists(pyde.install_dir, 'add_model', 'model'):
            shutil.rmtree(build_path(pyde.install_dir, 'add_model', 'model'))
        add.model._model('MODEL')
        self.assertTrue(
            path_exists(pyde.install_dir, 'add_model', 'model', 'model.py'),
            'package for model not created')
        
    def test_add_model_adds_model_to_model_barrel(self):
        pyde.install_dir = build_path('testing', 'test_environments', 'add_tests', 'add_model_test')
        pyde.meta = python_dev.get_module_metadata(pyde.install_dir)
        if path_exists(pyde.install_dir, 'add_model', 'model'):
            shutil.rmtree(build_path(pyde.install_dir, 'add_model', 'model'))
        add.model._model('MODEL')
        assert_in_file(
            build_path(pyde.install_dir, 'add_model', 'model', '__init__.py'),
            'from .model import Model',
            'Model not added to model barrel')
        
        




















