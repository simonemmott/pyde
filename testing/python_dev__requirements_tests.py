from unittest import TestCase
from unittest.mock import patch
from python_dev import requirements
import os


class RequirementsTests(TestCase):
    
    def test_create_requirement(self):
        req = requirements.Requirement('package')
        self.assertEqual('package', req.package)
        self.assertEqual(None, req.operator)
        self.assertEqual(None, req.version)
    
        req = requirements.Requirement('package==version')
        self.assertEqual('package', req.package)
        self.assertEqual('==', req.operator)
        self.assertEqual('version', req.version)
    
        req = requirements.Requirement('package>=version')
        self.assertEqual('package', req.package)
        self.assertEqual('>=', req.operator)
        self.assertEqual('version', req.version)
    
        req = requirements.Requirement('package<=version')
        self.assertEqual('package', req.package)
        self.assertEqual('<=', req.operator)
        self.assertEqual('version', req.version)
    
        req = requirements.Requirement('package>version')
        self.assertEqual('package', req.package)
        self.assertEqual('>', req.operator)
        self.assertEqual('version', req.version)
    
        req = requirements.Requirement('package<version')
        self.assertEqual('package', req.package)
        self.assertEqual('<', req.operator)
        self.assertEqual('version', req.version)
    
        req = requirements.Requirement('package == version')
        self.assertEqual('package', req.package)
        self.assertEqual('==', req.operator)
        self.assertEqual('version', req.version)
    
        req = requirements.Requirement('package --hash=HASH')
        self.assertEqual('package', req.package)
        self.assertEqual(None, req.operator)
        self.assertEqual(None, req.version)
        self.assertEqual('HASH', req.hash)
    
        req = requirements.Requirement('package >= version, <= upper')
        self.assertEqual('package', req.package)
        self.assertEqual('>=', req.operator)
        self.assertEqual('version', req.version)
        self.assertEqual('<=', req.upper_operator)
        self.assertEqual('upper', req.upper_version)
    
    def test_requirement_line(self):
        req = requirements.Requirement('package >= version, <= upper --hash=HASH')
        self.assertEqual('package>=version,<=upper --hash=HASH', req.line())

    @patch('pip._internal.main')
    def test_requirement_install(self, mock_pip):
        req = requirements.Requirement('package >= version, <= upper --hash=HASH')
        req.install()
        mock_pip.assert_called_once_with(['install', 'package>=version,<=upper', '--hash=HASH'])

    def test_comment(self):
        com = requirements.Comment('# comment')
        self.assertEqual('# comment', com.comment)
        self.assertEqual('# comment', com.line())

    def test_option(self):
        opt = requirements.Option('--OPTION=VALUE')
        self.assertEqual('OPTION', opt.option)
        self.assertEqual('VALUE', opt.value)
        self.assertEqual('--OPTION=VALUE', opt.line())

    def test_requirements(self):
        reqs = requirements.Requirements()
        
        self.assertEqual([], reqs.lines)
        self.assertEqual([], reqs.options)
        self.assertEqual([], reqs.requirements)
        
        com = requirements.Comment('# comment')
        reqs.add(com)
        
        self.assertEqual(1, len(reqs.lines))
        self.assertEqual(com, reqs.lines[0])
        self.assertEqual(0, len(reqs.options))
        self.assertEqual(0, len(reqs.requirements))
        
        req = requirements.Requirement('package==version')
        reqs.add(req)
        
        self.assertEqual(2, len(reqs.lines))
        self.assertEqual(req, reqs.requirements[0])
        self.assertEqual(0, len(reqs.options))
        self.assertEqual(1, len(reqs.requirements))
        self.assertEqual(req, reqs.requirements[0])
        
        opt = requirements.Option('--OPTION=VALUE')
        reqs.add(opt)
        
        self.assertEqual(3, len(reqs.lines))
        self.assertEqual(opt, reqs.lines[2])
        self.assertEqual(1, len(reqs.options))
        self.assertEqual(1, len(reqs.requirements))
        self.assertEqual(opt, reqs.options[0])

    def test_requirements_include(self):
        reqs = requirements.Requirements()
        req = requirements.Requirement('package==version')
        reqs.add(req)
        self.assertTrue(reqs.includes('package'))
        self.assertFalse(reqs.includes('XXX'))
        
    def test_get_requirements(self):
        reqs = requirements.get_requirements('testing/test_environments/requirements/requirements.txt')
        self.assertEqual(5, len(reqs.lines))
        self.assertEqual(1, len(reqs.options))
        self.assertEqual(2, len(reqs.requirements))
        self.assertEqual('PACKAGE', reqs.requirements[0].package)
        self.assertEqual('==', reqs.requirements[0].operator)
        self.assertEqual('VERSION', reqs.requirements[0].version)
      












