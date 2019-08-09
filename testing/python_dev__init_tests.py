from unittest import TestCase
from unittest.mock import patch
from python_dev import init
import os.path
            

class InitTests(TestCase):
    
    def setUp(self):
        pass
        
    def tearDown(self):
        pass
    
    @patch('python_dev.init.open')
    @patch('os.mkdir')
    @patch('os.path.exists')
    @patch('python_dev.init.write_about')
    def test_init(self, mock_write_about, mock_exists, mock_mkdir, mock_open):
        mock_exists.return_value = False
        init.init('MODULE', 'VERSION', 'AUTHOR', 'EMAIL', 'DESCRIPTION', 'PACKAGE', 'URL')
        mock_mkdir.assert_called_once_with('MODULE')
        mock_open.assert_called_once_with(
            os.path.sep.join(['MODULE', '__init__.py']),
            'w')
        mock_open.return_value.close.assert_called_once()
        mock_write_about.assert_called_once_with(
            os.path.sep.join(['MODULE', 'about.py']),
            version='VERSION',
            author='AUTHOR',
            email='EMAIL',
            description='DESCRIPTION',
            package='PACKAGE',
            url='URL'
            )
        






















