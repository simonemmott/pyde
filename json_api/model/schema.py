from json_model import JsonModel, Reference, Any
from .xml import Xml
from .external_docs import ExternalDocs
from python_dev import utils
from builtins import int
import types
import random

def random_name(length=10):
    return ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(length))


class Schema(JsonModel):
    id = JsonModel.field(str)
    type = JsonModel.field(str)
    title = JsonModel.field(str)
    multipleOf = JsonModel.field(int)
    maximum = JsonModel.field(int)
    exclusiveMaximum = JsonModel.field(int)
    minimum = JsonModel.field(int)
    exclusiveMinimum = JsonModel.field(int)
    maxLength = JsonModel.field(int)
    minLength = JsonModel.field(int)
    pattern = JsonModel.field(str)
    maxItems = JsonModel.field(int)
    minItems = JsonModel.field(int)
    uniqueItems = JsonModel.field(bool)
    maxProperties = JsonModel.field(int)
    minPropoerties = JsonModel.field(int)
    required = JsonModel.list(str)
    enum = JsonModel.list(str)
    allOf = JsonModel.list('Schema')
    anyOf = JsonModel.list('Schema')
    oneOf = JsonModel.list('Schema')
    _not = JsonModel.list('Schema', 'not')
    items = JsonModel.field('Schema')
    properties = JsonModel.dict('Schema')
    additionalProperties = JsonModel.field(bool)
    description = JsonModel.field(str)
    format = JsonModel.field(str)
    nullable = JsonModel.field(bool)
    readOnly = JsonModel.field(bool)
    writeOnly = JsonModel.field(bool)
    xml = JsonModel.field(Xml)
    externalDocs = JsonModel.field(ExternalDocs)
    example = JsonModel.field(Any)
    deprecated = JsonModel.field(bool)
    
    def is_property(self):
        return False
    
    def class_name(self):
        if self.__index__:
            return utils.to_class_case(self.__index__)
        if not hasattr(self, '__name__'):
            setattr(self, '__name__', random_name())
        return utils.to_class_case(self.__name__)
    
    def module_name(self):
        if self.__index__:
            return utils.to_snake_case(self.__index__)
        if not hasattr(self, '__name__'):
            setattr(self, '__name__', random_name())
        return utils.to_snake_case(self.__name__)
    
    def get_data_type(self):
        if self.type == 'number':
            return float
        if self.type == 'integer':
            return int
        if self.type == 'string':
            return str
        if self.type == 'boolean':
            return bool
        if self.type == 'object':
            return self
        if self.type == 'array':
            if self.items.is_reference():
                return self.items.get(force=True).get_data_type()
            return self.items.get_data_type()
        if self.allOf:
            return self
        
    def get_all_properties(self):
        if hasattr(self, '__properties__'):
            return self.__properties__
        props = {}
        if self.properties:
            for name, prop in self.properties.items():
                if prop.is_reference():
                    prop = Property(prop.get(force=True), name=name)
                else:
                    prop = Property(prop, name=name)
                props[prop.name] = prop
        if self.allOf:
            for schema in self.allOf:
                if schema.is_reference():
                    schema = schema.get(force=True)
                props.update(schema.get_all_properties())
        setattr(self, '__properties__', props)
        return props    
    
    def get_embedded_properties(self):
        embedded = []
        for prop in self.get_all_properties().values():
            data_type = prop.get_data_type()
            if isinstance(data_type, Schema):
                if not data_type.__referenced__:
                    if len(prop.get_all_properties()) > 0:
                        embedded.append(prop)
        return embedded
    
    def get_referenced_properties(self):
        referenced = []
        for prop in self.get_all_properties().values():
            data_type = prop.get_data_type()
            if isinstance(data_type, Schema):
                if data_type.__referenced__:
                    referenced.append(prop)
        return referenced
    
    def get_enumerations(self):
        enumerations = []
        for prop in self.get_all_properties().values():
            if prop.is_enum():
                enumerations.append(prop)
        return enumerations

restricted_names = ['in', 'from']
            
    
        
class Property(object):
    def __init__(self, schema, name='UN_NAMED'):
        self.alias = name
        if name in restricted_names:
            self.name = '_'+name
        elif name[0] == '$':
            self.name = '_'+name[1:]
        else:
            self.name = name
        self.schema = schema
    
    def is_property(self):
        return True
    
    def is_enum(self):
        if self.schema.enum:
            return True
        if self.schema.items:
            if self.schema.items.is_reference():
                items = self.schema.items.get(force=True)
            else:
                items = self.schema.items
            if items.enum:
                return True
        return False
    
    def get_all_properties(self):
        data_type = self.schema.get_data_type()
        if isinstance(data_type, Schema):
            return data_type.get_all_properties()
        return []
    
    def get_embedded_properties(self):
        data_type = self.schema.get_data_type()
        if isinstance(data_type, Schema):
            return data_type.get_embedded_properties()
        return []
    
    def get_enumerations(self):
        data_type = self.schema.get_data_type()
        if isinstance(data_type, Schema):
            return data_type.get_enumerations()
        return []
    
    def enumerations(self):
        if self.schema.enum:
            return self.schema.enum
        if self.schema.items:
            if self.schema.items.is_reference():
                items = self.schema.items.get(force=True)
            else:
                items = self.schema.items
            if items.enum:
                return items.enum
        return []
        
    
    def class_name(self):
        return utils.to_class_case(self.name)
    
    def get_data_type(self):
        return self.schema.get_data_type()

    def get_model_method(self):
        if self.schema.type == 'array':
            return 'JsonModel.list'
        elif self.schema.type == 'object':
            return 'JsonModel.field'
        elif self.schema.type in ['integer', 'number', 'boolean', 'string']:
            return 'JsonModel.field'
        elif self.schema.allOf:
            return 'JsonModel.field'
        return 'JsonModel.field'
        
    def get_model_options(self):
        def extend_opts(opts, key, value, quote=False):
            if isinstance(value, str):
                quote = True
            return '{opts}, {key}={q}{value}{q}'.format(
                opts=opts, 
                key=key, 
                value=value,
                q="'" if quote else ''
            )
        opts = ''
        if self.alias != self.name:
            opts = extend_opts(opts, 'alias', self.alias)
        if self.schema.__parent__ and hasattr(self.schema.__parent__, 'required') and self.alias in self.schema.__parent__.required:
            opts = extend_opts(opts, 'required', True)
        if self.schema.title:
            opts = extend_opts(opts, 'title', self.schema.title)
        if self.schema.description:
            opts = extend_opts(opts, 'description', self.schema.description)   
        return opts
        
    def get_model_type_str(self):
        if self.schema.enum:
            return "{name}Types".format(name=self.class_name())
        if self.schema.items:
            if self.schema.items.is_reference():
                items = self.schema.items.get(force=True)
            else:
                items = self.schema.items
            if items.enum:
                return "{name}Types".format(name=self.class_name())
        if self.schema.type == 'number':
            return 'float'
        elif self.schema.type == 'integer':
            return 'int'
        elif self.schema.type == 'string':
            return 'str'
        elif self.schema.type == 'object':
            if len(self.schema.get_all_properties()) == 0:
                return 'Any'
            if self.schema.__referenced__:
                return "'{name}'".format(name=utils.to_class_case(self.schema.__index__))
            else:
                return "{name}".format(name=self.class_name())
        elif self.schema.type == 'boolean':
            return 'bool'
        elif self.schema.allOf:
            if self.schema.__referenced__:
                return "'{name}'".format(name=utils.to_class_case(self.schema.__index__))
            else:
                return "{name}".format(name=self.class_name())
        elif self.schema.type == 'array':
            if self.schema.items.is_reference():
                items = self.schema.items.get(force=True)
                return Property(items, name=items.__index__).get_model_type_str()
            return Property(self.schema.items, name=self.name).get_model_type_str()
        pass
            
        
        
        
        
        
    


