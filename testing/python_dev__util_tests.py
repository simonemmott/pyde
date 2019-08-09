from unittest import TestCase
from unittest.mock import patch
import python_dev.utils as utils


class Dummy(object):
    def __init__(self, **kw):
        for key, value in kw.items():
            setattr(self, key, value)


class UtilTests(TestCase):
    
    def test_to_snake_case(self):
        self.assertIsNone(utils.to_snake_case(None))
        self.assertEqual('', utils.to_snake_case(''))
        self.assertEqual('hello_world', utils.to_snake_case('hello world!'))
        self.assertEqual('1234_hello_world', utils.to_snake_case('1234 hello world!'))
        self.assertEqual('hello_1234_world', utils.to_snake_case('hello 1234 world!'))
        self.assertEqual('hmm_how_about_this', utils.to_snake_case('  {Hmm how aBout @£$%^ this!@£$'))
        
    def test_to_kebab_case(self):
        self.assertIsNone(utils.to_kebab_case(None))
        self.assertEqual('', utils.to_kebab_case(''))
        self.assertEqual('hello-world', utils.to_kebab_case('hello world!'))
        self.assertEqual('hmm-how-about-this', utils.to_kebab_case('  {Hmm how aBout @£$%^ this!@£$'))

    def test_to_camel_case(self):
        self.assertIsNone(utils.to_camel_case(None))
        self.assertEqual('', utils.to_camel_case(''))
        self.assertEqual('helloWorld', utils.to_camel_case('hello world!'))
        self.assertEqual('model1', utils.to_camel_case('model1'))
        self.assertEqual('helloWorld', utils.to_camel_case('1234 hello world!'))
        self.assertEqual('hello1234World', utils.to_camel_case('hello 1234 world!'))
        self.assertEqual('hmmHowAboutThis', utils.to_camel_case('  {Hmm how aBout @£$%^ this!@£$'))

    def test_to_class_case(self):
        self.assertIsNone(utils.to_class_case(None))
        self.assertEqual('', utils.to_class_case(''))
        self.assertEqual('HelloWorld', utils.to_class_case('hello world!'))
        self.assertEqual('Model1', utils.to_class_case('model1'))
        self.assertEqual('HelloWorld', utils.to_class_case('1234 hello world!'))
        self.assertEqual('Hello1234World', utils.to_class_case('hello 1234 world!'))
        self.assertEqual('HmmHowAboutThis', utils.to_class_case('  {Hmm how aBout @£$%^ this!@£$'))

    def test_to_sentence_case(self):
        self.assertIsNone(utils.to_sentence_case(None))
        self.assertEqual('', utils.to_sentence_case(''))
        self.assertEqual('Hello world', utils.to_sentence_case('hello world!'))
        self.assertEqual('Hello World', utils.to_sentence_case('hello World!'))
        self.assertEqual('1234 hello world', utils.to_sentence_case('1234 hello world!'))
        self.assertEqual('Hello 1234 World', utils.to_sentence_case('hello 1234 World!'))
        self.assertEqual('Hmm how aBout this', utils.to_sentence_case('  {Hmm how aBout @£$%^ this!@£$'))

    def test_to_title_case(self):
        self.assertIsNone(utils.to_title_case(None))
        self.assertEqual('', utils.to_title_case(''))
        self.assertEqual('Hello World', utils.to_title_case('hello world!'))
        self.assertEqual('Hello World', utils.to_title_case('hello World!'))
        self.assertEqual('1234 Hello World', utils.to_title_case('1234 hello world!'))
        self.assertEqual('Hello 1234 World', utils.to_title_case('hello 1234 World!'))
        self.assertEqual('Hmm How About This', utils.to_title_case('  {Hmm how aBout @£$%^ this!@£$'))
        
    def test_to_plural(self):
        self.assertIsNone(utils.to_plural(None))
        self.assertEqual('', utils.to_plural(''))
        self.assertEqual('foos', utils.to_plural('foo'))
        self.assertEqual('cacti', utils.to_plural('cactus'))
        self.assertEqual('leaves', utils.to_plural('leaf'))
        self.assertEqual('1234', utils.to_plural('1234'))
        self.assertEqual('tries', utils.to_plural('try'))
        self.assertEqual('days', utils.to_plural('day'))





















