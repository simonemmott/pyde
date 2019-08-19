from unittest import TestCase

from python_dev.json_api.model.schema import Schema, Property


class SchemaTests(TestCase):

    def test_property(self):
        s = Schema(type='TYPE')
        p = Property(s)
        self.assertTrue(p.is_property())
        
    def test_get_data_type(self):
        s_int = Schema(type='integer')
        s_float = Schema(type='number')
        s_bool = Schema(type='boolean')
        s_str = Schema(type='string')
        s_obj = Schema(type='object')
        s_list = Schema(type='array', items=s_obj)
        
        self.assertEqual(int, s_int.get_data_type())
        self.assertEqual(float, s_float.get_data_type())
        self.assertEqual(bool, s_bool.get_data_type())
        self.assertEqual(str, s_str.get_data_type())
        self.assertEqual(s_obj, s_obj.get_data_type())
        self.assertEqual(s_obj, s_list.get_data_type())

    def test_class_name(self):
        s = Schema(type='integer')
        s.__index__ = 'index'
        self.assertEqual('Index', s.class_name())

    def test_module_name(self):
        s = Schema(type='integer')
        s.__index__ = 'index'
        self.assertEqual('index', s.module_name())
        
    def test_get_all_properties(self):
        s1_data = {
            'type': 'object',
            'properties': {
                'name': {
                    'type': 'string'
                },
                'username': {
                    'type': 'string'
                },
                'password': {
                    'type': 'string'
                },
                'email': {
                    'type': 'string'
                }
            }
        }
        s2_data = {
            'allOf': [
                s1_data,
                {
                    'type': 'object',
                    'properties': {
                        'uuid': {
                            'type': 'string'
                        },
                        'state': {
                            'type': 'string'
                        },
                        'environment': {
                            'type': 'string'
                        },
                        'release': {
                            'type': 'string'
                        }
                    }
                },
                {
                    'allOf': [
                        {
                            'type': 'object',
                            'properties': {
                                'attr1': {
                                    'type': 'string'
                                },
                                'attr2': {
                                    'type': 'string'
                                }
                            }
                        },
                        {
                            'type': 'object',
                            'properties': {
                                'attr2': {
                                    'type': 'string'
                                },
                                'attr3': {
                                    'type': 'string'
                                }
                            }
                        },
                    ]
                }
            ]
        }
        s1 = Schema(s1_data)
        s2 = Schema(s2_data)
        p1s = s1.get_all_properties()
        self.assertEqual(4, len(p1s))
        self.assertTrue('name' in p1s)
        self.assertTrue(p1s['name'].is_property())
        self.assertTrue('username' in p1s)
        self.assertTrue(p1s['username'].is_property())
        self.assertTrue('password' in p1s)
        self.assertTrue(p1s['password'].is_property())
        self.assertTrue('email' in p1s)
        self.assertTrue(p1s['email'].is_property())

        p2s = s2.get_all_properties()
        self.assertEqual(11, len(p2s))
        self.assertTrue('name' in p2s)
        self.assertTrue(p2s['name'].is_property())
        self.assertTrue('username' in p2s)
        self.assertTrue(p2s['username'].is_property())
        self.assertTrue('password' in p2s)
        self.assertTrue(p2s['password'].is_property())
        self.assertTrue('email' in p2s)
        self.assertTrue(p2s['email'].is_property())
        self.assertTrue('uuid' in p2s)
        self.assertTrue(p2s['uuid'].is_property())
        self.assertTrue('state' in p2s)
        self.assertTrue(p2s['state'].is_property())
        self.assertTrue('environment' in p2s)
        self.assertTrue(p2s['environment'].is_property())
        self.assertTrue('release' in p2s)
        self.assertTrue(p2s['release'].is_property())
        self.assertTrue('attr1' in p2s)
        self.assertTrue(p2s['attr1'].is_property())
        self.assertTrue('attr2' in p2s)
        self.assertTrue(p2s['attr2'].is_property())
        self.assertTrue('attr3' in p2s)
        self.assertTrue(p2s['attr3'].is_property())

    def test_get_property_method(self):
        p_int = Property(Schema(type='integer'))
        p_float = Property(Schema(type='number'))
        p_bool = Property(Schema(type='boolean'))
        p_str = Property(Schema(type='string'))
        p_obj = Property(Schema(type='object'))
        p_list = Property(Schema(type='array', items=Schema(type='object')))
        
        self.assertEqual('JsonModel.field', p_int.get_model_method())
        self.assertEqual('JsonModel.field', p_float.get_model_method())
        self.assertEqual('JsonModel.field', p_bool.get_model_method())
        self.assertEqual('JsonModel.field', p_str.get_model_method())
        self.assertEqual('JsonModel.field', p_obj.get_model_method())
        self.assertEqual('JsonModel.list', p_list.get_model_method())

    def test_get_property_name(self):
        prop = Property(Schema(type='integer'), 'NAME')
        self.assertEqual('NAME', prop.name)

    def test_get_model_options(self):
        data = {
            'type': 'object',
            'required': ['in', '$ref'],
            'properties': {
                'in': {
                    'type': 'string'
                },
                '$ref': {
                    'type': 'string',
                    'title': 'TITLE',
                    'description': 'DESCRIPTION'
                },
                'attr': {
                    'type': 'string'
                }
            }
        }
        schema = Schema(data)
        props = schema.get_all_properties()
        _in = props['_in']
        _ref = props['_ref']
        attr = props['attr']
        self.assertEqual(", alias='in', required=True", _in.get_model_options())
        self.assertEqual(", alias='$ref', required=True, title='TITLE', description='DESCRIPTION'", _ref.get_model_options())
        self.assertEqual("", attr.get_model_options())






















       
