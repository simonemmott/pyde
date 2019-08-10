from unittest import TestCase
from unittest.mock import patch
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

    @patch('python_dev.init.init')  
    def test_pyde_includes_init_command(self, mock_init):
        runner = CliRunner()
        result = runner.invoke(
            run, 
            ['init', 'MODULE'], 
            input='VERSION{sep}AUTHOR{sep}EMAIL{sep}DESCRIPTION{sep}PACKAGE{sep}URL{sep}'.format(sep=os.linesep))
        self.assertEqual(0, result.exit_code)
        mock_init.assert_called_once_with(
            'MODULE', 
            'VERSION', 
            'AUTHOR', 
            'EMAIL', 
            'DESCRIPTION', 
            'PACKAGE', 
            'URL')
                            
    @patch('python_dev.include.include')  
    def test_pyde_includes_include_command(self, mock_include):
        runner = CliRunner()
        result = runner.invoke(run, ['include', 'INCLUDE'])
        self.assertEqual(0, result.exit_code, 'Include command failed')
        mock_include.assert_called_once_with('INCLUDE')
        
    def test_get_module_metadata(self):
        meta = pyde.get_module_metadata(os.path.sep.join(['testing', 'test_environments', 'get_module_metadata']))
        self.assertEqual('main', meta.root_module.name)
        self.assertEqual('main', meta.name)
        self.assertEqual('VERSION', meta.about.version)
        self.assertEqual('AUTHOR', meta.about.author)
        self.assertEqual('AUTHOR_EMAIL', meta.about.author_email)
        self.assertEqual('DESCRIPTION', meta.about.description)
        self.assertEqual('PACKAGE', meta.about.package)
        self.assertEqual('URL', meta.about.url)
        self.assertEqual('NEW', meta.about.somthing_new)
        self.assertEqual(2, len(meta.modules))
        self.assertTrue('main' in [module.name for module in meta.modules])
        self.assertTrue('other_module' in [module.name for module in meta.modules])
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

