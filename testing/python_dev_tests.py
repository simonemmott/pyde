from unittest import TestCase
import os
import logging
import json
import python_dev
from python_dev import utils, configuration, Meta
import json_model


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

    def test_load_location_returns_empty_dict_if_location_not_found(self):
        data = python_dev.load_location('XXXX')
        self.assertEqual({}, data, 'Empty dict not returned by load_location')

    def test_load_location_returns_dict_from_json_file(self):
        data = python_dev.load_location(utils.build_path('testing', 'test_environments', 'load_location', 'test_load.json'))
        expected = {
            'name': 'NAME',
            'description': 'DESCRIPTION'
        }
        self.assertEqual(expected, data, 'Loaded dict not returned by load_location')

    def test_load_location_returns_dict_from_yaml_file(self):
        data = python_dev.load_location(utils.build_path('testing', 'test_environments', 'load_location', 'test_load.yaml'))
        expected = {
            'name': 'NAME',
            'description': 'DESCRIPTION'
        }
        self.assertEqual(expected, data, 'Loaded dict not returned by load_location')

    def test_load_location_returns_dict_from_ini_file(self):
        data = python_dev.load_location(utils.build_path('testing', 'test_environments', 'load_location', 'test_load.ini'))
        expected = {
            'DEFAULT': {
            },
            'group 1': {
                'name': 'NAME',
                'description': 'DESCRIPTION'
            },
            'group 2': {
                'foo': 'bar'
            }
        }
        self.assertEqual(expected, data, 'Loaded config not returned by load_location')

    def test_load_location_returns_dict_from_url(self):
        data = python_dev.load_location('http://echo.jsontest.com/key/value/one/two')
        expected = {
            'one': 'two',
            'key': 'value'
        }
        self.assertEqual(expected, data, 'Loaded url not returned by load_location')

    def test_load_open_api(self):
        api = python_dev.load_open_api(utils.build_path('testing', 'test_environments', 'load_api', 'petstore.yaml'))
#        print(json.dumps(api.to_dict(), indent=4))
        api = python_dev.load_open_api(utils.build_path('testing', 'test_environments', 'load_api', 'petstore.yaml'))
#        print(json.dumps(api.to_dict(unpack=False), indent=4))

    def test_config_to_obj(self):
        cfg = configuration.read_config(utils.build_path('testing', 'test_environments', 'configuration', 'test_1.ini'))
        cfg_obj = configuration.config_to_obj(cfg)
        self.assertEqual('VALUE', cfg_obj.pyde.name)
        self.assertEqual('META_VALUE', cfg_obj.Meta.meta_name)

    def test_add_config_meta(self):
        meta = Meta()
        cfg = configuration.read_config(utils.build_path('testing', 'test_environments', 'configuration', 'with_meta_data.ini'))
        python_dev._add_config_meta(meta, cfg)
        self.assertTrue(hasattr(meta, 'custom'))
        self.assertEqual('NAME', meta.custom.name)
        self.assertEqual('DESCRIPTION', meta.custom.description)
        self.assertTrue(hasattr(meta, 'custom2'))
        self.assertEqual('NAME_2', meta.custom2.name2)
        self.assertEqual('DESCRIPTION_2', meta.custom2.description2)
































       
